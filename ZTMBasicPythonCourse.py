# Developer's Fundamentals
# I- learn efficient ways of doing things, examples of different methods and function - don't memorize everything, go by the most useful tools'
#II- Commenting your code - adding value through comments, keep it simple, easy to read, make sure they are understandable
#III- Know what data structure to use and when - takes practice and experience
#IV- What is good, clean code?  
    #Concise but not too concise, needs to be readable - 
    #Easily readable, no extra stuff - don't use obscure keywords - 
    #Predictability (each part efficiently does one thing really well) - 
    #DRY (don't repeat yourself)
#V- Test your assumptions, test code in detail, prove that ach part of the code is what you think it is
#VI- Libraries enable you to not have to start from scratch, but only use if:
    #there is broad support for the library
    #you can't just write your own library for the purpose at hand
    #read about libraries and combine different techniques to create something useful
#VII- Pick the right library - up to date, lots of community support

#Each coding language excels at some things and doesn't excel at others - they are specialized so many are needed
#For each language, learn:  Terms, Data Types, Actions, and Best Practices
#Lists
#   list slicing creates new list
#   lists are mutable, unlike strings
#   copying different from modifying a list
#
#4 Pillars of OOP
#   1- Encapsulation- use classes, attributes, methods, etc. to build an integrated structure.  Rather than separating classes an attributes, wrap them all in the same function
#   2- Abstraction - getting access to only what is necessary 
#       using built-in function
#       avoid coding from scratch 
#       abstract away variables for which the details aren't necessary to understand
#       use private variable (._name) to abstract away.  Dunder methods are example
#   3- Inheritance - new objects take on the properties of existing objects 
#       inherit classes, parent and children - avoids repeating code
#   4- Polymorphism - output different according to what object is calling it - enables customization of methods according to specific uses

#Data Types 
#   Fundamental, Custom (Classes), Specialized, None, and Complex (imaginary)

#   int - stored binary
#       
#   float - stored in two places, one binary before the . and one after
#   string - sometimes single quotes, sometimes double; concatenation only uses strings
#   escape sequences - 
#       Variables in snake case, only letters, numbers, and underscores.  Are case sensitive. Constants are variables which are not changed
#       One way of assigning variables - A,B,C = 1,2,3 =>> A1, B2, C3
#Expressions vs. Statements - expression is a piece of code producing a value, 
#   statement is like iq = 5
#Augmented Assignment Operator - i = += 2
#Escape Sequences - >  \  what comes after is string, used to deal with single vs double quotes
#   \t add table after \
#   \n add carriage return after \
#Formatted Strings - f-string - print(f'hi' + {name} + '.  You are str{age} + years old'.)
#String Indexes - [start:stop:stepover]  - 
#[0:7] from zero to seven not including seven - 
#[0:8:2] from zero to eight not including eight, stepping over 2 at a time
#[1:]from 1 until the end
#[: : 1] show all from beginning to end, stepping one by one
#[-1] only the last member of the list
#[: : -1] the whole list in reverse order
#Immutability of strings:  assigned permanently, have to make new to change
#Built-in methods - owned by something (print, len, int, str, abs, round)
#String methods:  .lower, .upper, .capitalize (beginning of words only), .count, dunder methods, 
#.find, .replace
#bool - to control flow of program; do one thing if true, another if false.  Truthy and Falsy
#Data types interact - example is when you use int or str to change the type
#List actions -  .append (to end of list), insert, extend (unpacks iterable) - these three modify the list in place
    #pop - removes last item; pop(0)- removes item at index 0; remove(4)- removes the value 4 not index; join (takes iterable)- new sentence = ' '.join(['hi', 'my', 'name', 'is', 'JOJO'] join the space with each quoted item); clear; index(value, start, stop); count('value'); sort (does not produce new array, modifies in place); copy; reverse (used with sort) or another way is: [::-1] which creates new list
#List functions- len, True, in, sorted (produces new array, new copy, like [:])
#List Unpacking- 
    #a,b,c *other, d = [1,2,,3,4,5,6,7,8,9]
    #print(a) => 1
    #print(b) => 2
    #print(c) => 3
    #print(other) => [4,5,6,7,8]
    #print(d) => 9
#None, null = absence of value, used as a starting point
#Dictionaries
    #ordered
    #can contain lists, bool, strings, etc.
    #dictionaries can hold more information, more efficient use of resources
    #dictionary keys are immutable and unique
    #.keys, .items, .values, .clear, .copy, .pop, .popitem, .update - print(user.update({'ages':55}))
#Tuples
    #immutable lists
    #accessible through indexing
    #communicates that shouldn't be changed
    #makes code more predictable, efficient, easier, faster than list to process, less flexible though
    #tuple can be a key in dicctionary
    #(2,) tuple with single item
    #x,y,z, other works with tuples, also .count, .indx, print
