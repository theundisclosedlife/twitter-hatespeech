import json
import pdb
import codecs
import pdb
import pandas as pd

def get_data():
    tweets = []
    df=pd.read_csv("Untitled.csv")
    df = df.drop(["Unnamed: 0"], axis=1)
    df = df.drop_duplicates(subset ="Tweet", 
                     keep = False)
    df=df.reset_index(drop=True)
    
    def clean_text(text):
    
   
    
        text = re.sub(r"\A[A-Za-z][^ ]*", "", text)  

        text = re.sub(r"[^A-Za-z0-9^,!.\/'+-=]", " ", text)
        text = re.sub(r"what's", "what is ", text)
        text = re.sub(r"\'s", " ", text)
        text = re.sub(r"\'ve", " have ", text)
        text = re.sub(r"n't", " not ", text)
        text = re.sub(r"i'm", "i am ", text)
        text = re.sub(r"\'re", " are ", text)
        text = re.sub(r"\'d", " would ", text)
        text = re.sub(r"\'ll", " will ", text)
        text = re.sub(r",", " ", text)
        text = re.sub(r"\.", " ", text)
        text = re.sub(r"!", " ! ", text)
        text = re.sub(r"\/", " ", text)
        text = re.sub(r"\^", " ^ ", text)
        text = re.sub(r"\+", " + ", text)
        text = re.sub(r"\-", " - ", text)
        text = re.sub(r"\=", " = ", text)
        text = re.sub(r"'", " ", text)

    
    return text
# apply the above function to df['text']
    df['Tweet'] = df['Tweet'].map(lambda x: clean_text(x))
    
    
    
    df['polarity'] = (df['Code']=="H").astype(int)
   
    for i in range(0,len(df['Tweet'])):
        tweets.append({'text' : df['Tweet'][i].lower(),
                       'label': df['polarity'][i]
                      })
        
               

    #pdb.set_trace()
    return tweets


if __name__=="__main__":
    tweets = get_data()
    
    pdb.set_trace()
