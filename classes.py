# Create class
class User:
    # Constructor
    def __init__(self, first, last):
        self.first = first
        self.last = last

    def introduce(self):
        return f'My name is {self.first} {self.last}'

# Init user obj
jake = User('Jake', 'Ike')

# Extend class
class Customer(User):
    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.balance = 0
    
    def setBalance(self, amount):
        self.balance = self.balance + amount

sara = Customer("Sara", "Ike")