import random
import re
from pathlib import Path

import llm


DEFAULT_OUTPUT = Path("dataset-ex226.txt")
DEFAULT_COUNT = 10000
DEFAULT_BATCH_SIZE = 12
DEFAULT_MODEL = "gemma4:e2b"

# Hardcoded run settings. Edit these values directly when you want a different run.
COUNT = DEFAULT_COUNT
BATCH_SIZE = DEFAULT_BATCH_SIZE
MODEL = DEFAULT_MODEL
OUTPUT_PATH = DEFAULT_OUTPUT


SUBJECTS = [
    "a baker",
    "a bus driver",
    "a carpenter",
    "a teacher",
    "a software engineer",
    "a doctor",
    "a gardener",
    "a pilot",
    "a painter",
    "a mechanic",
    "a student",
    "a farmer",
    "a scientist",
    "a musician",
    "a librarian",
    "a coach",
    "a nurse",
    "a journalist",
    "a plumber",
    "a designer",
]


SETTINGS = [
    "at sunrise",
    "during a rainy afternoon",
    "in a busy city",
    "on a quiet weekend",
    "inside a small workshop",
    "at a train station",
    "near the ocean",
    "in a mountain town",
    "before dinner",
    "after a long day",
    "on a bright Monday morning",
    "late at night",
]


ACTIONS = [
    "finds a simple solution",
    "notices a small detail",
    "finishes the task early",
    "helps a neighbor",
    "plans the next step carefully",
    "keeps the room tidy",
    "starts the work with confidence",
    "shares a useful idea",
    "waits for the right moment",
    "checks the result twice",
    "writes down the important parts",
    "makes a careful choice",
]


TONES = [
    "calm and factual",
    "warm and reflective",
    "plain and direct",
    "light and hopeful",
    "simple and natural",
    "clear and descriptive",
]


OPENERS = [
    "The",
    "A",
    "Each",
    "One",
    "Every",
    "This",
]


def _existing_sentences(path: Path) -> set[str]:
    if not path.exists():
        return set()
    with path.open("r", encoding="utf-8", errors="ignore") as fh:
        return {line.rstrip("\n") for line in fh if line.strip()}


def _build_prompt(batch_size: int) -> str:
    return (
        "Generate "
        f"{batch_size} short, original, correctly capitalized sentences.\n"
        "Rules:\n"
        "- Output one sentence per line.\n"
        "- Do not number the lines.\n"
        "- Do not use bullet points or quotes.\n"
        "- Every sentence must start with a capital letter and end with a period, question mark, or exclamation point.\n"
        "- Keep each sentence between 6 and 18 words.\n"
        "- Make the sentences diverse and random.\n"
        "- Do not repeat any sentence.\n"
        "- Avoid names, code, lists, and markdown.\n"
        "\n"
        "Mix these ingredients freely:\n"
        f"- subjects: {', '.join(random.sample(SUBJECTS, k=min(8, len(SUBJECTS))))}\n"
        f"- settings: {', '.join(random.sample(SETTINGS, k=min(6, len(SETTINGS))))}\n"
        f"- actions: {', '.join(random.sample(ACTIONS, k=min(8, len(ACTIONS))))}\n"
        f"- tones: {', '.join(random.sample(TONES, k=min(4, len(TONES))))}\n"
        f"- openers: {', '.join(random.sample(OPENERS, k=min(4, len(OPENERS))))}\n"
    )


def _extract_sentences(text: str) -> list[str]:
    lines = []
    for raw_line in text.splitlines():
        line = raw_line.strip()
        if not line:
            continue
        line = re.sub(r"^\s*(?:[-*]|\d+[.)])\s*", "", line)
        line = line.strip().strip('"').strip("'")
        if not line:
            continue
        if line[0].islower():
            continue
        if len(line.split()) < 4:
            continue
        if not re.search(r"[.?!]$", line):
            line += "."
        lines.append(line)
    return lines


def generate_sentences(count: int, batch_size: int, model: str, output_path: Path) -> list[str]:
    generated: list[str] = []
    seen = set()
    existing = _existing_sentences(output_path)
    seen.update(existing)

    attempts = 0
    max_attempts = max(10, (count // max(1, batch_size)) * 4)

    while len(generated) < count and attempts < max_attempts:
        need = min(batch_size, count - len(generated))
        prompt = _build_prompt(need)
        attempts += 1
        print(f"Requesting {need} sentences from {model} (attempt {attempts})")
        try:
            response = llm.invoke(prompt, model=model)
        except TypeError:
            response = llm.invoke(prompt)
        except Exception as exc:
            print(f"LLM invocation failed: {exc}")
            continue

        for sentence in _extract_sentences(response):
            if sentence in seen:
                continue
            seen.add(sentence)
            generated.append(sentence)
            if len(generated) >= count:
                break

    return generated


def append_sentences(sentences: list[str], output_path: Path) -> None:
    if not sentences:
        return
    output_path.parent.mkdir(parents=True, exist_ok=True)
    needs_leading_newline = False
    if output_path.exists() and output_path.stat().st_size > 0:
        with output_path.open("rb") as fh:
            fh.seek(-1, 2)
            needs_leading_newline = fh.read(1) != b"\n"
    with output_path.open("a", encoding="utf-8") as fh:
        if needs_leading_newline:
            fh.write("\n")
        fh.write("\n".join(sentences))
        fh.write("\n")


def main() -> None:
    if COUNT <= 0:
        raise SystemExit("COUNT must be positive")
    if BATCH_SIZE <= 0:
        raise SystemExit("BATCH_SIZE must be positive")

    sentences = generate_sentences(COUNT, BATCH_SIZE, MODEL, OUTPUT_PATH)
    append_sentences(sentences, OUTPUT_PATH)

    print(f"Appended {len(sentences)} sentences to {OUTPUT_PATH}")
    if len(sentences) < COUNT:
        print(f"Warning: requested {COUNT}, but only generated {len(sentences)} unique sentences.")


if __name__ == "__main__":
    main()
