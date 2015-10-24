def main():
    name = raw_input("Hello. What is your name? ")
    print "Hi, %s" % name,
    age = int(raw_input("How old are you? "))
    print ("Did you know that in five years you will be %s years old?" % str(age+5))
    print ("And five years ago you were %s! Imagine that!" % str(age-5))

if __name__ == '__main__': main()
