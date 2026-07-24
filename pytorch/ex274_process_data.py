import json
import glob
import os
import re
import traceback
import unicodedata
import time
import shutil
from typing import Any, Dict, List, Optional, Tuple

try:
    from tqdm import tqdm
except Exception:
    tqdm = None


def load_json(path: str) -> Any:
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


def save_json(path: str, data: Any) -> None:
    temp_path = f"{path}.tmp"
    with open(temp_path, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=2)
    os.replace(temp_path, path)


def save_with_backup(path: str, data: Any) -> None:
    backup_path = f"{path}.{int(time.time())}.bak"
    if os.path.exists(path):
        try:
            shutil.copy2(path, backup_path)
        except Exception as exc:
            print(f"Could not refresh backup {backup_path}: {exc}")
    save_json(path, data)


def normalize_text(text: str) -> str:
    text = text.strip().lower()
    text = unicodedata.normalize("NFKD", text)
    text = "".join(ch for ch in text if not unicodedata.combining(ch))
    text = re.sub(r"[^\w\s]+", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def strip_trailing_descriptor(title: str) -> str:
    title = title.strip()

    while True:
        new_title = re.sub(r"\s*[\(\[\{][^\)\]\}]*[\)\]\}]\s*$", "", title).strip()
        if new_title == title:
            break
        title = new_title

    title = re.sub(
        r"\s*(official music video|official video|music video|official audio|audio|lyrics?|lyric video|mv|ost|soundtrack|live music video|full album|playlist|extended|remix|cover)\s*$",
        "",
        title,
        flags=re.IGNORECASE,
    ).strip()
    return title


def canonical_title(title: str) -> str:
    return normalize_text(strip_trailing_descriptor(title))


def heuristic_is_music(title: str) -> Tuple[bool, bool]:
    text = normalize_text(title)

    music_signals = [
        "official music video",
        "official video",
        "music video",
        "official audio",
        "audio",
        "lyrics",
        "lyric",
        "ost",
        "soundtrack",
        "cover",
        "remix",
        "mix",
        "theme song",
        "theme",
        "song",
        "single",
        "live music video",
        "mv",
    ]
    non_music_signals = [
        "interview",
        "trailer",
        "gameplay",
        "walkthrough",
        "playthrough",
        "longplay",
        "review",
        "highlights",
        "analysis",
        "commentary",
        "podcast",
        "news",
        "launch date",
        "match",
        "game awards",
        "full game",
    ]

    music_score = 0
    non_music_score = 0

    for signal in music_signals:
        if signal in text:
            music_score += 2

    for signal in non_music_signals:
        if signal in text:
            non_music_score += 2

    if " - " in title or " ft " in f" {text} " or " feat " in f" {text} ":
        music_score += 1
    if "ost" in text or "soundtrack" in text:
        music_score += 2
    if text in {"youtube", "[", "]"}:
        non_music_score += 3

    is_music = music_score >= non_music_score
    confident = not (
        (music_score == 0 and non_music_score == 0)
        or abs(music_score - non_music_score) <= 1
    )
    return is_music, confident


def llm_is_music(title: str, llm_module: Any) -> Optional[bool]:
    prompt = (
        "Decide whether this YouTube title is a music video or song video.\n"
        "Reply with exactly one token: MUSIC or NOT_MUSIC.\n\n"
        f"Title: {title}"
    )
    response = str(llm_module.invoke(prompt, model="gpt-5-nano")).strip().lower()
    if "not_music" in response or "not music" in response:
        return False
    if "music" in response:
        return True
    return None


def classify_title(title: str, llm_module: Any = None) -> bool:
    stripped_title = strip_trailing_descriptor(title)
    heuristic_result, confident = heuristic_is_music(stripped_title)
    if confident:
        return heuristic_result

    if llm_module is not None and hasattr(llm_module, "invoke"):
        try:
            llm_result = llm_is_music(stripped_title, llm_module)
            if llm_result is not None:
                return llm_result
            print(f"LLM returned an unparseable label for title={title!s}; using heuristic result")
        except Exception as exc:
            print(f"LLM classification failed for title={title!s}: {exc}")

    return heuristic_result


def load_title_cache(path: str) -> Dict[str, Dict[str, Any]]:
    title_cache: Dict[str, Dict[str, Any]] = {}
    if not os.path.exists(path):
        return title_cache

    try:
        for row in load_json(path):
            if not isinstance(row, dict) or "title" not in row:
                continue

            key = canonical_title(str(row["title"]))
            cached_entry = title_cache.setdefault(key, {})
            cached_entry["title"] = str(row["title"])
            if "is_music" in row:
                cached_entry["is_music"] = bool(row["is_music"])
            if "audio_description" in row:
                cached_entry["audio_description"] = str(row.get("audio_description", ""))
            if "embeddings" in row and isinstance(row["embeddings"], dict):
                cached_entry["embeddings"] = dict(row["embeddings"])
    except Exception as exc:
        print(f"Could not load existing {path}; starting fresh: {exc}")

    return title_cache


def load_title_cache_with_backup(path: str) -> Dict[str, Dict[str, Any]]:
    title_cache = load_title_cache(path)
    if title_cache:
        return title_cache

    backup_paths = glob.glob(f"{path}.*.bak")
    backup_paths.sort(reverse=True)
    for backup_path in backup_paths:
        cached = load_title_cache(backup_path)
        if cached:
            print(f"Falling back to backup cache {backup_path}")
            return cached

    return title_cache


def main() -> None:
    source_path = "data.txt"
    out_path = "out.json"

    try:
        import llm
    except Exception:
        llm = None

    models_env = os.getenv("EMBEDDING_MODELS")
    if models_env:
        models = [model.strip() for model in models_env.split(",") if model.strip()]
    elif llm is not None and hasattr(llm, "EMBEDDING_MODEL"):
        models = [getattr(llm, "EMBEDDING_MODEL")]
    else:
        models = ["text-embedding-3-small", "text-embedding-3-large"]

    title_cache = load_title_cache_with_backup(out_path)

    with open(source_path, "r", encoding="utf-8") as file:
        lines = [line.strip() for line in file.read().splitlines() if line.strip()]

    source_rows: List[Dict[str, Any]] = []
    for line in lines:
        if line == "title#timestamp":
            continue

        if "#" in line:
            title, timestamp = line.rsplit("#", 1)
        else:
            title, timestamp = line, ""

        source_rows.append(
            {
                "title": title.strip(),
                "timestamp": timestamp.strip(),
            }
        )

    title_groups: Dict[str, Dict[str, Any]] = {}
    for row in source_rows:
        key = canonical_title(row["title"])
        group = title_groups.setdefault(
            key,
            {
                "title": row["title"],
                "rows": [],
            },
        )
        group["rows"].append(row)

    description_cache: Dict[str, str] = {}
    embedding_cache: Dict[str, Dict[str, Any]] = {}
    music_cache: Dict[str, bool] = {}

    for key, cached_row in title_cache.items():
        description_cache[key] = str(cached_row.get("audio_description", ""))
        embedding_cache[key] = dict(cached_row.get("embeddings", {}))
        if "is_music" in cached_row:
            music_cache[key] = bool(cached_row["is_music"])

    if llm is not None and not hasattr(llm, "invoke"):
        print("llm.invoke not available; audio descriptions will be empty")
    if llm is not None and not hasattr(llm, "get_embedding"):
        print("llm.get_embedding not available; embeddings will be empty")

    unique_titles = list(title_groups.items())
    iterable = tqdm(unique_titles, desc="Processing titles") if tqdm is not None else unique_titles

    for key, group in iterable:
        title = str(group["title"])
        if key not in music_cache:
            music_cache[key] = classify_title(title, llm_module=llm)

        cached_title = title_cache.get(key, {})
        if cached_title:
            description_cache.setdefault(key, str(cached_title.get("audio_description", "")))
            if key not in embedding_cache and isinstance(cached_title.get("embeddings"), dict):
                embedding_cache[key] = dict(cached_title["embeddings"])

        if key not in description_cache:
            audio_description = ""
            if music_cache[key] and llm is not None and hasattr(llm, "invoke"):
                try:
                    prompt = (
                        "Write a single-line audio-to-text description of what this song "
                        "is probably supposed to sound like, or include any known info. "
                        "Keep it to one sentence and do not add bullet points.\n\n"
                        f"Title: {title}"
                    )
                    audio_description = str(llm.invoke(prompt, model="gpt-5-nano")).strip()
                except Exception as exc:
                    print(f"Audio description failed for title={title!s}: {exc}")
                    audio_description = ""
            description_cache[key] = audio_description

        cached_embeddings = dict(embedding_cache.get(key, {}))
        missing_models = [model for model in models if model not in cached_embeddings]
        if music_cache[key] and missing_models:
            embedding_target = f"{title}\n{description_cache[key]}".strip()
            for model in missing_models:
                emb = None
                if llm is not None and hasattr(llm, "get_embedding"):
                    try:
                        emb = llm.get_embedding(embedding_target, model=model)
                    except Exception as exc:
                        print(f"Embedding failed for model={model!s}, title={title!s}: {exc}")
                        emb = None
                cached_embeddings[model] = emb
        embedding_cache[key] = cached_embeddings
        title_cache[key] = {
            "title": title,
            "is_music": music_cache[key],
            "audio_description": description_cache.get(key, ""),
            "embeddings": dict(embedding_cache.get(key, {})),
        }

        save_with_backup(
            out_path,
            [
                {
                    "title": item["title"],
                    "timestamp": item["timestamp"],
                    "is_music": bool(music_cache[canonical_title(item["title"])])
                    if canonical_title(item["title"]) in music_cache
                    else False,
                    "audio_description": description_cache.get(canonical_title(item["title"]), ""),
                    "embeddings": {
                        model: embedding_cache.get(canonical_title(item["title"]), {}).get(model)
                        for model in models
                    }
                    if music_cache.get(canonical_title(item["title"]), False)
                    else {},
                }
                for item in source_rows
            ],
        )
        if tqdm is not None:
            iterable.set_postfix_str(f"saved={len(source_rows)}")

    save_with_backup(
        out_path,
        [
            {
                "title": item["title"],
                "timestamp": item["timestamp"],
                "is_music": bool(music_cache[canonical_title(item["title"])])
                if canonical_title(item["title"]) in music_cache
                else False,
                "audio_description": description_cache.get(canonical_title(item["title"]), ""),
                "embeddings": {
                    model: embedding_cache.get(canonical_title(item["title"]), {}).get(model)
                    for model in models
                }
                if music_cache.get(canonical_title(item["title"]), False)
                else {},
            }
            for item in source_rows
        ],
    )
    print(f"Wrote {out_path} with {len(source_rows)} rows")


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"process_data.py failed: {exc}")
        traceback.print_exc()
        raise
