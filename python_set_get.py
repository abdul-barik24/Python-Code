#Python Set & Get
class book:
    def __init__(self, name, author):
        self.name = name
        self.author = author
        self.price = 0

    def set_price(self, price):
        self.price = price

    def get_price(self):
        return self.price
    
    def details(self):
        print(f'The book\'s name is \"{self.name}\" \nthat\'s written by {self.author}. \nIt\'s price is {self.price} Taka only!')
    
book1 = book('Opekhha', 'Homayun Ahmed')
book1.set_price(150)

book1.details()