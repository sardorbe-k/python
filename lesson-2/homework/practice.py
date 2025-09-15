# 1. Age Calculator
#Write a Python program to ask for a user's name and year of birth, then calculate and display their age.
name = input('Sizning ismingiz:')
birth_year = int(input("Tug'ilgan yilingizni kiriting:"))
current_year = 2025
age = current_year - birth_year
print(f"Salom, {name}! Sizning yoshingiz {age} da ")

# 2. Extract Car Names
#Extract car names from the following text:
txt = 'LMaasleitbtui'
car = txt[1]  + txt[2] + txt[4] + txt[6] + txt[7] + txt[8] + txt[12]
print(car)

# 3. Extract Car Names
#Extract car names from the following text:

txt2 = 'MsaatmiazD'
car2 = txt2[0] + txt2[2] + txt2[-2] + txt2[-1].lower() + txt2[-3]
print(car2)

# 4. Extract Residence Area. Extract the residence area from the following text:

txt = "I'am John. I am from London"
start = txt.find("London")
print(txt[start:])

# 5.  Reverse String. Write a Python program that takes a user input string and prints it in reverse order.

word = input('Nimadir yozing:')
print(word[::-1])

# 6. Count Vowels. Write a Python program that counts the number of vowels in a given string.

text = input("Matn kiriting: ")
vowels = "aeiouAEIOU"  
count = 0

for ch in text:
    if ch in vowels:
        count += 1
print("Matndagi unli harflar soni:", count)

# 7. Find Maximum Value. Write a Python program that takes a list of numbers as input and prints the maximum value.

numbers = [12, 45, 7, 89, 23, 56]   
print("Eng katta qiymat:", max(numbers))

# 8.  Check Palindrome. Write a Python program that checks if a given word is a palindrome (reads the same forward and backward).

word = input("So'z kiriting: ")

if word == word[::-1]:
    print("Bu so'z palindrom!")
else:
    print("Bu so'z palindrom emas.")

# 9. Extract Email Domain. Write a Python program that extracts and prints the domain from an email address provided by the user.

email = input("Email manzilingizni kiriting: ")
domain = email.split('@')[1]

print("Domen:", domain)

# 10. Generate Random Password. Write a Python program to generate a random password containing letters, digits, and special characters

import random
belgilar = "abcçdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%&*?"
uzunlik = int(input("Parol uzunligini kiriting: "))
parol = ""
for i in range(uzunlik):
    parol += random.choice(belgilar)
print("Tasodifiy parol:", parol)






 
