## pirveli leqciis savarjishoebi

# # 1
# class Rectangle:
#
#     def __init__(self,width,length,color):
#         self.width = width
#         self.length = length
#         self.color = color
#
#     def __str__(self):
#         return f"perimeter of Rectangle  is {self.perimeter} \nArea of Rectangle is {self.area} "
#
#
#     @property
#     def perimeter(self):
#         return 2 * (self.length + self.width)
#
#     @property
#     def area(self):
#         return self.length * self.width
#
# obj1 = Rectangle(1, 5, 'blue')
# obj2 = Rectangle(3, 3, 'green')
# obj3 = Rectangle(3, 7, 'purple')
#
# print(str(obj1))



## 2
#
# class Car:
#
#     def __init__(self, color, model, makeYear, fuelType):
#         self.color = color
#         self.model = model
#         self.makeYear = makeYear
#         self.fuelType = fuelType
#
#
#     def __str__(self):
#         return f'{self.color}\n{self.model}\n{self.makeYear}\n{self.fuelType}'
#
#
# mercedes = Car('red', 'Mercedes', 2015, 'Gas')
# BMW = Car('Blue', 'BMW', 2013, 'Gas')
# Audi = Car('orange', 'Audi', 2009, 'Diesel')
#
#
# print(str(mercedes))


## 3
#
# class Dog:
#
#     def __init__(self, Breed, Size, Age, Color):
#         self.Breed = Breed
#         self.Size = Size
#         self.Age = Age
#         self.Color = Color
#
#     def __str__(self):
#         return f' Breed = {self.Breed}\n Size = {self.Size}\n Age = {self.Age} years\n Color = {self.Color}'
#
# Br1 = Dog('Maltese','Small', 2, 'white')
# print(str(Br1))

##4
# class Celsius:
#     def __init__(self):
#         self.__temperature = 0
#
#     def set_temp(self,temperature):
#         self.__temperature = temperature
#
#     def get_temp(self):
#         return self.__temperature
#
#     def del_temp(self):
#         del self.__temperature
#
#     temperature = property(get_temp, set_temp, del_temp)
#
# c1 = Celsius()
# c2 = Celsius()
#
# c1.temperature = 30
# c2.temperature = 39
#
# print(c1.temperature)
# print(c2.temperature)
#
# del c1.temperature


##5

# class Bank_Account:
#
#
#     def __init__(self, account_name):
#         self.__account_name = account_name
#         self.balance = 0
#
#     def set_name(self,account_name):
#         self.__account_name = account_name
#
#     def get_name(self):
#         return self.__account_name
#
#     def deposit(self, amount):
#         self.balance += amount
#         print(f'თანხის შეტანა შესრულებულია. ამჟამად თქვენს ანგარიშზე გაქვთ {self.balance} ლარი.')
#
#     def withdraw(self, money):
#         if money > self.balance:
#             print('თქვენს ანგარიშზე არ არის საკმარისი თანხა')
#         else:
#             self.balance -= money
#             print(f'თანხის გამოტანა შესრულებულია. ამჟამად თქვენს ანგარიშზე გაქვთ {self.balance} ლარი.')
#
#
# def main():
#     obj1 = Bank_Account('giorgi kakhtelidze')
#     balance = 100
#     while True:
#         print(f'ამჟამად თქვენ ანგარიშზე არის {balance} ლარი')
#         operacia = int(input('შეიტანე შესაბამისი კოდი რომელი ოპერაციის შესრულებაც გსურთ:\nთანხის შეტანა: 1, თანხის გამოტანა: 2.\nპასუხი: '))
#         if operacia == 1:
#             amount = int(input('რა თანხის შეტანა გსურთ?'))
#             obj1.deposit(amount)
#             break
#         elif operacia == 2:
#             money = int(input('რა თანხის გამოტანა გსურს? '))
#             obj1.withdraw(money)
#             break
#         else:
#             print('თქვენ შეიყვანეთ არასწორი კოდი. სცადეთ ახლიდან.\n')
#
# main()




## 6
# class Fraction:
#
#     def __init__(self, top, bottom):
#         self.top = top
#         self.bottom = bottom
#
#
#     def __str__(self):
#         return f'{self.top}/{self.bottom}'
#
#     def add(self,other):
#         new_top = self.top * other.bottom + other.top * self.bottom
#         new_bottom = self.bottom * other.bottom
#         return Fraction(new_top, new_bottom)
#
#     def inverse(self):
#         return f'{self.bottom}/{self.top}'
#
# obj1 = Fraction(3,7)
# obj2 = Fraction(2,8)
#
# print(str(obj1))
# print(obj2.inverse())


## 7
#
# class Point:
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def distance(self):
#         import math
#         z = self.x ** 2 + self.y ** 2
#         return math.sqrt(z)
#
# point1 = Point(3,5)
# point2 = Point(6,9)
#
# print(point1.distance())
# print(point2.distance())



## 8
# class Point:
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __str__(self):
#         return f'({self.x},{self.y})'
#
# ## d1 = x2-x1   d2 = y2 - y1
#
#     def distance(self,other):
#         import math
#         d1 = self.x - other.x
#         d2 = self.y - other.y
#
#         distance = math.sqrt(d1 ** 2 + d2 ** 2)
#         return distance
#
# a = Point(7,12)
# b = Point(2,4)
# print(str(a))
# print(str(b))
# distance = a.distance(b)
# print('Distance between point a and point b: ', distance)


## 9



import sqlite3

conn = sqlite3.connect('my_database.sqlite')
cursor = conn.cursor()





cursor.execute("INSERT INTO books (title, author, price) VALUES ('Hamlet', 'William Shakespeare', 10.5)")
conn.commit()

book_list = [

('The Book Thief', 'Markus Zusak', 17 ),
('Animal Farm', 'George Orwell', 13 ),
('The Hunger Games', 'Suzanne Collins', 17 ),
('Harry Potter and the Prisoner of Azkaban', 'Rowling', 25),
('Harry Potter and the Goblet of Fire', 'Rowling', 24 ),
('Macbeth', 'William Shakespeare', 29 )
]
cursor.executemany('INSERT INTO books (title, author, price) VALUES (?,?,?)', book_list)
conn.commit()



import sqlite3
sqliteConnection = sqlite3.connect('SOLite Python.db')
cursor = sqliteConnection.cursor()
sqlite_select_query = "*'SELECT * from SqliteDb_developers"""
cursor. execute(sqlite_select_query)
records = cursor. fetchall()
print("Total rows are:  ", len(records))