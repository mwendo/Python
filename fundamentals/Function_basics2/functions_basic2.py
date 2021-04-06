# 1
def countdown(num):
    result = []
    for x in range(num, -1, -1):
        result.append(x)
    return result
print(countdown(10))


# 2
def print_and_return(x):
    print(x[0])
    return x[1]

print(print_and_return([1,2]))

# 3
def first_plus_length(x):
    sum = x[0] + len(x)
    return sum
print(first_plus_length([1,2,3,4,5]))

# 4
def values_greater_than_second(x):
    newList = []
    count = 0
    for i in range(0, len(x), 1):
        if (x[i] > x[1]):
            newList.append(x[i])
            count = count + 1
    print(count)
    if (len(newList) < 2):
        return false
    return newList
    
print(values_greater_than_second([5,2,3,2,1,4]))


# 5
def this_length_that_value(size, value):
    newList = []
    for x in range(0, size, 1):
        newList.append(value)
    return newList

print(this_length_that_value(5, 2))