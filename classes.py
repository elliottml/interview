# python 3.9.7

def main():
    ''' main loop '''

    # create a new set of class variables

    classvar1a = MyClass1()
    classvar1b = MyClass1()
    classvar2 = MyClass2()
    
    print("Entering main()")
    
    print("")
    
    print("Setting local values in classvar1a")
    classvar1a.setLocal("1alocal") #set a local value   
    print(classvar1a.getLocal())  #get the local value
    
    print("Setting local values in classvar1b")
    classvar1b.setLocal("1blocal") #set a local value   
    print(classvar1b.getLocal())  #get the local value
    
    print("Setting global value for classvar1x")
    classvar1a.setglobal("1xglobal") #set a global value   
    print(classvar1a.getGlobal())  #get the global value
    print(classvar1b.getGlobal())   #and do it again
    
     print("Setting local values in classvar2")
    classvar2.setLocal("2local") #set a local value   
    print(classvar2.getLocal())  #get the local value
    
    print("Setting global value for classvar2")
    classvar2.setglobal("1xglobal") #set a global value   
    print(classvar2.getGlobal())  #get the global value

    
class MyClass1:
    ''' sample class 1 '''
    
    globalvar       #a public gloabl variable
    
    def __init__(self):
        self.__localvar

    def setLocal(self, value):
        self.__localvar = value        #a private local variable
    
    def setGlobal(self, value):
        globalVar = value
    
    def getLocal(self):
        return self.__localvar
    
    def getGlobal(self):
        return globalvar

class MyClass2(MyClass1):
    ''' sample class 2 derived from MyClass1 '''

if __name__ == "__main"
    main()