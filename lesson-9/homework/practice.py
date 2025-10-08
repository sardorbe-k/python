# 1. Write a Python program to create a class representing a Circle. Include methods to calculate its area and perimeter.


import math  

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius


r = float(input("Aylana radiusini kiriting: "))
circle = Circle(r)

print(f"Aylananing yuzi: {circle.area():.2f}")
print(f"Aylananing perimetri: {circle.perimeter():.2f}")

# 2. Write a Python program to create a Person class. Include attributes like name, country, and date of birth. Implement a method to determine the person's age.

from datetime import date  

class Person:
    def __init__(self, name, country, birth_year):
        self.name = name
        self.country = country
        self.birth_year = birth_year

    def age(self):
        current_year = date.today().year
        return current_year - self.birth_year


name = input("Ismni kiriting: ")
country = input("Mamlakatni kiriting: ")
birth_year = int(input("Tug‘ilgan yilingizni kiriting: "))

person = Person(name, country, birth_year)

print(f"\nIsm: {person.name}")
print(f"Mamlakat: {person.country}")
print(f"Yosh: {person.age()} yosh")

# 3. Write a Python program to create a Calculator class. Include methods for basic arithmetic operations.

class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Xato! Nolga bo‘lish mumkin emas."
        return a / b


calc = Calculator()

a = float(input("Birinchi sonni kiriting: "))
b = float(input("Ikkinchi sonni kiriting: "))

print("Qo‘shish:", calc.add(a, b))
print("Ayirish:", calc.subtract(a, b))
print("Ko‘paytirish:", calc.multiply(a, b))
print("Bo‘lish:", calc.divide(a, b))


# 4. Write a Python program to create a class that represents a shape. Include methods to calculate its area and perimeter. Implement subclasses for different shapes like Circle, Triangle, and Square.

import math

class Shape:
    def area(self):
        return 0

    def perimeter(self):
        return 0


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return 4 * self.side


class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))


circle = Circle(5)
square = Square(4)
triangle = Triangle(3, 4, 5)

print("Aylana maydoni:", circle.area())
print("Aylana perimetri:", circle.perimeter())

print("Kvadrat maydoni:", square.area())
print("Kvadrat perimetri:", square.perimeter())

print("Uchburchak maydoni:", triangle.area())
print("Uchburchak perimetri:", triangle.perimeter())


# 5. Write a Python program to create a class representing a binary search tree. Include methods for inserting and searching for elements in the binary tree.

class BinarySearchTree:
    def __init__(self):
        self.tree = []  

    def insert(self, value):
        if value not in self.tree:
            self.tree.append(value)
            self.tree.sort()  
        else:
            print(f"{value} allaqachon mavjud!")

    def search(self, value):
        return value in self.tree


bst = BinarySearchTree()
bst.insert(10)
bst.insert(5)
bst.insert(15)
bst.insert(7)

print("Daraxt:", bst.tree)
print("7 mavjudmi?", bst.search(7))  
print("20 mavjudmi?", bst.search(20)) 

# 6.Write a Python program to create a class representing a stack data structure. Include methods for pushing and popping elements.

class Stack:
    def __init__(self):
        self.items = [] 

    def push(self, item):
        self.items.append(item)
        print(f"{item} stack'ga qo‘shildi.")

    def pop(self):
        if not self.is_empty():
            removed = self.items.pop()
            print(f"{removed} stack'dan olib tashlandi.")
            return removed
        else:
            print("Stack bo‘sh, olib tashlab bo‘lmaydi!")

    def is_empty(self):
        return len(self.items) == 0

    def display(self):
        print("Hozirgi stack:", self.items)


stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)

stack.display()

stack.pop()
stack.display()

stack.pop()
stack.pop()
stack.pop()  


# 7. Write a Python program to create a class representing a stack data structure. Include methods for pushing and popping elements.

class Node:
    def __init__(self, data):
        self.data = data      
        self.next = None      

class LinkedList:
    def __init__(self):
        self.head = None      

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:         
            self.head = new_node
        else:
            current = self.head
            while current.next:       
                current = current.next
            current.next = new_node
        print(f"{data} qo‘shildi.")

    def delete(self, key):
        current = self.head

        if current and current.data == key:
            self.head = current.next
            print(f"{key} o‘chirildi.")
            return

        prev = None
        while current and current.data != key:
            prev = current
            current = current.next

        if current is None:
            print(f"{key} topilmadi.")
            return

        prev.next = current.next
        print(f"{key} o‘chirildi.")

    def display(self):
        current = self.head
        if current is None:
            print("Ro‘yxat bo‘sh.")
            return
        print("Linked List tarkibi:", end=" ")
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


