# 1. Sort a Dictionary by Value. Write a Python script to sort (ascending and descending) a dictionary by value.
my_dict = {'apple': 10, 'banana': 2, 'orange': 5, 'mango': 7}

ascending = dict(sorted(my_dict.items(), key=lambda x: x[1]))
print("O'sish tartibida:", ascending)

descending = dict(sorted(my_dict.items(), key=lambda x: x[1], reverse=True))
print("Kamayish tartibida:", descending)

# 2. Add a Key to a Dictionary. Write a Python script to add a key to a dictionary.

my_dict = {0: 10, 1: 20}

my_dict[2] = 30

print(my_dict)

# 3. Concatenate Multiple Dictionaries. Write a Python script to concatenate the following dictionaries to create a new one.
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

new_dict = {}
new_dict.update(dic1)
new_dict.update(dic2)
new_dict.update(dic3)

print(new_dict)

# 4.  Generate a Dictionary with Squares. Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).

n = 5

squares = {x: x*x for x in range(1, n+1)}

print(squares)

# 5. . Dictionary of Squares (1 to 15). Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are the square of the keys.
squares = {x: x*x for x in range(1, 16)}

print(squares)

#Set Exercises
# 1. 1. Create a Set. Write a Python program to create a set.
my_set = {1, 2, 3, 4, 5}

print(my_set)

# 2. Iterate Over a Set. Write a Python program to iterate over sets
my_set = {"apple", "banana", "cherry"}

for item in my_set:
    print(item)

# 3.  Add Member(s) to a Set. Write a Python program to add member(s) to a set.
my_set = {"apple", "banana"}
my_set.add("cherry")

my_set.update(["mango", "grape"])

print("Qo'shilgandan keyin:", my_set)

# 4. Remove Item(s) from a Set.Write a Python program to remove item(s) from a given set.
my_set = {"apple", "banana", "cherry", "mango"}

my_set.remove("banana")  

my_set.discard("mango")

print("O'chirilgandan keyin:", my_set)

# 5.  Remove an Item if Present in the Set. Write a Python program to remove an item from a set if it is present in the set.
my_set = {"apple", "banana", "cherry"}

item = "banana"
if item in my_set:
    my_set.remove(item)

print("Natija:", my_set)


