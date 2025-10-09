#Loyihaning tuzilmasi:
#project/
#│
#├── main.py
#├── math_operations.py
#├── string_utils.py
#│
#├── geometry/
#│   ├── __init__.py
#│   └── circle.py
#│
#└── file_operations/
#    ├── __init__.py
#    ├── file_reader.py
#    └── file_writer.py

#1️— math_operations.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Bo‘lish mumkin emas!"
    return a / b

️3# — string_utils.py
def reverse_string(text):
    """Berilgan matnni teskari chiqaradi"""
    return text[::-1]

def count_vowels(text):
    """Matndagi unlilar sonini sanaydi"""
    vowels = "aeiouAEIOU"
    return sum(1 for ch in text if ch in vowels)

 ️#3 — geometry/circle.py
import math

def calculate_area(radius):
    """Aylananing yuzasini hisoblaydi"""
    return math.pi * radius ** 2

def calculate_circumference(radius):
    """Aylananing uzunligini hisoblaydi"""
    return 2 * math.pi * radius

# 4️ — file_operations/file_reader.py
def read_file(file_path):
    """Faylni o‘qiydi"""
    try:
        with open(file_path, "r") as f:
            return f.read()
    except FileNotFoundError:
        return "Fayl topilmadi."

# 5️ — file_operations/file_writer.py
def write_file(file_path, content):
    """Matnni faylga yozadi"""
    with open(file_path, "w") as f:
        f.write(content)
    print(" Faylga yozildi.")

#6 — main.py (asosiy fayl)
from math_operations import add, subtract, multiply, divide
from string_utils import reverse_string, count_vowels
from geometry.circle import calculate_area, calculate_circumference
from file_operations.file_reader import read_file
from file_operations.file_writer import write_file

# === Math operations ===
print("Matematik amallar:")
print("Qo‘shish:", add(10, 5))
print("Ayrish:", subtract(10, 5))
print("Ko‘paytirish:", multiply(10, 5))
print("Bo‘lish:", divide(10, 2))
print("-" * 40)

# === String utilities ===
print("Matn funksiyalari:")
print("Teskari:", reverse_string("Python"))
print("Unlilar soni:", count_vowels("Programming Language"))
print("-" * 40)

# === Geometry package ===
print("Aylana hisoblari:")
print("Yuza:", calculate_area(7))
print("Uzunlik:", calculate_circumference(7))
print("-" * 40)

# === File operations ===
print("Fayl funksiyalari:")
write_file("example.txt", "Bu test matni faylga yozildi.")
print("O‘qilgan matn:", read_file("example.txt"))

# Ishga tushirish

#Terminalda shu buyruqni yozasiz:

#python main.py
