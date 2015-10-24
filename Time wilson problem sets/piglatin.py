
def convert(orig_word):
    upperletter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    last = len(orig_word)-1
    pig_word = ""
    print last
    if orig_word[0] in upperletter:
        pig_word = orig_word[1].upper() + orig_word[2:]
        print "after uppercase: " + pig_word
    else:
        pig_word = orig_word[1:]
        
    if orig_word[last] in letters:
        pig_word = pig_word + orig_word[0] + "ay"
    else:
        pig_word = pig_word[1:last] + orig_word[0] + "ay" + pig_word[last]

    print "after retaining " + pig_word
    return pig_word
        
def main():
    
    word = raw_input("Enter a string: ")
    if word:
        pig_word = []
        word_list = word.split()
        for w in word_list:
            pig_word.append(convert(w))
        output = ' '.join(pig_word)
        print output
    else:
        main()
    
if __name__ == '__main__': main()
