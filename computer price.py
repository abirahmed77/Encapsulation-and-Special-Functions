class Computer:
    
    def __init__(self):
        self.__maxPrice = 900
        
    def prinPrice(self):
        print(f"Selling Price : {self.__maxPrice}")
        
    def setMaxPrice(self, price):
        self.__maxPrice = price
        
c = Computer()
c.prinPrice()

c.__maxPrice = 1500
c.prinPrice()

c.setMaxPrice(2500)
c.prinPrice()