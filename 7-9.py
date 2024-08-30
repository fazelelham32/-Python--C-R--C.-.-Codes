
# Created by Hamidreza Talebi



def main():
    print("This py file")
    for i in testfunc(5,25,3):
        print(i, end=' ')
        
def testfunc(*kw):
    num=len(kw)
    if num<1: raise TypeError('Require one argument')
    elif num==1:
        stop=kw[0]
        start=0
    elif num==2:
        (start,stop)=kw
        step=1
    elif num==3:
        (start,stop,step)=kw
    else:raise TypeError('Inclusive expected at most 3 arguments, got'.format(num))    
    i=start
    while i<=stop:
        yield i
        i+=step
    
if __name__ == "__main__": main()






