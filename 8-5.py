
# Created by Hamidreza Talebi

class animal():
    def talk(self):print("You can talk!")
    def walk(self):print("You can Walk!")
    
class Duck(animal):
    def quack(self):print("Quaaaak!")
    def walk(self):print("I can Walk!")       
def main():
    donald=Duck()
    donald.talk()
    donald.walk()
    
if __name__ == "__main__": main()


