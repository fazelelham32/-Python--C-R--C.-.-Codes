import glob

def read_files():
    tweets = []
    lens = []
    for file in glob.glob('Health-Tweets/**'):
        with open(file, 'r', encoding='utf-8', errors='ignore') as f:
            print(file)
            lines = f.readlines()
        
        for line in lines:
            tweet = ''.join(line.split('|')[2:]).strip().lower().split(' ')
            tweets.append(tweet)
            lens.append(len(tweet))
        
    return tweets, lens

read_files()
