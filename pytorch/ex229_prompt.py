import random
from ex226_gen import keywords
from ex226_eval import eval_samples

def build_prompts(failure_stats, count=5):
    top = sorted(failure_stats.items(), key=lambda x: x[1], reverse=True)[:3]
    top_categories = [k for k, v in top]
    
    prompts = []
    
    targeted_count = int(count * 0.7)
    mutation_count = int(count * 0.1)
    random_count = count - targeted_count - mutation_count
    
    # In case targeted_count is 0 but we want to generate at least 1, we can adjust
    if count > 0 and targeted_count == 0 and random_count == 0:
        targeted_count = count
        mutation_count = 0
        
    if top_categories:
        cat_str = ", ".join(top_categories)
    else:
        cat_str = "general capitalization rules"
        
    for _ in range(targeted_count):
        prompts.append(
            f"Generate a paragraph emphasizing these capitalization cases: {cat_str}.\n"
            f"Use diverse formats: dialogue, essays, lists, or informal writing.\n"
            f"Return only raw text."
        )
        
    for _ in range(mutation_count):
        sample = random.choice(eval_samples)
        prompts.append(
            f"Rewrite this text while preserving capitalization complexity:\n'{sample}'\n"
            f"Add more named entities, acronyms, and proper nouns.\nReturn only raw text."
        )
        
    for _ in range(random_count):
        topic = random.choice(keywords)
        prompts.append(
            f"Write a short text about '{topic}'. Include a mix of proper nouns, "
            f"acronyms, and standard sentences.\nReturn only raw text."
        )
        
    random.shuffle(prompts)
    return prompts
