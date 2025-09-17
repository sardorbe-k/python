   # 1. Create and Access List Elements. Create a list containing five different fruits and print the third fruit.

fruits = ['apple', 'banana','lemon','orange','ananas']
print(fruits[2])

# 2. Concatenate Two Lists. Create two lists of numbers and concatenate them into a single list.

num1 = [1,2,3]
num2 = [4,5,6]
num1.extend(num2)
print(num1)

# 3. Extract Elements from a List. Given a list of numbers, extract the first, middle, and last elements and store them in a new list.

number = [10, 20, 30, 40, 50]
first_number = number [0]
middle_number = number[len(number)//2]
last_number = number [-1]
new_list = [first_number, middle_number, last_number]
print('New sheet',new_list)

# 4. Convert List to Tuple. Create a list of your five favorite movies and convert it into a tuple.

movies = ["Inception", "Interstellar", "Avatar", "Titanic", "The Dark Knight"]

movies_tuple = tuple(movies)

print("Ro'yxat",movies)
print("Kortej",movies_tuple)

# 5.  Check Element in a List. Given a list of cities, check if "Paris" is in the list and print the result.

cities = ["London", "Paris", "Berlin", "Tokyo", "New York"]

print("Paris" in cities)

# 6.  Duplicate a List Without Using Loops. Create a list of numbers and duplicate it without using loops.

numbers = [1, 2, 3, 4, 5]

duplicate = numbers * 2

print("Asl ro'yxat:", numbers)
print("Dublikat ro'yxat:", duplicate)

# 7. Swap First and Last Elements of a List. Given a list of numbers, swap the first and last elements.

number = [10, 20, 30, 40, 50 ]
print('Asl ruyxat',number )

number[0] ,number[-1] = number[-1], number[0]
print('almashtirilgan holati' ,number)

# 8. Slice a Tuple. Create a tuple of numbers from 1 to 10 and print a slice from index 3 to 7.

number= (1,2,3,4,5,6,7,8,9)
print('Aslisi:',number)

number=number[2:7]
print('Uzgartirish kiritilganidan sung:',number)

# 9.Count Occurrences in a List. Create a list of colors and count how many times "blue" appears in the list.

colours = ['blue','yellow','red','orange','blue','blue']
print(colours.count('blue'))

# 10.  Find the Index of an Element in a Tuple. Given a tuple of animals, find the index of "lion".

animals = ('lion','mouse','tiger','dog','horse')
print(animals.index('lion'))

# 11. Merge Two Tuples. Create two tuples of numbers and merge them into a single tuple.

num1 = (12, 16, 20)

num2 = (23, 26, 30)
new = num1+num2
print(new)

# 12. Find the Length of a List and Tuple. Given a list and a tuple, find and print their lengths.
names_list = ['Salim','Alisher','Malika','Nozanin','Amin'] 
names_tuple = ('Salim','Alisher','Malika','Nozanin','Amin') 

print(len(names_list))   
print(len(names_tuple))  

# 13.Convert Tuple to List. Create a tuple of five numbers and convert it into a list.

numbers_tuple = (10, 20, 30, 40, 50)   
numbers_list = list(numbers_tuple)     
print(numbers_list)

# 14.  Find Maximum and Minimum in a Tuple. Given a tuple of numbers, find and print the maximum and minimum values.

numbers = (12, 45, 7, 89, 23, 56)

print("Eng katta son:", max(numbers))
print("Eng kichik son:", min(numbers))

# 15. Reverse a Tuple. Create a tuple of words and print it in reverse order.

number = (12, 13, 14, 15, 16, 17, 18)
print(number[::-1])

