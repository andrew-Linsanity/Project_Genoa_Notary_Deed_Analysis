from cltk.ner.spacy_ner import spacy_tag_ner
from nltk.tokenize import word_tokenize
# Initialize Latin CLTK pipeline

# A list of Word objects, each with attributes like:
# string – the original word form (e.g., 'Gallia')
# lemma – the lemma form (e.g., 'Gallia')
# pos – part of speech (e.g., 'NOUN')
# morph – morphological features (e.g., Case=Nom|Gender=Fem|Number=Sing)
# index – word position in the sentence
# TODO: worth look into 


text_tokens = word_tokenize("Gallia est omnis divisa in partes tres", language='lat')
spacy_tag_ner('lat', text_tokens=text_tokens)
# lemmatized results
for word in doc.words:
    if "named_entity" in word.features._features:
    ner = word.features._features["named_entity"]
    print(f"{word.string} --> {ner}")
