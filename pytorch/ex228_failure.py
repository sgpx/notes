import json
import llm

def llm_classify(failures):
    if not failures:
        return []
    
    prompt = "Classify capitalization errors into categories.\n\nExamples of categories: person_name, acronym, city_name, title, punctuation, etc.\n\nFailures:\n"
    for f in failures:
        prompt += f"gold:\n{f['gold']}\npred:\n{f['pred']}\n\n"
        
    prompt += "Return ONLY a valid JSON object in this format:\n{\n  \"categories\": [\"person_name\", \"acronym\"]\n}\n"
    
    try:
        response = llm.invoke(prompt)
        if "```json" in response:
            response = response.split("```json")[1].split("```")[0]
        elif "```" in response:
            response = response.split("```")[1].split("```")[0]
            
        data = json.loads(response.strip())
        return data.get("categories", [])
    except Exception as e:
        print(f"Error classifying failures via LLM: {e}")
        return []
