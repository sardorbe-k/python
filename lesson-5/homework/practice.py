# 1
try:
    year = int(input("Yilni kiriting: "))

    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"{year} - kabisa yili ✅")
    else:
        print(f"{year} - oddiy yil ❌")

except ValueError:
    print("Xato: Yil butun son bo‘lishi kerak!")

#2 
n = int(input('sonni kiriting?').strip())   

if n % 2 != 0:            
    print("Weird")
elif n % 2 == 0 and 2 <= n <= 5:
    print("Not Weird")
elif n % 2 == 0 and 6 <= n <= 20:
    print("Weird")
elif n % 2 == 0 and n > 20:
    print("Not Weird")

#3
def even_numbers(a, b):
    if a > b:  
        return
    if a % 2 == 0:
        print(a)
    even_numbers(a + 1, b) 
even_numbers(2, 10)

