
globalTen = 10
globaltwenty = 20

def addNumbers1(num1=1,num2=1):
    return num1 + num2

def addNumbers2(*args):
    print "value of global ten is %d" % globalTen
    #cant change the global variable value directly
    #globalTen = 15
    finalValue = 0

    if args:
        for i in args:
            finalValue += i
        return finalValue
    else:
        return "Please provide numbers"

def changeGlobal():
    global globalTen
    globalTen = 15
    globals()['globaltwenty'] = 21
    
def main():
    print addNumbers1()
    print addNumbers2()
    print addNumbers2(10,20,30,40,50)
    print "value of global ten is %d" % globalTen
    changeGlobal()
    print globalTen
    print globaltwenty

if __name__ == '__main__':main()
