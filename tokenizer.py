import os
import spacy
import json

nlp = spacy.load("en_core_web_sm")

# Get a list of all text files in the current directory with a specific naming pattern
text_files = [file for file in os.listdir() if file.endswith(".txt") and "power_of_habit_chapter_" in file]

# Create a dictionary to store token chunks
token_chunks_dict = {}

# Process each text file
for file_name in text_files:
    with open(file_name, 'r', encoding='utf-8') as file:
        text = file.read()

    # Create a spacy doc object
    doc = nlp(text)

    # Split the doc object into chunks of 4000 tokens each
    chunk_size = 4000
    chunks = [doc[i:i + chunk_size] for i in range(0, len(doc), chunk_size)]

    # Store the token chunks in the dictionary
    token_chunks_dict[file_name] = [{"section": i + 1, "tokens": len(chunk), "text": chunk.text} for i, chunk in enumerate(chunks)]

# Save the dictionary as a JSON file
output_file = "token_chunks.json"
with open(output_file, 'w', encoding='utf-8') as json_file:
    json.dump(token_chunks_dict, json_file, ensure_ascii=False, indent=4)

print(f"Token chunks saved to {output_file}")
