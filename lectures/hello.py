num = 10
name = "Mr. Nibbles"
isWorking = True
pi = 3.14

# !Composite Types
# ? Arrays are called Lists
# Lists have indexes
ninjas = ['Harleigh', 'Keith', 'Rodney']
print(ninjas[2])
print(len(ninjas))


# ? Dictionaries are objects
dojo = {'locaiton': 'Chicago', "num_of_ninjas":37}

# ? Tuples are immutable Lists
tuple_dojo = ("Chicago", 37)


# ! Loops
for x in range(len(ninjas) -1, -1, -1):
    print(ninjas[x])


# ! Conditionals
if name == "Mr. Nibbles":
    print("Hello " + name)
    print("Hello", name)
    print(f"Hello {name}")
elif name == "Benny Bob":
    print("Oh no!")
else:
    print("Where is Mr. Nibbles?")

fav_color = "purple"
color = input("What is your favorite color?")
while color != fav_color:
    color = input(f"That is wrong. \n What is your favorite color?")
print(f"Your favorite color is {color}")