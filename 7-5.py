
# Created by Hamidreza Talebi



def main():
    testfunc(one=1, two=2, four=4)
def testfunc(**kw):
    print("This is a test function", kw['one'],kw['two'],kw['four'],kw['two'])
if __name__ == "__main__": main()





