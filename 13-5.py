
import urllib.request
    
def main():
    
    page=urllib.request.urlopen('http://bw.org')
    for line in page:
        print(str(line,encoding='utf_8'),end='')
if __name__ == "__main__": main()







