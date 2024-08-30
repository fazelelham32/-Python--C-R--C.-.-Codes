
# Created by Hamidreza Talebi

class Duck:
    def __init__(self,**kwargs):
        self.properties=kwargs
        
    @property
    def color(self):
        return self.properties.get('color', None)
    @color.setter
    def color(self,c):
        self.properties['color']=c
    @color.deleter
    def color(self):
        del self.properties['color']

def main():
    donald=Duck()
    donald.color='blue'
    print(donald.color)
    
if __name__ == "__main__": main()







