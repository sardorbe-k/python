#1 
used_chars = ['a', 'e', 'i', 'u', 'o']
index = 2
my_txt = 'abcabcabcdeabcdefabcdefgyy'

while index < len(my_txt) - 1:
    if my_txt[index] not in used_chars:
        used_chars.append(my_txt[index])
        my_txt = my_txt[:index + 1] + '_' + my_txt[index +1:]
        index += 4
        
    else:
        index += 1

print(my_txt)

# 2 
n = int(input('son kirting ').strip())  

for i in range(n):       
    print(i ** 2)        

# 3 Loop-Based Exercises. Exercise 1: Print first 10 natural numbers using a while loop

i = 1 
while i <= 10:
    print(i)
    i += 1

#Exercise 2: Print the following pattern
rows = 5
for i in range(1, rows + 1):          
    for j in range(1, i + 1):        
        print(j, end=" ")             
    print()                           

# Exercise 3: Calculate sum of all numbers from 1 to a given number
n = int(input("Enter number: "))
total = 0
i = 1

while i <= n:
    total += i
    i += 1

print("Sum is:", total)

#Exercise 4: Print multiplication table of a given number
n = int(input("Enter number: "))

for i in range(1, 11):     
    print(n * i)

# Exercise 5: Display numbers from a list using a loop

numbers = [12, 75, 150, 180, 145, 525, 50]

for num in numbers:
    if num >=500:
        break
    if num > 150:
        continue
    if num % 5 != 0:
        continue   
    print(num)

# Exercise 6: Count the total number of digits in a number

num = 75869

print(len(str(num)))

# Exercise 7: Print reverse number pattern

n = 5

for i in range(n, 0, -1):
    for j in range(i, 0, -1):
        print(j, end="")
    print()

# Exercise 8: Print list in reverse order using a loop

list1 = [10, 20, 30, 40, 50]

for i in range(len(list1)-1,-1,-1):
    print(list1[i])

# Exercise 9: Display numbers from -10 to -1 using a for loop

for num in range(-10,0):
    print(num)

# Exercise 10: Display message “Done” after successful loop execution

for num in range(0,5):
    print(num)
else:
    print("Done")

# Exercise 11: Print all prime numbers within a range

start = 25
end = 50

print("Prime numbers between", start, "and", end, ":")

for num in range(start, end +1):
    if num >1 :
        for i in range(2, int(num ** 0.5)+1):
            if num % i == 0:
                break
        else:
            print(num)


# Exercise 12: Display Fibonacci series up to 10 terms

n = 10
a,b = 0,1

print("Fibonacci sequence:")
for i in range(n):
    print(a, end="")
    a,b = b,a + b 

# Exercise 13: Find the factorial of a given number

num = 5
factorial = 1

for i in range(1, num + 1):
    factorial *= i  

print(f"{num}! = {factorial}")

# 4
def uncommon_elements(list1, list2):
    result = []

    for x in list1:
        if x not in list2:
            result.append(x)

    for y in list2:
        if y not in list1:
            result.append(y)

    return result

print(uncommon_elements([1, 1, 2], [2, 3, 4]))

print(uncommon_elements([1, 2, 3], [4, 5, 6]))

print(uncommon_elements([1, 1, 2, 3, 4, 2], [1, 3, 4, 5]))


