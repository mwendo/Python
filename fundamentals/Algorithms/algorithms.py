
# function myFunction (str) {
#     var count = 0;

#     for (var i = 0; i<str.length; i++) {
#         if (str[i] == "(") {
#             count = count + 1;
#         }

#         else if (str[i] == ")") {
#             count = count - 1;
#         }
#     }
#     if (count == 0) {
#         console.log(true);
#     }
#     else {
#         console.log(false);
#     }
# }

# myFunction("N(0(p)3");

def function (str):
    count = 0
    for i in range(0, len(str), 1):
        if(str[i] == "("):
            count = count + 1
        elif (str[i] == ")"):
            count = count - 1
    if (count == 0):
        print(true)
    else:
        print(false)

function("N(0(p)3")