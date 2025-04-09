class SR:
    
    def __init__(self):
        self.__string = ""
        
    def takeInput(self):
        self.__string = input("Enter a String word : ")
        
    def RString(self):
        return self.__string[::-1]
    
obj = SR()
obj.takeInput()

print(f"The Reversed word : {obj.RString()}")