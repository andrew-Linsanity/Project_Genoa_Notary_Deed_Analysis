import stanza
from cltk import NLP as CLTK_NLP
import pandas as pd

# --- SETUP ---

# Download models (run once)
stanza.download('la')

# Initialize Stanza & CLTK
stanza_nlp = stanza.Pipeline(lang='la', processors='tokenize,pos,lemma,depparse')
cltk_nlp = CLTK_NLP(language="lat")

# --- INPUT ---

with open("input_latin.txt", "r", encoding="utf-8") as f:
    text = f.read()

# --- PROCESS WITH CLTK ---
cltk_doc = cltk_nlp.analyze(text)

# --- PROCESS WITH STANZA ---
stanza_doc = stanza_nlp(text)

# Collect token-level info
tokens = []
for sent in stanza_doc.sentences:
    for word in sent.words:
        tokens.append({
            "id": word.id,
            "text": word.text,
            "lemma": word.lemma,
            "pos": word.xpos,
            "head": word.head,
            "deprel": word.deprel
        })

# --- PROCESS WITH CLTK ---
cltk_doc = cltk_nlp.analyze(text)

# Extract entities from CLTK using word.features
cltk_ents = []
current_entity = []
current_label = None

for word in cltk_doc.words:
    feats = word.features
    if feats and "named_entity" in feats:
        label = feats["named_entity"]
        if current_label == label:
            current_entity.append(word.string)
        else:
            if current_entity:
                cltk_ents.append((" ".join(current_entity), current_label))
            current_entity = [word.string]
            current_label = label
    else:
        if current_entity:
            cltk_ents.append((" ".join(current_entity), current_label))
            current_entity = []
            current_label = None

# Append any remaining entity
if current_entity:
    cltk_ents.append((" ".join(current_entity), current_label))

# --- ALIGN NER TAGS TO TOKENS ---

def assign_ner(tokens, cltk_ents):
    ner_tags = ["O"] * len(tokens)
    i = 0
    while i < len(tokens):
        for ent_text, ent_type in cltk_ents:
            ent_tokens = ent_text.split()
            match = True
            for j in range(len(ent_tokens)):
                if i + j >= len(tokens) or tokens[i + j]['text'] != ent_tokens[j]:
                    match = False
                    break
            if match:
                ner_tags[i] = f"B-{ent_type}"
                for j in range(1, len(ent_tokens)):
                    ner_tags[i + j] = f"I-{ent_type}"
                i += len(ent_tokens) - 1
                break
        i += 1
    return ner_tags

ner_tags = assign_ner(tokens, cltk_ents)

# --- COMBINE INTO CONLL TABLE ---
for i, tag in enumerate(ner_tags):
    tokens[i]["ner"] = tag
    tokens[i]["idx"] = i + 1  # global token ID

# --- OUTPUT TO CSV ---
df = pd.DataFrame(tokens)
df = df[["idx", "text", "lemma", "pos", "head", "deprel", "ner"]]
df.columns = ["ID", "FORM", "LEMMA", "POS", "HEAD", "DEPREL", "NER"]

df.to_csv("conll_output_cltk.csv", index=False, encoding="utf-8")
print("CoNLL table with CLTK NER written to conll_output_cltk.csv")