ll = LinkedList()
ll.insert(10)
ll.insert(20)
ll.insert(30)
ll.display()

ll.delete(20)
ll.display()

ll.delete(40)  

# 8. Write a Python program to create a class representing a shopping cart. Include methods for adding and removing items, and calculating the total price.

class ShoppingCart:
    def __init__(self):
        self.items = {} 

    def add_item(self, name, price):
        self.items[name] = price
        print(f"{name} savatchaga {price} so‘m bilan qo‘shildi.")

    def remove_item(self, name):
        if name in self.items:
            del self.items[name]
            print(f"{name} savatchadan olib tashlandi.")
        else:
            print(f"{name} savatchada yo‘q.")

    def total_price(self):
        total = sum(self.items.values())
        return total

    def show_cart(self):
        if not self.items:
            print("Savatcha bo‘sh.")
        else:
            print("Savatchadagi mahsulotlar:")
            for name, price in self.items.items():
                print(f"- {name}: {price} so‘m")
            print(f"Umumiy narx: {self.total_price()} so‘m")


cart = ShoppingCart()
cart.add_item("Olma", 5000)
cart.add_item("Banan", 7000)
cart.add_item("Sut", 8000)

cart.show_cart()

cart.remove_item("Banan")
cart.show_cart()

cart.remove_item("Non")  

# 9. Write a Python program to create a class representing a stack data structure. Include methods for pushing, popping, and displaying elements.

class Stack:
    def __init__(self):
        self.items = []  
    def push(self, item):
        self.items.append(item)
        print(f"{item} stack'ga qo‘shildi.")

    def pop(self):
        if not self.is_empty():
            removed = self.items.pop()
            print(f"{removed} stack'dan olib tashlandi.")
            return removed
        else:
            print("Stack bo‘sh, olib tashlab bo‘lmaydi!")

    def display(self):
        if not self.items:
            print("Stack bo‘sh.")
        else:
            print("Stack tarkibi (pastdan yuqoriga):", self.items)

    def is_empty(self):
        return len(self.items) == 0


stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)

stack.display()  

stack.pop()
stack.display()

stack.pop()
stack.pop()
stack.pop()  

# 10.Write a Python program to create a class representing a queue data structure. Include methods for enqueueing and dequeueing elements.

class Queue:
    def __init__(self):
        self.items = []  

    def enqueue(self, item):
        self.items.append(item)
        print(f"{item} navbatga qo‘shildi.")

    def dequeue(self):
        if not self.is_empty():
            removed = self.items.pop(0) 
            print(f"{removed} navbatdan olib tashlandi.")
            return removed
        else:
            print("Navbat bo‘sh, olib tashlab bo‘lmaydi!")

    def display(self):
        if self.is_empty():
            print("Navbat bo‘sh.")
        else:
            print("Hozirgi navbat:", self.items)

    def is_empty(self):
        return len(self.items) == 0


queue = Queue()
queue.enqueue("Olma")
queue.enqueue("Banan")
queue.enqueue("Shaftoli")

queue.display()

queue.dequeue()
queue.display()

queue.dequeue()
queue.dequeue()
queue.dequeue() 

# 11. Write a Python program to create a class representing a bank. Include methods for managing customer accounts and transactions.

class Bank:
    def __init__(self):
        self.accounts = {}  
    def create_account(self, name, balance=0):
        self.accounts[name] = balance
        print(f"{name} uchun hisob ochildi. Boshlang‘ich balans: {balance} so‘m.")

    def deposit(self, name, amount):
        if name in self.accounts:
            self.accounts[name] += amount
            print(f"{name} hisobiga {amount} so‘m qo‘shildi. Yangi balans: {self.accounts[name]} so‘m.")
        else:
            print("Bunday mijoz topilmadi.")

    def withdraw(self, name, amount):
        if name in self.accounts:
            if self.accounts[name] >= amount:
                self.accounts[name] -= amount
                print(f"{name} hisobidan {amount} so‘m yechildi. Yangi balans: {self.accounts[name]} so‘m.")
            else:
                print("Balansda yetarli mablag‘ yo‘q.")
        else:
            print("Bunday mijoz topilmadi.")

    def show_balance(self, name):
        if name in self.accounts:
            print(f"{name} hisobidagi balans: {self.accounts[name]} so‘m.")
        else:
            print("Bunday mijoz topilmadi.")


bank = Bank()
bank.create_account("Ali", 50000)
bank.deposit("Ali", 20000)
bank.withdraw("Ali", 10000)
bank.show_balance("Ali")

