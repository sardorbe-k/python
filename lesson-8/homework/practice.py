# 1. Write a Python program to handle a ZeroDivisionError exception when dividing a number by zero.
def safe_divide(a, b):
    try:
        result = a / b
        print(f"Result: {result}")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed!")

safe_divide(10, 2)  
safe_divide(8, 0)   

# 2. Write a Python program that prompts the user to input an integer and raises a ValueError exception if the input is not a valid integer.

def get_integer():
    user_input = input("Iltimos, butun son kiriting: ")
    try:
        number = int(user_input)   
        print(f"Siz kiritgan son: {number}")
    except ValueError:
        raise ValueError("Xatolik: Siz butun son kiritmadingiz!")

get_integer()

# 3. Write a Python program that opens a file and handles a FileNotFoundError exception if the file does not exist.

def open_file(filename):
    try:
        with open(filename, "r") as f:
            content = f.read()
            print("File has been read successfully!\n")
            print(content)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found!")

open_file("data.txt")  

# 4. Write a Python program that prompts the user to input two numbers and raises a TypeError exception if the inputs are not numerical.

def get_two_numbers():
    x = input("Enter the first number: ")
    y = input("Enter the second number: ")
    
    try:
        num1 = float(x)  
        num2 = float(y)
        print(f"The numbers are: {num1} and {num2}")
    except ValueError:
        raise TypeError("Error: Both inputs must be numerical values!")

get_two_numbers()

# 5. Write a Python program that opens a file and handles a PermissionError exception if there is a permission issue.

try:
    with open("test.txt", "w") as file:
        file.write("Bu faylga yozish muvaffaqiyatli amalga oshdi!")
    print("Faylga yozish tugadi.")

except PermissionError:
    print("Xatolik: Sizda bu faylga yozish uchun ruxsat yo‘q!")

except Exception as e:
    print(f"Boshqa xatolik yuz berdi: {e}")

# 6. Write a Python program that executes an operation on a list and handles an IndexError exception if the index is out of range.

try:
    numbers = [5, 10, 15, 20, 25]

    index = int(input("Elementni olish uchun index kiriting: "))
    print("Tanlangan element:", numbers[index])

except IndexError:
    print("Xatolik: Siz kiritgan index ro'yxatdan tashqarida (Index out of range).")

except ValueError:
    print("Xatolik: Iltimos, faqat butun son kiriting.")

# 7. Write a Python program that prompts the user to input a number and handles a KeyboardInterrupt exception if the user cancels the input.

try:
    number = int(input("Son kiriting: "))
    print("Siz kiritgan son:", number)

except KeyboardInterrupt:
    print("\nXatolik: Siz kiritishni bekor qildingiz (KeyboardInterrupt).")

except ValueError:
    print("Xatolik: Iltimos, faqat butun son kiriting.")

# 8. Write a Python program that executes division and handles an ArithmeticError exception if there is an arithmetic error.

try:
    a = int(input("Birinchi sonni kiriting: "))
    b = int(input("Ikkinchi sonni kiriting: "))
    result = a / b
    print("Natija:", result)

except ArithmeticError:
    print("Xatolik: Arifmetik xato! Ehtimol 0 ga bo‘lishga urindingiz.")

# 9. Write a Python program that opens a file and handles a UnicodeDecodeError exception if there is an encoding issue.

try:
    with open("test.txt", "r", encoding="ascii") as file:
        content = file.read()
        print(content)

except UnicodeDecodeError:
    print("Xatolik: Faylni o‘qishda kodlash muammosi yuz berdi (UnicodeDecodeError).")

# 10. Write a Python program that executes a list operation and handles an AttributeError exception if the attribute does not exist.

try:
    my_list = [1, 2, 3, 4]
    my_list.split()

except AttributeError:
    print("Xatolik: Bu obyekt uchun bunday atribut yoki metod mavjud emas (AttributeError).")


# File Input/Output Exercises
# 1. Write a Python program to read an entire text file.

with open("sample.txt", "r") as file:
    content = file.read()
    print(content)

