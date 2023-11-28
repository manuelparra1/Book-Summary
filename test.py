import json

# Load the token chunks from the JSON file
with open("token_chunks.json", 'r', encoding='utf-8') as json_file:
    token_chunks_dict = json.load(json_file)

print(token_chunks_dict['power_of_habit_chapter_1.txt'].keys())
# Iterate over each file and its chunks, sending them to the GPT-3.5 API for summarization

#for file_name, chunks in token_chunks_dict.items():
#    for i, chunk_info in enumerate(chunks):
