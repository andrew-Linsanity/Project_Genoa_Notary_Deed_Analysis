from langid import classify, rank
import os
import re
import math

def is_roman_number(s: str) -> bool:
    # allows one or more of the allowed characters, followed by an optional dot at the end.
    pattern = r'^[IVXLCDMTNHEYAWO]+\.?,?$'
    return bool(re.fullmatch(pattern, s))

def is_deed(paragraph):
    if paragraph.startswith("["):
        parts = paragraph.split("].") 
        if len(parts) > 1:
            deed_roman = parts[1].strip()
            if is_roman_number(deed_roman):
                return True, deed_roman
            
    if(is_roman_number(paragraph)):
        return True, paragraph
    
    return False, None

def split_deeds(input_file, output_dir):
    with open(input_file, 'r', encoding='utf-8') as f:
        paragraphs = f.read().split('\n\n')  # Separate by double newline

    deeds = {}
    current_deed = None
    current_content = []

    for paragraph in paragraphs:
        paragraph = paragraph.strip()

        is_new, deed_id = is_deed(paragraph)
        if is_new:
            if current_deed and current_content:
                deeds[current_deed] = '\n\n'.join(current_content)
                current_content = []

            current_deed = deed_id
        if current_deed:
            current_content.append(paragraph)

    if current_deed and current_content:
        deeds[current_deed] = '\n\n'.join(current_content)

    # TODO: GiovanniScriba_DeedNumber_Date
    # Write out each deed to a separate file
    os.makedirs(output_dir, exist_ok=True)
    for deed_id, content in deeds.items():
        filename = f"{output_dir}/deed_{deed_id}.txt"
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)

    print(f"{len(deeds)} deeds extracted to {output_dir}/")

# Example usage
split_deeds("deeds_input.txt", "split_deeds_output")