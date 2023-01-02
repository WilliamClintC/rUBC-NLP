import pandas as pd
import numpy as np
import nltk

# Open the TXT file in read mode
with open('headlines.txt', 'r',encoding='utf-8') as file:
    # Read the contents of the file into a string
    contents = file.read()



from nltk.tokenize import RegexpTokenizer
tokenizer = RegexpTokenizer(r'\w+')
tokenized=tokenizer.tokenize(contents)

from nltk import word_tokenize
text = tokenized
tagged = nltk.pos_tag(text)
#print(tagged)
df = pd.DataFrame(tagged)
df.to_csv('tagged.csv',header=False,encoding='utf-8',index=False)
want = [w[0] for w in tagged if w[1]!='"'and w[1]!='.'and w[1]!='POS'and w[1]!='DT'and w[1]!='WP'and w[1]!='TO'and w[1]!='RB'and w[1]!='VBZ'and w[1]!='IN' and w[1]!='PRP'
        and w[1]!='VBG' and w[1]!='VB'and w[1]!='RBR'and w[1]!='CD'and w[1]!='VBP'and w[1]!='JJR'and w[1]!='JJ'and w[1]!='VBD'and w[1]!='EX'and w[1]!='MD'
        and w[1]!='JJS'and w[1]!='PRP$'and w[1]!='WRB']

filtered_sentence=[]
for w in want:
    if w == "Year" :
        filtered_sentence.append("year")
    if w == "Campus" :
        filtered_sentence.append("campus")
    if w == "Fall" :
        filtered_sentence.append("fall")
    if w == "Science" :
        filtered_sentence.append("science")
    if w == "How" :
        filtered_sentence.append("how")
    if w == "Help" :
        filtered_sentence.append("help")
    if w == "Vancouver" :
        filtered_sentence.append("vancouver")
    if w == "Please" :
        filtered_sentence.append("please")
    if w == "Black" :
        filtered_sentence.append("black")
    if w == "Academic" :
        filtered_sentence.append("academic")
    if w == "First" :
        filtered_sentence.append("first")
    if w == "Online" :
        filtered_sentence.append("online")
    if w == "International" :
        filtered_sentence.append("international")
    if w == "science" :
        filtered_sentence.append("science")
    if w == "Science" :
        filtered_sentence.append("science")
    if w == "Canadian" :
        filtered_sentence.append("canadian")
    if w == "indigenous" : 
        filtered_sentence.append("Indigenous")
    if w == "covid" :
        filtered_sentence.append("COVID")
    if w == "China" :
        filtered_sentence.append("china")

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
example_sent = want
stop_words = set(stopwords.words('english')+["UBC","students","student","I","Students","Why","people","Year","Campus","person","school","Anyone",
                    "go","Fall","SCIENCE","Help","How","Vancouver","Please","Black","Academic","First","A","Online","think","Internatinoal","science","Just","Canadian"
                    ,"indigenous","covid","Are","Do","Does","know","would","could","x200b","b","n","But","nI","nl","China","lot","someone","things","something"
                    , "post","everyone","thing","anything","anyone","point","others","And","place","question","part","My","reason","fact","bit","OP","problem","r","etc"
                    ,"idea","opinion","reddit","case","No","way" ])

for w in example_sent:
    if w not in stop_words :
        filtered_sentence.append(w)

 
#stop words filtered



import matplotlib.pyplot as plot
from nltk.probability import FreqDist
fd = FreqDist(filtered_sentence)
fd.plot(20,title="Most common words found in r/UBC's most controversial in 2022 ",cumulative=False)

#print(fd.most_common(50))