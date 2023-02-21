def suf():
    suffixes = {
        1: ["ो", "े", "ू", "ु", "ी", "ि", "ा"],
        2: ["कर", "ाओ", "िए", "ाई", "ाए", "ने", "नी", "ना", "ते", "ीं", "ती", "ता", "ाँ", "ां", "ों", "ें"],
        3: ["ाकर", "ाइए", "ाईं", "ाया", "ेगी", "ेगा", "ोगी", "ोगे", "ाने", "ाना", "ाते", "ाती", "ाता", "तीं", "ाओं", "ाएं", "ुओं", "ुएं", "ुआं"],
        4: ["ाएगी", "ाएगा", "ाओगी", "ाओगे", "एंगी", "ेंगी", "एंगे", "ेंगे", "ूंगी", "ूंगा", "ातीं", "नाओं", "नाएं", "ताओं", "ताएं", "ियाँ", "ियों", "ियां"],
        5: ["ाएंगी", "ाएंगे", "ाऊंगी", "ाऊंगा", "ाइयाँ", "ाइयों", "ाइयां"],
    }

    def hi_stem(word):
        for L in 5, 4, 3, 2, 1:
            if len(word) > L + 1:
                for suf in suffixes[L]:
                    if word.endswith(suf):
                        return word[:-L]
        return word

    if __name__ == '__main__':
        import sys
        if len(sys.argv) != 1:
            sys.exit('{} takes no arguments'.format(sys.argv[0]))
        for line in sys.stdin:
            print(*[hi_stem(word) for word in line.split()])




def getData():
    filename = input("Please enter the name of file: ")
    readfile = open(filename, "r")

    for line in readfile:
        word = line.split(" ")
        words= [x[:-1] for x in word]
        print(words)
        
        for text in words:
            pos=text.split('/')
            
            if pos[1]== "NN":

                if pos[1]== "NST":

                    if pos[1]== "NNP":

                        if pos[1]== "PRP":

                            if pos[1]== "DEM":

                                if pos[1]== "VM":

                                    if pos[1]== "VAUX":

                                        if pos[1]== "JJ":

                                            if pos[1]== "RB":
            

                                                if pos[1]== "PSP":

                                                    if pos[1]== "RP":

                                                        if pos[1]== "QF":

                                                            if pos[1]== "CC":

                                                                if pos[1]== "WQ":

                                                                    if pos[1]== "QO":

                                                                        if pos[1]== "INTF":

                                                                            if pos[1]== "INJ":

                                                                                if pos[1]== "NEG":

                                                                                    if pos[1]== "SYM":

                                                                                        if pos[1]== "XC":

                                                                                            if pos[1]== "RDP":

                                                                                                if pos[1]== "ECH":

                                                                                                    if pos[1]== "UNK":
            
                                                                                                        getData()
