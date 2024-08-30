
# Created by Hamidreza Talebi

class Dog():
    def talk(self):print("You can talk!")
    def walk(self):print("You can Walk!")
    def bark(self):print("Bark!")
    def fur(self):print("The dog has brown and white fur")
    
class Duck():
    def quack(self):print("Quaaaak!")
    def walk(self):print("I can Walk!")
    def bark(self):print("The duck can not bark!")
    def fur(self):print("The duck has feathers")
           
def main():
    donald=Duck()
    fido=Dog()
    
    in_the_forest(donald)
    in_the_pond(fido)
    
def in_the_forest(d):
    d.bark()
    d.fur()
def in_the_pond(b):
    b.bark()
    b.walk()
    
    
if __name__ == "__main__": main()






