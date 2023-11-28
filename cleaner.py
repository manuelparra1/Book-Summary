import re
import os

def clean_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    # Remove header text with page counts
    text = re.sub(r'\S[^\d]+\s*●\s*\d+', '', text)

    # Remove footers with original file name and date
    text = re.sub(r'Duhi_9781400069286_2p_all_r1.j.indd \d+ 10/17/11 12:01 PM', '', text)

    # Remove footers with original file name and date
    text = re.sub(r'Duhi_9781400069286_2p_all_r1.j.indd \d+ 10/17/11 12:0', '', text)
    
    # Remove hyphenated words from harcoded text wrap (PDF's)
    text = text.replace('- ', '')

    # Save the cleaned text back to the file
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(text)

def clean_all_files(directory):
    # Iterate through all files in current directory
    for filename in os.listdir(directory):
        # TODO
        # Rewrite to focus on specific text files
        if filename.endswith(".txt"):
            file_path = os.path.join(directory, filename)
            clean_text(file_path)

# Specify the directory containing your text files
directory_path = os.getcwd()

# Clean all files in the specified directory
clean_all_files(directory_path)
