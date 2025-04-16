import os
import re
from spellchecker import WordFrequency
import json

def custom_tokenizer(text):
    return re.findall(r'[a-zA-Z]+', text.lower())


word_freq = WordFrequency()
folder_path = "Latin Corpus"

for filename in os.listdir(folder_path):
    if filename.endswith(".tess"):
        path = os.path.join(folder_path, filename)
        word_freq.load_text_file(path)

print("Total words:", word_freq.total_words) 

# Save to a JSON file
with open('latin_dict.json', 'w', encoding='utf-8') as f:
    json.dump(word_freq.dictionary, f, ensure_ascii=False, indent=2)