from proj5.Counting2 import *
from proj5.Preprocess3 import *
from proj5.GenerateText2 import *

text_number = input('write the number of texts you want: ')
tw, l = read_preprocess_files()
pd = simple_learner(tw, l)

print(generate(int(text_number), pd, l))