#Sets
    #unordered, unique objects (no duplicates)
    #each item in one and only one location in memory
    #doesn't allow duplicates to be added
    #making a set out of a list returns only the unique items
    #no indexing
    #.add, .copy, clear, and the functions in, len, list
    #also .difference (print(my_set.difference(your_set)))
    #also .discard() discard a value in a set
    #.difference_update - remove all items of another set from this set
    #.intersection - items in common
    #.isdisjoint - are the Venn diagram circles overlapping? no = disjoint
    # .union or | - unites but removes duplicates
    #.issubset - my_set is subset of your_set
    #.superset - my_set encompasses everything that is in your_set

#Conditional Logic - controlling the flow of the code, telling it to skip lines according to conditional logic
    #elif- can have multiple ones
    #indentation spacing - 4 spaces or tab, is distinction between hierarchies

#Falsy and Truthy
    #1 True 0 False

#----------------------------------------------
#----------------------------------------------

#----------------------------------------------
#----------------------------------------------
#print('helloooo')

# first_name = 'Dinah'
# last_name = 'Rosenbaum'
# full_name = first_name + ' ' + last_name
# print(last_name)

# weather = "\t It\'s \"kind of\" sunny \n hope you have a good day!"
# print(weather)

# name = 'Dinah'
# age = 60
# print(f'hi {name}. You are {age} years old')

# selfish = '01234567'
# print(selfish[0:8:2])
# 0246

# selfish = '01234567'
# print(selfish[::1])
# 01234567

# selfish = '01234567'
# print(selfish[::2])
# 0246

# selfish = '01234567'
# print(selfish[::-1])
# 76543210

# selfish = '01234567'
# print(selfish[::-2])
# 7531

# greet = 'hellloooo'
# print(greet[0:len(greet)])
# hellloooo

# birth_year = input('what year were you born?')
# age = 2025 - int(birth_year)
# print(f'You are {age} years old')

# username = input('What is your username?')
# password = input('What is your password?')
# password_length = len(password)
# hidden_password = '*' * password_length
# print(f'Your username is {username} and your password, {hidden_password}, is {password_length} characters long')

# cart = [
#     'notebooks',
#     'sunglasses',
#     'toys',
#     'grapes'
# ]
# print(cart[0::2])
# starts at zero, steps through by step of 2

# basket = [1,2,3,4,5]
# basket.append(100)
# new_list = basket
# print(basket)
# print(new_list)

# basket = [1,2,3,4,5]
# new_list = basket.append(100)
# print(basket)
# print(new_list)

# Grok Says:  Why does append return None?
# In Python, methods that modify an object in place (like list.append, list.extend, list.remove, etc.) typically return None to indicate they mutate the object directly rather than creating a new one. This is a design choice to make it clear that the operation is in-place. Methods that return a new object (like list.copy or string methods like str.upper) return the new object instead.

# basket = ['a', 'b', 'c', 'd','e']
# print('b' in basket)

# scores = [85, 92, 78, 95, 88]
# scores.sort(reverse=True)
# print(scores)  # Output: [95, 92, 88, 85, 78]

# Grok says about sort, sorted and reverse:
# Why Use a Sorted Reversed List?
# A sorted reversed list is useful when:

# You need to prioritize higher values (e.g., scores, prices, or timestamps) for tasks like ranking, filtering, or displaying data.
# The problem requires descending order, such as showing the "top N" items or processing data from most recent to oldest
# Choose sort(reverse=True) to modify the original list efficiently.
# Choose sorted(..., reverse=True) to preserve the original data or work with non-list iterables.

# List Unpacking:
# a,b,c, *other, d = [1,2,3,4,5,6,7,8,9]
# print(a)
# print(b)
# print(c)
# print(other)
# print(d)

# other is in between the first three and the last element
# Grok says:  
# uses unpacking with the * operator to assign values from the list to variables. The *other part is a special feature in Python called extended unpacking, introduced in Python 3, which collects any remaining elements into a list after assigning specific elements to other variables.
# The * collects these "other" elements into a list named other.

# Capture variable-length elements:
# Simplify code
# Extracting First, Last, and Middle Elements - 
# Example: Parsing a log file where the first two fields are metadata, the last field is a timestamp, and the middle fields are data

# using sets for lookups:
# my_set = {1,2,3,4,5,6}
# print(1 in my_set)

# These use cases demonstrate sets’ power in scenarios requiring uniqueness, fast lookups, or mathematical operations, making them a go-to choice for data processing, filtering, and algorithmic tasks in Python.

# Ternary Operators
# condition_if_true if condition else condition_if_else
# is_friend = True
# can_message = "mesage allowed" if is_friend else "not allowed to message"
# print(can_message)

