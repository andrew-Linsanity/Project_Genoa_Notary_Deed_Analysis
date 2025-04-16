import re
import csv
from collections import Counter

from cltk.lemmatize.lat import LatinBackoffLemmatizer
from cltk.tokenizers.word import WordTokenizer


# lemmatizer = LatinBackoffLemmatizer()
# tokenizer = WordTokenizer(language='latin')

# --- Load Latin corpus ---
# Replace 'latin_corpus.txt' with the path to your Latin text file.
with open("latin_corpus.txt", "r", encoding="utf-8") as f:
    text = f.read()

# --- Preprocess the Text ---
# Convert to lowercase
text = text.lower()

# Remove punctuation and numbers; extract only words
words = re.findall(r'\b[a-zA-Z]+\b', text)

# --- Lemmatize the words ---
lemmatized_words = []
for word in words:
    if word.isalpha(): # double-check if the word is alphabetic
        # lemmatizer returns a list tuples (original, lemma)
        lemma = lemmatizer.lemmatize([word])[0][1]
        lemmatized_words.append(lemma)
words = lemmatized_words

# --- Count Word Frequencies ---
freq = Counter(words)

# --- Frequency Dictionary to CSV ---
# CSV file format: "word,frequency"
with open("latin_dictionary.csv", "w", encoding="utf-8", newline="") as csvfile:
    writer = csv.writer(csvfile)
    # Optional: write header
    # writer.writerow(["word", "frequency"])
    for word, count in freq.items():
        writer.writerow([word, count])

print("Latin frequency dictionary created and saved as 'latin_dictionary.csv'.")
