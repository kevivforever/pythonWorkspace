import exceptions

class Dog:
    __secret = 2
    

def main():
    #raise Exception('JustDisagreeable')
    for i in dir(exceptions):
        print i

    try:
        zeroDivision = notHere/0
    except (NameError,ZeroDivisionError), e:
        print "You can't divide by zero"
        print e
    else:
        print zeroDivision
        print "This only occurs if exceptions are raised"
    finally:
        print "This will always occur"

if __name__ == '__main__': main()
