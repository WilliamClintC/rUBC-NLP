from pprint import pprint
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import requests
import praw


#what is my project. Im going to create a tracker that tells me the most controversial topics in real time


#time.to_csv('time.csv',header=False,encoding='utf-8',index=False)
df = pd.read_csv('headlines.csv')
headlines="".join(df['title'])

import nltk

nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA



sia= SIA()
results =[]
for line in headlines:
    pol_score =sia.polarity_scores(line)
    pol_score['headline']=line
    results.append(pol_score)

pprint(results[:3],width=100)

df=pd.DataFrame.from_records(results)
df.head()

df.to_csv('results.csv',header=False,encoding='utf-8',index=False)

df['label']=0
df.loc[df['compound']>0.2,'label']=1
df.loc[df['compound']<-0.2,'label']=-1
df.head()

df.to_csv('After_Label_results.csv',header=False,encoding='utf-8',index=False)

df2=df[['headline','label']]
df2.to_csv('reddit_headlines_labels.csv',encoding='utf-8',index=False)

temp=df.label.value_counts(normalize=True)*100
temp.to_csv('Temp_results.csv',header=False,encoding='utf-8',index=False)

fig, ax=plt.subplots(figsize=(8,8))
counts=df.label.value_counts(normalize=True)*100
sns.barplot(x=counts.index, y=counts, ax=ax)

ax.set_xticklabels(['Negative','Neutral','Positive'])
ax.set_ylabel("Percentage")

plt.show()