# 2. Write a Python program to read first n lines of a file.

n = int(input("Nechta qatordan o‘qilsin: "))
with open("sample.txt", "r") as file:
    for i in range(n):
        print(file.readline().strip())

# 3. Write a Python program to append text to a file and display the text.

text = input("Qo‘shmoqchi bo‘lgan matningizni kiriting: ")
with open("sample.txt", "a") as file:
    file.write("\n" + text)

with open("sample.txt", "r") as file:
    print(file.read())

# 4. Write a Python program to read last n lines of a file.

n = int(input("Nechta oxirgi qatordan o‘qilsin: "))
with open("sample.txt", "r") as file:
    lines = file.readlines()
    for line in lines[-n:]:
        print(line.strip())

# 5. Write a Python program to read a file line by line and store it into a list.

with open("sample.txt", "r") as file:
    lines = file.readlines()
print(lines)

# 6. Write a Python program to read a file line by line and store it into a variable.

with open("sample.txt", "r") as file:
    content = ""
    for line in file:
        content += line
print(content)

# 7. Write a Python program to read a file line by line and store it into an array.

import array

with open("sample.txt", "r") as file:
    arr = array.array('u', file.read())  # 'u' -> Unicode character array
print(arr)

# 8. Write a Python program to find the longest words.

with open("sample.txt", "r") as file:
    words = file.read().split()
    longest = max(words, key=len)
print("Eng uzun so‘z:", longest)

# 9. Write a Python program to count the number of lines in a text file.

with open("sample.txt", "r") as file:
    lines = file.readlines()
print("Qatorlar soni:", len(lines))

# 10. Write a Python program to count the frequency of words in a file.

from collections import Counter

with open("sample.txt", "r") as file:
    words = file.read().split()
    freq = Counter(words)
print(freq)

# 11. Write a Python program to get the file size of a plain file.

import os

size = os.path.getsize("sample.txt")
print("Fayl hajmi:", size, "bayt")

# 12. Write a Python program to write a list to a file.

fruits = ["apple", "banana", "cherry"]
with open("fruits.txt", "w") as file:
    for item in fruits:
        file.write(item + "\n")

# 13. Write a Python program to copy the contents of a file to another file.

with open("sample.txt", "r") as src, open("copy.txt", "w") as dest:
    dest.write(src.read())

# 14. Write a Python program to combine each line from the first file with the corresponding line in the second file.

with open("file1.txt") as f1, open("file2.txt") as f2:
    for line1, line2 in zip(f1, f2):
        print(line1.strip() + " " + line2.strip())

# 15. Write a Python program to read a random line from a file.

import random

with open("sample.txt", "r") as file:
    lines = file.readlines()
print("Tasodifiy qator:", random.choice(lines))

# 16. Write a Python program to assess if a file is closed or not.

file = open("sample.txt", "r")
print("Fayl ochilganmi?", not file.closed)
file.close()
print("Fayl yopildimi?", file.closed)

# 17. Write a Python program to remove newline characters from a file.

with open("sample.txt", "r") as file:
    lines = [line.strip() for line in file]

print(lines)

# 18. Write a Python program that takes a text file as input and returns the number of words in a given text file.

with open("sample.txt", "r") as file:
    text = file.read().replace(",", " ")
    words = text.split()
print("So‘zlar soni:", len(words))

# 19. Write a Python program to extract characters from various text files and put them into a list.

import glob

chars = []
for filename in glob.glob("*.txt"):
    with open(filename, "r") as file:
        chars.extend(list(file.read()))

print(chars)

# 20. Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt.

import string

for letter in string.ascii_uppercase:
    with open(f"{letter}.txt", "w") as file:
        file.write(f"This is file {letter}.txt")

# 21. Write a Python program to create a file where all letters of the English alphabet are listed with a specified number of letters on each line.

import string

letters = string.ascii_lowercase
n = int(input("Har bir qatorda nechta harf bo‘lsin: "))

with open("alphabet.txt", "w") as file:
    for i in range(0, len(letters), n):
        file.write(letters[i:i+n] + "\n")

