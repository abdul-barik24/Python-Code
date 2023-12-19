#Abstract Class & Methods in Python
from abc import ABC, abstractmethod
class food(ABC):
    @abstractmethod
    def tasty(self):
        pass
    
    def info(self):
        print(f'Name: {self.name} \nPrice: {self.price} Tk, \nSize: {self.size} inches!')

#subclass
class pizza(food):
    def __init__(self, name, size, price):
        self.name = name
        self.size = size
        self.price = price

    def tasty(self):            #the method is overriden
        print(f'The {self.name} pizza is very delicious!')


p1 = pizza('King', '6', 750)

p1.info()
p1.tasty()
