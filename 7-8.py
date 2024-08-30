
# Created by Hamidreza Talebi



def main():
    print("This py file")
    for i in testfunc(0,25,1):
        print(i, end=' ')
        
def testfunc(start,stop,step):
    i=start
    while i<=stop:
        yield i
        i+=step
    
if __name__ == "__main__": main()






