class egg:
    def __init__(self, kind="fried"):
        self.kind=kind
    def whatkind(self):
        return self.kind
    

def main():
    fried=egg()
    scrambled=egg('scrambled')
    print(scrambled.whatkind())
   
if __name__ == "__main__": main()