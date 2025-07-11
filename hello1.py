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

