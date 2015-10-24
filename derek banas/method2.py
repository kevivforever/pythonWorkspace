
globalTen = 10

def createDict(**kvargs):
    for i in kvargs:
        print (i, kvargs[i])
    print (type(kvargs))
    return

def main():
    createDict(Name='Derek',Age=35,YearBorn=1974)
    createDict(Cust1=('Derek',35,1974),Cust2=('Sally',25,1984))
    
if __name__ == '__main__':main()
