

class Animal:

    __hungry = "Yes"
    __name = "No Name"
    __owner = "No Owner"
    
    def __init__(self):
        pass

    def set_owner(self, newOwner):
        self.__owner = newOwner
        return
    
    def get_owner(self):
        return self.__owner

    def set_name(self, newName):
        self.__name = newName
        return
    
    def get_name(self):
        return self.__name
    
    def noise(self):
        print('errr')
        self.__hiddenmethod()
        return

    def __hiddenmethod(self):
        print ("hard to find")
        return

def main():
    dog = Animal()
    dog.set_owner('Sue')
    print dog.get_owner()
    #print dog.__owner
    dog.noise()
    #dog.__hiddenmethod()


if __name__ == '__main__': main()
