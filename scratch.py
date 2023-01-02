import nltk
from nltk import word_tokenize
nltk.download('punkt')

text = word_tokenize("And now for something completely different")
tagged = nltk.pos_tag(text)
#print(tagged)
verbs_nouns = [w[0] for w in tagged if w[1]=='VP' or w[1]=='NN']
print(verbs_nouns)