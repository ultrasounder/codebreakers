# class Circle:

#     def __init__(self, center, radius):
#         if radius < 0:
#             raise ValueError('Negative radius')
#         self.radius = radius
#         self. center = center

#     def get_radius(self):
#         return self.radius

#     def get_center(self):
#         return self.center
    
#     def get_area(self):
#         from math import pi
#         return pi * self.radius * self.radius

#     def get_circumference(self):
#         from math import pi
#         return 2 * pi * self.radius
    
#     def move(self, pt):
#         self.center = pt

#     def grow(self):
#         self. radius += 1

#     def shrink(self):
#         if self.radius > 0:
#             self.radius -= 1


# c1 = Circle((2, 4), 5)
# c2 = Circle((4,5), 5)

# print(c1.get_center())
# print(c2.get_center())
# print(c1.get_area())
# print(c2.get_area())
# print(c1.get_circumference())
# print(c2.get_circumference())

class BankAccount:

    def __init__(self, number, name, balance):
        if balance < 0:
            raise ValueError('Negative initial balance')
        self.__account_number = number
        self.__name = name
        self.__balance = balance

    def id(self):
        """returns the account number of this bank account object."""
        return self.__account_number

    def deposit(self):
        """Add funds to the account. There is no limit to the size of the   deposit."""
        self.__balance += amount

    def withdraw(self, amount):
        """Remove funds from the account, if possible. Only complete the withdrawl sucessfuly
        if there are enough funds in the account to fulfill that transaction. return true
        if sucessul and return false otherwise"""
        result = False #default condition
        if self.__balance - amount >= 0:
            self.__balance -= amount
            result = True
        return False

    def __str__(self):
        """returns the string representation of the object"""
        return '[{:>5} {:<10} {:>7} ]'.format(self. __account_number, self.__name, self.__balance)


#Client code that uses the BankAccount class 

def open_database(filename, db):
    """Read the account information from a given file and store it
    in the given list"""
    with open(filename) as lines:
        for line in lines:
            line.strip()
            number, name, balance = line.split(",")
            db.append(BankAccount(int(number), name, int(balance)))

def print_database(db):
    for accnt in db:
        print(accnt)

def get_account(db, account_number):
    for accnt in db:
        if accnt.id() == account_number:
            return accnt
            
        
        
