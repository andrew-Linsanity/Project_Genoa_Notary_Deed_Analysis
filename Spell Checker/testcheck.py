from spellchecker import SpellChecker

# Load the custom Latin dictionary
latin_spell = SpellChecker(language=None)  # language=None allows custom dictionaries
latin_spell.word_frequency.load_text_file('latin_dict.txt')

# Sample Latin sentence with some intentional typos
sample_text = "Puella videt lupos in sylva magna. Amikus est fortis."

# Tokenize the sentence (basic whitespace split for now)
words = sample_text.lower().replace('.', '').split()

# Check for misspelled words
misspelled = latin_spell.unknown(words)

print("Misspelled words:", misspelled)

# Optional: get suggestions
for word in misspelled:
    print(f"Suggestions for '{word}': {latin_spell.candidates(word)}")
