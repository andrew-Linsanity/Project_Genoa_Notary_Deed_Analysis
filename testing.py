from langid import classify, rank
import os
import re
import math


BASE_DIR = os.path.dirname(os.path.abspath(__file__))  
DATA_DIR = os.path.join(BASE_DIR, "data")  

os.makedirs(DATA_DIR, exist_ok=True) 

INPUT_FILE = os.path.join(DATA_DIR, "input.txt")    
OUTPUT_ITALIAN = os.path.join(DATA_DIR, "test_italian_output.txt")
OUTPUT_LATIN = os.path.join(DATA_DIR, "test_latin_output.txt")
OUTPUT_NONE = os.path.join(DATA_DIR, "test_none_output.txt")

def clean_text(text):
    """
    Cleans the text by removing:
    1. Lines containing "MARIO"
    2. Lines that start with a parenthesis containing a number, like "(1)" or "(23)"
    """
    cleaned_lines = []
    for line in text.splitlines():
        if ("MARIO CHIAUDANO" in line) or ("GIOVANNI SCRIBA" in line):
            continue
        if re.match(r'^\(\s*\d+\s*\)', line.strip()):  # Matches lines starting with (number)
            continue
        cleaned_lines.append(line)
    return "\n".join(cleaned_lines)

def compute_probability(text, top_score):
    """
    Compute prob
    """
    language_ranking = rank(text)  # ranking, tuple (lang, log_prob)
    # log probability -> non-normalized prob
    exp_scores = [math.exp(score) for lang, score in language_ranking]
    total = sum(exp_scores)
    return math.exp(top_score) / total

def rank_Italian_Latin(text):
    """
    Compute probability for Italian and Latin 
    """
    language_ranking = rank(text)  
    exp_scores = [math.exp(score) for lang, score in language_ranking]
    total = sum(exp_scores)
    
    it_prob = 0
    la_prob = 0
    
    for lang, score in language_ranking:
        if lang == 'it':
            it_prob = math.exp(score) / total
        elif lang == 'la':
            la_prob = math.exp(score) / total
    
    # Return the language with the higher probability
    if it_prob > la_prob:
        return 'it'
    else:
        return 'la'
    
    # TODO: add a lower bound to the prob 

def is_roman_number(s: str) -> bool:
    # The pattern allows one or more of the allowed characters, followed by an optional dot at the end.
    pattern = r'^[IVXLCDMTNHEYAWO]+\.?,?$'
    return bool(re.fullmatch(pattern, s))

def is_deed(paragraph):
    if paragraph.startswith("["):
        parts = paragraph.split("].") 
        if len(parts) > 1:
            deed_roman = parts[1].strip()
            if is_roman_number(deed_roman):
                return True, deed_roman

    if(is_roman_number(paragraph[:-1])):
        return True, paragraph[:-1]
    
    return False, None

    
def separate_italian_latin(input_file, output_italian, output_latin, output_none):
    # print("Start Running separate_italian_latin.py")
    italian_paragraphs = []
    latin_paragraphs = []
    non_categorized = []

    with open(input_file, 'r', encoding='utf-8', errors='ignore') as file:
        text = file.read()
        paragraphs = text.split("\n\n")  

        for paragraph in paragraphs:
            paragraph = paragraph.strip() 
            # print(paragraph + '\n')
            
            paragraph = clean_text(paragraph)
            if not paragraph:
                continue  # Skip empty paragraphs
            
            is_deed_bool, deed_roman = is_deed(paragraph)
            if(is_deed_bool):
                deed_roman = deed_roman.rstrip(".")
                italian_paragraphs.append(deed_roman)
                latin_paragraphs.append(deed_roman)
                continue
            try:
                detected_lang, confidence = classify(paragraph)
                # probability = compute_probability(paragraph, confidence)
                
                if detected_lang == 'it':  # Italian
                    
                    italian_paragraphs.append(paragraph)
                    # italian_paragraphs.append('\n')
                elif detected_lang == 'la':  # Latin
                    latin_paragraphs.append(paragraph)
                    # latin_paragraphs.append('\n')
                else:
                    if(rank_Italian_Latin == 'it'):
                        italian_paragraphs.append(paragraph)
                        # italian_paragraphs.append('\n')
                    else:
                        latin_paragraphs.append(paragraph)
                        # latin_paragraphs.append('\n')
                    # non_categorized.append(paragraph + '\n')
                    # if(probability > 0.69):
                    #     print(f"Detected language: {detected_lang} with probability {probability:.2f}")
                    #     print(paragraph)
            except:
                print("Unknown Languages")
    
    
    # Write Italian lines to output file
    with open(output_italian, 'w', encoding='utf-8') as file:
        file.write("\n".join(italian_paragraphs))

    # Write Latin lines to output file
    with open(output_latin, 'w', encoding='utf-8') as file:
        file.write("\n".join(latin_paragraphs))

    with open(output_none, 'w', encoding='utf-8') as file:
        file.write("\n".join(non_categorized))  

separate_italian_latin(INPUT_FILE, OUTPUT_ITALIAN, OUTPUT_LATIN, OUTPUT_NONE)
