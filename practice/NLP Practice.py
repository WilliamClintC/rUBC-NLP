import nltk
nltk.download('stopwords')


text= """We develop a valuation model for venture capital--backed companies and apply it to 135 US unicorns, that is, private companies with reported valuations above $1 billion. We value unicorns using financial terms from legal filings and find that reported unicorn post--money valuations average 48% above fair value, with 14 being more than 100% above. Reported valuations assume that all shares are as valuable as the most recently issued preferred shares. We calculate values for each share class, which yields lower valuations because most unicorns gave recent investors major protections such as initial public offering (IPO) return guarantees (15%), vetoes over down-IPOs (24%), or seniority to all other investors (30%). Common shares lack all such protections and are 56% overvalued. After adjusting for these valuation-inflating terms, almost one-half (65 out of 135) of unicorns lose their unicorn status."""
demoWords = ["playing","happiness","going","doing"]

from nltk.corpus import stopwords
stop_words =stopwords.words('english')
print("step 1")

from nltk.tokenize import word_tokenize, sent_tokenize
tokenize_words = word_tokenize(text)
print("step 2")

tokenize_words_without_stop_words=[]
without_stop_words = []
for word in tokenize_words:
    if word not in stop_words:
        tokenize_words_without_stop_words.append(word)
print("These are the removed stop words",set(tokenize_words)-set(tokenize_words_without_stop_words))
print("all the important words are",set(tokenize_words_without_stop_words)-set(stop_words))

#from nltk.probability import FreqDist
#fd = FreqDist(tokenize_words_without_stop_words)
#fd.plot(30,cumulative=False)
#plt.show()

