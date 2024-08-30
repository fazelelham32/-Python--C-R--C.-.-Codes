
# Created by Hamidreza Talebi

class Duck():
    
    def __init__(self,**kw):
        self.varaibles=kw
        
    def set_varaible(self,k,v):
        self.varaibles[k]=v
        
    def get_varaible(self,k):
        return self.varaibles.get(k,None)
    
def main():
    donald=Duck(feet=2)
    print(donald.get_varaible('feet'))
    
if __name__ == "__main__": main()






