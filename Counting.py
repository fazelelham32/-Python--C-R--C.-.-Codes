from Preprocess3 import read_preprocess_files
import os
import pickle

def simple_learner(tweets,lens):
    pos_dict={}
    if 'pos_dict.pickle' not in os.listdir('.'):
    
        for index in range(max(lens)):
            pos_dict[index]={}

        for tweet in tweets:
            for i,word in enumerate(tweet):
                try:
                    pos_dict[i][tweet[i]]+=1
                except KeyError:
                    pos_dict[i][tweet[i]]=1
                except IndexError:
                    break
                
        with open('pos_dict.pickle', 'wb') as handle:
            pickle.dump(pos_dict, handle)

    else:
        with open('pos_dict.pickle', 'rb') as handle:
            pos_dict = pickle.load(handle)
  
    return pos_dict

tw, l = read_preprocess_files()
result= simple_learner(tw,l)
