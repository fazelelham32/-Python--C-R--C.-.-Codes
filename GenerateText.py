import random
from Preprocess import *
from Counting import *
def generate(tweets_num,pos_dict,lens):
    for num in range(tweets_num):
        generated_text=''
        text_len= random.randint(min(lens), max(lens))
        for index in range(text_len):
            words= list(pos_dict[index].keys())
            freqs= list(pos_dict[index].values())
            selected_word= random.choices(words,freqs)[0]
            generated_text=generated_text+selected_word+' '

        with open('generatedText.txt','a+') as f:
            f.write(generated_text+'\n')

    
tw, l = read_preprocess_files()
pd= simple_learner(tw,l)
generate(50,pd,l)

        
