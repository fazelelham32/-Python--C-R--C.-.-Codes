import random
import os

dir = os.path.dirname(__file__)

def generate(tweets_num, pos_dict, lens):
    all_generated_text = []
    
    if len(lens) > 0:
        min_len = min(lens)
        max_len = max(lens)
    else:
        min_len = 0
        max_len = 0
    
    for num in range(tweets_num):
        generated_text = ''
        text_len = random.randint(min_len, max_len)
        for index in range(text_len):
            if index in pos_dict:
                words = list(pos_dict[index].keys())
                freqs = list(pos_dict[index].values())
                selected_word = random.choices(words, freqs)[0]
                generated_text += selected_word + ' '
        
        all_generated_text.append(generated_text)
        with open(dir + '/generatedText.txt', 'a+') as f:
            f.write(generated_text + '\n')

    return all_generated_text

        
