
# Created by Hamidreza Talebi

class inclusive_range:
    def __init__(self,*args):
        numargs=len(args)
        if numargs<1:raise TypeError('require at least one argument')
        elif numargs==1:
            self.stop=args[0]
            self.start=1
            self.step=1
        elif numargs==2:
            (self.start,self.stop)=args
            self.step=1
        elif numargs==3:
            (self.start,self.stop,self.step)=args
        else:raise TypeError('at least 3 arguments')
            
    def __iter__(self):
        i=self.start
        while i<=self.stop:
            yield i
            i+=self.step
            

def main():
    o=inclusive_range(2,25,7)
    for i in o:print(i, end= ' ')
    
if __name__ == "__main__": main()







