import openai
import json

# Set your OpenAI API key
openai.api_key = 'your-api-key'  # Replace 'your-api-key' with your actual API key

# Load the token chunks from the JSON file
with open("token_chunks.json", 'r', encoding='utf-8') as json_file:
    token_chunks_dict = json.load(json_file)

# Dictionary to store summaries
summaries = {}

# Iterate over each file and its chunks, sending them to the GPT-3.5 API for summarization
for file_name, chunks in token_chunks_dict.items():
    for i, chunk_info in enumerate(chunks):
        # Adjust the prompt and parameters based on your specific needs
        prompt = f"Summarize the following text:\n\n{chunk_info['text']}"
        response = openai.Completion.create(
            engine="text-davinci-003",  # or use another engine
            prompt=prompt,
            max_tokens=100,
            temperature=0.7  # Adjust temperature if needed
        )

        # Extract and store the generated summary in the dictionary
        summary = response['choices'][0]['text'].strip()
        key = f"{file_name}_chunk_{i + 1}_summary"
        summaries[key] = summary

# Print or use the summaries dictionary as needed
for key, value in summaries.items():
    print(f"{key}: {value}\n")
