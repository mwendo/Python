x = [[5, 2, 3], [10, 8, 9]]
students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'}
]
sports_directory = {
    'basketball': ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer': ['Messi', 'Ronaldo', 'Rooney']
}
z = [{'x': 10, 'y': 20}]

# # 1
x[1][0] = 15
print(x[1][0])

# # 2
students[0]["last_name"] = "Bryant"
print(students[0]["last_name"])

# # 3
sports_directory["soccer"][0] = "Andres"
print(sports_directory["soccer"][0])

# # 4
z[0]['y'] = 30
print(z)

# 5
students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]
# iterateDictionary(students)
# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel


def iterateDictionary(list):
    for students in list:
        for key in students:
            print(students[key])


print(iterateDictionary(students))


def iterateDictionary2(key_name, some_list):
    for x in some_list:
        print(x[key_name])


iterateDictionary2("first_name", students)
iterateDictionary2("last_name", students)


# 6
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
# printInfo(dojo)
# output:
# 7 LOCATIONS
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank

# 8 INSTRUCTORS
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon


def myFunction(some_dict):
    for key, value in some_dict.items():
        print(key, len(value))
        for x in range(0, len(value), 1):
            print(value[x])


myFunction(dojo)
