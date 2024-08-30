

def main():
    d=dict(five=5,two=2,three=3)
    for k in sorted(d.keys()):
        print(k,d[k])
if __name__ == "__main__": main()