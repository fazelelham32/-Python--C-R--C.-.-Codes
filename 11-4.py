
# Created by Hamidreza Talebi  

def main():
    buffersize=50000
    infile=open('bigfile.txt', 'r')
    outfile=open('new.txt', 'w')
    buffer=infile.read(buffersize)
    
    while len(buffer):
        outfile.write(buffer)
        buffer=infile.read(buffersize)
    print('Done')
if __name__ == "__main__": main()







