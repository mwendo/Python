# 1
for x in range(0, 151, 1):
    print(x)

# 2
for x in range(5, 1001, 5):
    print(x)

# 3
for x in range(1, 101, 1):
    if (x % 10 == 0):
        print("Coding Dojo")
    elif (x % 5 == 0):
        print("Coding")
    else:
        print(x)

# 4
sum = 0
for x in range(1, 500000, 1):
    if(x % 2 == 1):
        sum += x
print(sum)

# 5
for x in range(2018, 0, -4):
    print(x)

# 6
lowNum = 2
highNum = 9
mult = 3
for x in range(lowNum -1, highNum + 1, 1):
    if (x % mult ==0):
        print(x)
