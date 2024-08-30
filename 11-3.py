
# Created by Hamidreza Talebi  

def main():
    infile=open('lines.txt', 'r')
    outfile=open('new.txt', 'w')
    for line in infile:
        print(line, file=outfile ,end=' ')
    print('Done')
if __name__ == "__main__": main()







