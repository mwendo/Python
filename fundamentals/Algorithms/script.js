// 04/06/2021
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


// 04/07/2021
function palindrome(intext) {
    var revtext = intext.split('').reverse().join('');
    console.log(revtext == intext);
    }
    
palindrome("racecar")

function palindromeBig(intext) {
    var intextSpl = intext.split('').reverse();
    console.log (intextSpl);

    for(var i = 0; i<intextSpl.length; i++) {
        if(intextSpl[i-1] == intextSpl[i + 1]){
            
        }
    }
}

palindromeBig("here is my big racecar george");