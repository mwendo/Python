num1 = 42  # variable declaration (integer)
num2 = 2.3 # variable declaration (integer)
boolean = True # variable declaration (boolean)
string = 'Hello World' # variable declaration (string)
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] # variable declaration array (lists)
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} # variable declaration dictionary
fruit = ('blueberry', 'strawberry', 'banana') # variable declaration tuples 
print(type(fruit)) # log statement  
print(pizza_toppings[1]) # log statement type check
pizza_toppings.append('Mushrooms') # lists add value
print(person['name']) # log statement access value
person['name'] = 'George' # dictionary change value
person['eye_color'] = 'blue' # dictionary add value
print(fruit[2]) # tuple access value

if num1 > 45: # conditional if else statement
    print("It's greater")
else:
    print("It's lower")

if len(string) < 5: # conditional if else if statement
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")

for x in range(5): # for loop
    print(x)
for x in range(2,5):
    print(x)
for x in range(2,10,3):
    print(x)
x = 0
while(x < 5): # while loops
    print(x)
    x += 1

pizza_toppings.pop() # composite list delete value 
pizza_toppings.pop(1) # composite list delete value

print(person) # log statement
person.pop('eye_color') # dictionary delete value 
print(person) # log statement

for topping in pizza_toppings: # for loop
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement')
    if topping == 'Olives':
        break

def print_hello_ten_times(): # function and for loop
    for num in range(10):
        print('Hello')

print_hello_ten_times() # log statements

def print_hello_x_times(x): # function and for loop
    for num in range(x):
        print('Hello')

print_hello_x_times(4) #log statements

def print_hello_x_or_ten_times(x = 10): # function and for loop
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)