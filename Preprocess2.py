import glob
import pickle
import os

def read_files():
    tweets = []
    lens = []

    if 'lens.pickle' not in os.listdir('.'):
        for file in glob.glob('Health-Tweets/**'):
            with open(file, 'r', encoding='utf-8', errors='ignore') as f:
                print(file)
                lines = f.readlines()

                for line in lines:
                    tweet = ''.join(line.split('|')[2:]).strip().lower().split(' ')
                    tweets.append(tweet)
                    lens.append(len(tweet))

        with open('tweets.pickle', 'wb') as handle:
            pickle.dump(tweets, handle)
        with open('lens.pickle', 'wb') as handle:
            pickle.dump(lens, handle)
    else:

        with open('tweets.pickle', 'rb') as handle:
            tweets = pickle.load(handle)
        with open('lens.pickle', 'rb') as handle:
            lens = pickle.load(handle)
  
    return tweets, lens

read_files()

