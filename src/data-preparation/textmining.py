import pandas as pd
from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import os
import time

data = pd.read_csv('../../gen/data-preparation/temp/parsed-data.csv', sep = '\t',encoding = 'utf-16')
data.head()
analyser = SentimentIntensityAnalyzer()
count =0

for i, j in data.iterrows():
    count +=1
    print(count)
    blob = TextBlob(j['text'])
    if data.loc[i,"lang"] != "en":
        try:
           blob = blob.translate(to='en')
        except:
                data.loc[i, 'negativity'] = 0
                data.loc[i, 'positivity'] = 0
                continue
    score = analyser.polarity_scores(blob)
   
    data.loc[i, 'negativity'] = score['neg']
    data.loc[i, 'positivity'] = score['pos']
    #try:
        #data.loc[i, 'polarity'] = blob.sentiment.polarity
        #data.loc[i, 'subjectivity'] = blob.sentiment.subjectivity
    #except:
        #data.loc[i, 'polarity'] = ''
        #data.loc[i, 'subjectivity'] = ''
    
#     data.loc[i, 'negativity'] = ''
  #   data.loc[i, 'positivity'] = ''

data.head()

os.makedirs('../../gen/data-preparation/output/', exist_ok=True)

data.to_csv('../../gen/data-preparation/output/dataset.csv', index = False, sep = '\t', encoding = 'utf-8')

print('done.')