# is_magician = True
# is_expert = False

# if is_expert and is_magician:
#     print("you are a master magician")

# elif is_magician and not is_expert:
#     print("at least you're getting there")

# elif not is_magician:
#     print("You need magic powers")

# For loops:
# my_list = [1,2,3,4,5,6,7,8,9]
# counter = 0
# for item in my_list:
#     counter = counter + item
# print(counter)

# Conditionals:
# is_old = True 
# is_licensed = True

# if is_old and is_licensed:
#     print('you are old enough to drive, and you have a license!')
# else:
#     print('you are not of age!')
# print('okokok')

# while True:
#     input('say something: ')
#     break

# my_list = [1,2,3]
# for item in my_list:
#     print(item)

# i = 0
# while i < len(my_list):
#     print(my_list[i])
#     i += 1


# picture = [
#     [0,0,0,1,0,0,0],
#     [0,0,1,1,1,0,0],
#     [0,1,1,1,1,1,0],
#     [1,1,1,1,1,1,1],
#     [0,0,0,1,0,0,0],
#     [0,0,0,1,0,0,0]
# ]
# fill = '*'
# empty = ' '
# for row in picture:
#     for pixel in row:
#         if pixel:
#             print(fill, end='')
#         else:
#             print(empty, end='')
#     print('')


# some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
# duplicates = []
# for value in some_list:
#     if some_list.count(value) > 1:
#         if value not in duplicates:
#             duplicates.append(value)
# print(duplicates)


# def sum(num1, num2):
#     return num1 + num2

# print(sum(10,sum(10, sum(10,5))))


# Nested Functions:
# def sum(num1, num2):
#     def another_func(num1, num2):
#         return num1 + num2
#     return another_func(num1, num2)

# total = sum(10,20)
# print(total)

# def checkDriverAge():
#     age = input("What is your age?: ")
#     if int(age) < 18:
#         print("Sorry, you are too young to drive this car. Powering off")
#     elif int(age) > 18:
#         print("Powering On. Enjoy the ride!");
#     elif int(age) == 18:
#         print("Congratulations on your first year of driving. Enjoy the ride!")
# checkDriverAge()

# Default Values:
# def checkDriverAge(age=0):
#     if int(age) < 18:
#         print("Sorry, you are too yound to drive this car. Powering off")
#     elif int(age) > 18:
#         print("Powering On. Enjoy the ride!");
#     elif int(age) == 18:
#         print("Congratulations on your first year of driving. Enjoy the ride!")
# checkDriverAge(19)


# Clean Code:
# def is_even(num):
#     return num % 2 == 0

# print(is_even(52))


# Positional Arguments and Keyword Arguments:
# def super_func(*args):
#     print(args)
#     print(sum(args))

# super_func(1,2,3,4,5)


# def super_func(*args, **kwargs):
#     total = 0
#     for items in kwargs.values():
#         total += items
#     return sum(args) + total
# print(super_func(1,2,3,4,5, num1=5, num2=10))


# def highest_even(li):
#     evens = []
#     for item in li:
#         if item % 2 == 0:
#             evens.append(item)
#     return max(evens)
# print(highest_even([3,10,4,8,11]))


# Walrus Operator:
# a = 'helloooooooooo'
# if ((n := len(a)) > 10):
#     print(f"too long {n} elements")

# while ((n := len(a)) > 1):
#     print(n)
#     a = a[:-1]
# print(a)


# Nonlocal keyword and scope and nested functions:
# def outer():
#     x = "local"
#     def inner():
#         nonlocal x
#         x = "nonlocal"
#         print("inner:", x)
#     inner()
#     print("outer:", x)
# outer()


# class PlayerCharacter:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def run(self):
#         print('run')
#         return 'done'

# player1 = PlayerCharacter('Cindy', 44)
# player2 = PlayerCharacter('Tom', 21)
# player1.attack = 100
# player2.attack = 50
# print(player1.name)
# print(player2.name)
# print(player1.age)
# print(player2.age)
# print(player1.attack)
# print(player2.attack)

# Result:  
# Cindy
# Tom
# 44
# 21
# 100
# 50


# Exercise Cats Everywhere

# Given the  below class:
    
# class Cat:
#     species = 'mammal'

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# #Instantiate the Cat object with 3 cats
# cat1 = Cat('cat1', 5)
# cat2 = Cat('cat2', 13)
# cat3 = Cat('cat3', 3)

# #Create function that finds the oldest cat
# def oldest_cat(*args):
#     return max(args)

# #Print out: "The oldest cat is x years old.".
# print(f'Oldest Cat is {oldest_cat(cat1.age, cat2.age, cat3.age)} years old.')

#--------------------------------
# class Pets():
#     animals = []
#     def __init__(self, animals):
#         self.animals = animals

