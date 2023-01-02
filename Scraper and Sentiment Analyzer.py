
import nltk
from pprint import pprint
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import requests
from IPython import display
import praw
from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA
nltk.download('vader_lexicon')


#what is my project. Im going to create a tracker that tells me the most controversial topics in real time
reddit = praw.Reddit (
    client_id="x6kDfhzIfzBSEH9nhGf-Hw",
    client_secret="krBRoDQYgOYkHITZDGM41PYMHqlMwg",
     user_agent="Scraper 1.0 by /u/WillCCUBC" )

sns.set(style='darkgrid',context='talk',palette="Dark2")

headlines = set()
set_of_comments=set()
counter=0
comment_counter=0
for submission in reddit.subreddit('poltics').hot(limit=4):
    if 1641024000 <submission.created_utc<1672560000  :
        counter=counter+1
        headlines.add(submission.title)
        #headlines.add(submission.selftext)
    #for comment in submission.comments:
        #comment_counter=comment_counter+1
        #print(comment_counter)
        #print(comment.body.encode("utf-8", errors='ignore'))
        #headlines.add(comment.body.encode(errors='ignore'))
print("total posts:",counter)      
#df = pd.DataFrame(headlines)
#df.to_csv('headlines.csv',header=False,index=False)
#df.to_csv('headlines.txt',header=False,encoding='utf-8',index=False)
#df = pd.DataFrame(set_of_comments)
#df.to_csv('comments.txt',header=False,encoding='utf-8',index=False)






sia= SIA()
results =[]
for line in headlines:
    scores =sia.polarity_scores(line)
    scores['headline']=line
    results.append(scores)

#pprint(results[:3],width=100)
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
