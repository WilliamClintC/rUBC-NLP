import nltk
nltk.download('wordnet')
nltk.download('vader_lexicon')
from nltk.stem import PorterStemmer,WordNetLemmatizer
from nltk.sentiment import SentimentIntensityAnalyzer 

text = "We develop a valuation model for venture capital--backed companies and apply it to 135 US unicorns, that is, private companies with reported valuations above $1 billion. We value unicorns using financial terms from legal filings and find that reported unicorn post--money valuations average 48% above fair value, with 14 being more than 100% above. Reported valuations assume that all shares are as valuable as the most recently issued preferred shares. We calculate values for each share class, which yields lower valuations because most unicorns gave recent investors major protections such as initial public offering (IPO) return guarantees (15%), vetoes over down-IPOs (24%), or seniority to all other investors (30%). Common shares lack all such protections and are 56% overvalued. After adjusting for these valuation-inflating terms, almost one-half (65 out of 135) of unicorns lose their unicorn status."""
#text= """We develop a valuation model for venture capital--backed companies and apply it to 135 US unicorns, that is, private companies with reported valuations above $1 billion. We value unicorns using financial terms from legal filings and find that reported unicorn post--money valuations average 48% above fair value, with 14 being more than 100% above. Reported valuations assume that all shares are as valuable as the most recently issued preferred shares. We calculate values for each share class, which yields lower valuations because most unicorns gave recent investors major protections such as initial public offering (IPO) return guarantees (15%), vetoes over down-IPOs (24%), or seniority to all other investors (30%). Common shares lack all such protections and are 56% overvalued. After adjusting for these valuation-inflating terms, almost one-half (65 out of 135) of unicorns lose their unicorn status."""
demoWords = ["playing","happiness","going","doing", "coding", "programming","program","go","do","code"]

#lemmatizer=WordNetLemmatizer()
#WordNetLemmatizer=WordNetLemmatizer()
#stemmer = PorterStemmer()
#word={}
#for word in demoWords:
#    print(word,stemmer.stem(word),lemmatizer.lemmatize(word,"v"))

sia = SentimentIntensityAnalyzer()
print("statement 1",sia.polarity_scores("Programming is fun"))
print("statement 2",sia.polarity_scores("You behave very bad today"))
print("statement 3",sia.polarity_scores(text))