#     def walk(self):
#         for animal in self.animals:
#             print(animal.walk())

# class Cat():
#     is_lazy = True

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def walk(self):
#         return f'{self.name} is just walking around'

# class Simon(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'

# class Sally(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'

#-------------------------------
#1 Add another Cat

# class Tikachu(Cat):
#     def sing(self,sounds):
#         return f'{sounds}'

#2 Create a list of all of the pets (create 3 cat instances from the above)
# my_cats = []
# cat1 = Simon('Simon', 10)
# cat2 = Sally('Sally', 15)
# cat3 = Tikachu('Tikachu', 5)

# my_cats.append(cat1)
# my_cats.append(cat2)
# my_cats.append(cat3)

#OR my_cats = [Simon('Simon', 10), Sally('Sally', 15), Tikachu('Tikachu', 5)]

#3 Instantiate the Pet class with all your cats use variable my_pets

# my_pets = Pets(my_cats)

#4 Output all of the cats walking using the my_pets instance

# my_pets.walk()
#-------------------------------
#------------------------------

# class User():
#     def __init__(self, email):
#         self.email = email
#     def sign_in(self):
#         print('logged in')

# class Wizard(User):
#     def __init__(self, name, power, email):
#         super().__init__(email)
#         self.name = name
#         self.power = power
#     def attack(self):
#         print(f'attacking with power of {self.power}')
        
# class Archer(User):
#     def __init__(self, name, num_arrows):
#         self.name = name
#         self.num_arrows = num_arrows
    

    # print(f'attacking with arrows: arrows left- {self.num_arrows}')
# wizard1 = Wizard('Merlin', 50, 'merlin@gmail.com')

# print(wizard1.email)
# archer1 = Archer('Robin', 100)
# [isinstance keyword]showing scope and inheritance
# [dir keyword] showing what functions are available for that object
#-------------------------------------
#-------------------------------------

# Dunder Methods:
# class Toy():
#     def __init__(self, color, age):
#         self.color = color
#         self.age = age
#         self.my_dict = {
#             'name': 'Yoyo',
#             'has_pets': False
#         }

#     def __str__(self):
#         return (f'{self.color}')
    
#     def __len__(self):
#         return 5
    
#     def __call__(self):
#         return('yesss??')
    
#     def __getitem__(self, i):
#         return self.my_dict[i]

# action_figure = Toy('red', 0)
# print(action_figure.__str__())       
# print(str(action_figure))
# print(len(action_figure))
# print (action_figure())
# print (action_figure['name'])

# Exercise:

# class SuperList(list):
#     def __len__(self):
#         return 1000
    
# super_list1 = SuperList();

# print(len(super_list1))
# super_list1.append(5)
# print(super_list1[0])
# print(issubclass(SuperList, list))
# print(issubclass(list, object))
#---------------------------------
#---------------------------------

# class User():
#     def sign_in(self):
#         print('logged in')

# class Wizard(User):
#     def __init__(self, name, power):
#         self.name = name
#         self.power = power
#     def attack(self):
#         print(f'attacking with power of {self.power}')
        
# class Archer(User):
#     def __init__(self, name, arrows):
#         self.name = name
#         self.arrows = arrows
    
#     def check_arrows(self):
#         print(f'{self.arrows} remaining')

#     def run(self):
#         print('ran really fast')

# class HybridBorg(Wizard, Archer):
#     def __init__(self, name, power, arrows):
#         Archer.__init__(self, name, arrows)
#         Wizard.__init__(self, name, power)

# hb1 = HybridBorg('borgie', 50, 100)
# print(hb1.check_arrows())

# print(f'attacking with arrows: arrows left- {self.num_arrows}')
# wizard1 = Wizard('Merlin', 50, 'merlin@gmail.com')
# print(wizard1.email)
# archer1 = Archer('Robin', 100)
#--------------------------------
#---------------------------------

# Map Function:
# my_list = [1,2,3]
# def multiply_by2(item):
#     return item*2

# print(list(map(multiply_by2, my_list)))
# print(my_list)

#--------------------------------
#---------------------------------
#Filter Function: 
# my_list = [1,2,3]

# def only_odd(item):
#     return item % 2 != 0

# print(list(filter(only_odd, my_list)))
# print(my_list)

#--------------------------------
#---------------------------------
# Zip Function:
# my_list = [1,2,3]
# your_list = [10,20,30]

# print(list(zip(my_list, your_list)))
# print(my_list)
# print(your_list)
#--------------------------------
#--------------------------------

# Reduce Function:
# from functools import reduce
# my_list = [1,2,3]

# def accumulator(acc, item):
#     print(acc, item)
#     return acc + item

# print(reduce(accumulator, my_list, 0))
# print(my_list)