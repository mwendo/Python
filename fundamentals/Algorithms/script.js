function myFunction (str) {
    var count = 0;

    for (var i = 0; i<str.length; i++) {
        if (str[i] == "(") {
            count = count + 1;
        }

        else if (str[i] == ")") {
            count = count - 1;
        }

        else if (str[i] == "{") {
            count = count + 1;
        }

        else if (str[i] == "}") {
            count = count - 1;
        }

        else if (str[i] == "[") {
            count = count + 1;
        }

        else if (str[i] == "]") {
            count = count - 1;
        }

        else if (count < 0) {
            console.log(false);
            break;
        }
    }
    if (count == 0) {
        console.log(true);
    }
    else {
        console.log(false);
    }
}

myFunction("W(a{t}s[o(n{ c}o)m]e )h[e{r}e]!");
myFunction("D(i{a}l[ t]o)n{e");

// Aaron
// Sydney
// Micah