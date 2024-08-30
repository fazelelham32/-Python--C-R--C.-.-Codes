
def main():
    message = 'GUVF VF ZL FRPERG ZRFFNTR.'
    LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    # loop through every possible key
    for key in range(len(LETTERS)):
        translated = ''
        for symbol in message:
            if symbol in LETTERS:
                num = LETTERS.find(symbol) # get the number of the symbol
                num = num - key
                if num < 0:
                    num = num + len(LETTERS)
                    translated = translated + LETTERS[num]
                else:
                    # just add the symbol without encrypting/decrypting
                    translated = translated + symbol
                    # display the current key being tested, along with its decryption
                    print('Key #%s: %s' % (key, translated))

    
if __name__ == "__main__": main()
