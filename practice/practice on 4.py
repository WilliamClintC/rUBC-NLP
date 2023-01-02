import nltk
from nltk.corpus import wordnet

syn = wordnet.synsets('Love')
print(syn[1].definition())
print(syn[0].definition())

synonyms=[]
for syn in wordnet.synsets('Love'):
    for lemma in syn.lemmas():
        synonyms.append(lemma.name())
print(synonyms)

antonyms=[]
for syn in wordnet.synsets('Love'):
    for lemma in syn.lemmas():
        if lemma.antonyms():
            antonyms.append(lemma.antonyms()[0].name())
       
print(antonyms)