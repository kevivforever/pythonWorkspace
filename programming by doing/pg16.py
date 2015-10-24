def main():
    print "Hello. What is your name?"
    name = raw_input("> ")
    print
    print "Hi, %s! How old are you?" % name
    age = raw_input("> ")
    print
    print "So you're %s, eh?  That's not old at all!" % age
    print "How much do you make, %s?" %name
    earn = raw_input("> ")
    print
    print "%s!  I hope that's per hour and not per year! LOL!" % earn
    
if __name__ == '__main__': main()
