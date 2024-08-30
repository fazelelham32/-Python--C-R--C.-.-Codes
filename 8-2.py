
# Created by Hamidreza Talebi

class Duck():
    
    def __init__(self,value):
        self._v=value
    
    def quack(self):
        print("1-This is test",self._v)
    
    def walk(self):
        print("2-This is test ", self._v)
    
def main():
    donald=Duck(113)
    donald.quack()
    donald.walk()
    
if __name__ == "__main__": main()






