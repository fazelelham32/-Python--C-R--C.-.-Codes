import os
import pickle
import random

directory = os.path.dirname(__file__)
def simple_learner(tweets, lens):
    pos_dict = {}
    if '/pos_dict.pickle' not in os.listdir(directory):
    
        if len(lens) > 0:
            max_len = max(lens)
        else:
            max_len = 0

        for index in range(max_len):
            pos_dict[index] = {}

        for tweet in tweets:
            for i, word in enumerate(tweet):
                try:
                    pos_dict[i][tweet[i]] += 1
                except KeyError:
                    pos_dict[i][tweet[i]] = 1
                except IndexError:
                    break
                
        with open(directory + '/pos_dict.pickle', 'wb') as handle:
            pickle.dump(pos_dict, handle)

    else:
        with open(directory + '/pos_dict.pickle', 'rb') as handle:
            pos_dict = pickle.load(handle)
  
    return pos_dict


def generate(text_number, pos_dict, lens):
    generated_texts = []
    
    if len(lens) > 0:
        min_len = min(lens)
    else:
        min_len = 0
    
    max_len = max(lens)
    if max_len < min_len:
        max_len = min_len
    
    for _ in range(text_number):
        text_len = random.randint(min_len, max_len)
        generated_text = ""
        for i in range(text_len):
            try:
                word_dict = pos_dict[i]
                word = random.choice(list(word_dict.keys()))
                generated_text += word + " "
            except KeyError:
                continue
        generated_texts.append(generated_text.strip())
        
    return generated_texts
