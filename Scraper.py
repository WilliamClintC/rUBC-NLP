import pandas as pd
import numpy as np
import praw
import time

#what is my project. Im going to create a tracker that tells me the most controversial topics in real time
reddit = praw.Reddit (
    client_id="x6kDfhzIfzBSEH9nhGf-Hw",
    client_secret="krBRoDQYgOYkHITZDGM41PYMHqlMwg",
     user_agent="Scraper 1.0 by /u/WillCCUBC" )

headlines = set()
set_of_comments=set()
counter=0
comment_counter=0
for submission in reddit.subreddit('UBC').controversial(limit=None):
    if 1641024000 <submission.created_utc<1672560000  :
        counter=counter+1
        headlines.add(submission.title)
        headlines.add(submission.selftext)
    for comment in submission.comments:
        comment_counter=comment_counter+1
        print(comment_counter)
        #print(comment.body.encode("utf-8", errors='ignore'))
        headlines.add(comment.body.encode(errors='ignore'))
print("total posts:",counter)      
df = pd.DataFrame(headlines)
df.to_csv('headlines.csv',header=False,index=False)
#df.to_csv('headlines.txt',header=False,encoding='utf-8',index=False)
#df = pd.DataFrame(set_of_comments)
#df.to_csv('comments.txt',header=False,encoding='utf-8',index=False)