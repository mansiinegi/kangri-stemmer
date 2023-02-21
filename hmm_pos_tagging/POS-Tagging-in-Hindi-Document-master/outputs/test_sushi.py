
suffixes = {
    1: ["ो", "े", "ू", "ु", "ी", "ि", "ा"],
    2: ["कर", "ाओ", "िए", "ाई", "ाए", "ने", "नी", "ना", "ते", "ीं", "ती", "ता", "ाँ", "ां", "ों", "ें"],
    3: ["ाकर", "ाइए", "ाईं", "ाया", "ेगी", "ेगा", "ोगी", "ोगे", "ाने", "ाना", "ाते", "ाती", "ाता", "तीं", "ाओं", "ाएं", "ुओं", "ुएं", "ुआं"],
    4: ["ाएगी", "ाएगा", "ाओगी", "ाओगे", "एंगी", "ेंगी", "एंगे", "ेंगे", "ूंगी", "ूंगा", "ातीं", "नाओं", "नाएं", "ताओं", "ताएं", "ियाँ", "ियों", "ियां"],
    5: ["ाएंगी", "ाएंगे", "ाऊंगी", "ाऊंगा", "ाइयाँ", "ाइयों", "ाइयां"],
}

def hi_stem(word):
    for L in 5, 4, 3, 2, 1:
        #print(word,len(word),L ,end=" ")
        if len(word) > L + 1:
            for suf in suffixes[L]:
                print(suf)
                if word.endswith(suf):
                    return word[:-L]
    return word





def getData():
    # filename = input("Please enter the name of file: ")
    
    readfile = open("hmmoutput.txt", "r", encoding='utf-8')

    for line in readfile:
        word = line.split(" ")
        words= [x[:-1] for x in word]
        print(words)
        
        for text in words:
            pos=text.split('/')
            print(hi_stem(pos[0]))
            
            # if pos[1]== pos[1]:
            #     print(hi_stem(pos[0]))

getData()






