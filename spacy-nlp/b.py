import spacy
from spacy.tokens import Span

# Load a pre-trained model for NER
nlp = spacy.load("en_core_web_sm")

# Define a dictionary mapping player/team names to unique identifiers
player_team_mapping = {
    "cp3": "0b2c",
    "lakers": "4e7d",
    "lbj": "0a1f"
    # Add more mappings here
}

# Custom function to replace identified entities with unique identifiers
def replace_entities(doc):
    for ent in doc.ents:
        if ent.text.lower() in player_team_mapping:
            ent._.custom_id = player_team_mapping[ent.text.lower()]

# Add the custom attribute to the entities
Span.set_extension("custom_id", default=None, force=True)

# Process the text and replace entities with unique identifiers
text = "what is lbj ppg"
doc = nlp(text)
replace_entities(doc)

# Print the modified sentence
print([token.ent_type for token in doc])
modified_text = " ".join(token.text if token.ent_type == "" else player_team_mapping[token.text.lower()] or token.text for token in doc)
print(modified_text)
