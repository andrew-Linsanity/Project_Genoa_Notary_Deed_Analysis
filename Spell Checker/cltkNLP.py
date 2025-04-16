from cltk.ner.spacy_ner import spacy_tag_ner
from cltk.tokenizers.word import WordTokenizer

# Original Spacy Version: spaCy v3.7.5
text = "Marcus Tullius Cicero in senatu locutus est."

# Instantiate the tokenizer
tokenizer = WordTokenizer()

# Use the instance to tokenize
text_tokens = tokenizer.tokenize(text)

# Tag the tokens
tagged_list = spacy_tag_ner('lat', text_tokens=text_tokens)

# Print results
print("word, tag")
for word, tag in tagged_list:
    print(f"{word} , {tag}")

    
