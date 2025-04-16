import re
from spellchecker import SpellChecker

def correct_text(text, spell):
    import re
    tokens = re.findall(r'\w+|\W+', text)
    corrected_tokens = []

    for token in tokens:
        if re.match(r'\w+', token):
            word_lower = token.lower()
            if word_lower not in spell:
                correction = spell.correction(word_lower)
                if correction is None:
                    correction = token  # fallback to original token
                elif token[0].isupper():
                    correction = correction.capitalize()
                corrected_tokens.append(correction)
            else:
                corrected_tokens.append(token)
        else:
            corrected_tokens.append(token)
    
    return "".join(corrected_tokens)

def main():
    spell = SpellChecker(language=None)
    spell.word_frequency.load_dictionary('latin_dict.json')

    input_filename = 'test_input.txt'
    output_filename = 'corrected_input.txt'
    
    with open(input_filename, 'r', encoding='utf-8') as infile:
        text = infile.read()

    corrected_text = correct_text(text, spell)
    
    with open(output_filename, 'w', encoding='utf-8') as outfile:
        outfile.write(corrected_text)
    
    print(f"Corrected file saved as '{output_filename}'.")

if __name__ == '__main__':
    main()
