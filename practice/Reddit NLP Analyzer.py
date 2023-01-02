from pprint import pprint
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import requests
import praw
import nltk


headlines= pd.read_csv('headlines.csv')


nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA



sia= SIA()
results =[]
for line in headlines:
    pol_score =sia.polarity_scores(line)
    pol_score['headline']=line
    results.append(pol_score)

pprint(results[:3],width=100)
