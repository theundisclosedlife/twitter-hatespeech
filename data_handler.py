import json
import pdb
import codecs
import pdb
import pandas as pd

def get_data():
    tweets = []
    df=pd.read_csv("Untitled.csv")
    df = df.drop(["Unnamed: 0"], axis=1)
    df['polarity'] = (df['Code']=="H").astype(int)
   
    for i in range(0,len(df['Tweet']):
        tweets.append({'text' : df['Tweet'][i].lower(),
                       'label': df['polarity'][i]
                      })
        
               

    #pdb.set_trace()
    return tweets


if __name__=="__main__":
    tweets = get_data()
    
    pdb.set_trace()
