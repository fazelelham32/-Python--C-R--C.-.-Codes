
import time, saytime
def main():
    t = time.localtime()
    print("Content-type: text/html\n")
    print(
    "In Phoenix, Arizona, it is now " + saytime.saytime_t(t).words() +
    time.strftime(', on %A, %d %B %Y.')
    )
if __name__ == "__main__": main()



