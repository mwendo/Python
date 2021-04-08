// // 04/06/2021
// function myFunction (str) {
//     var count = 0;

//     for (var i = 0; i<str.length; i++) {
//         if (str[i] == "(") {
//             count = count + 1;
//         }

//         else if (str[i] == ")") {
//             count = count - 1;
//         }

//         else if (str[i] == "{") {
//             count = count + 1;
//         }

//         else if (str[i] == "}") {
//             count = count - 1;
//         }

//         else if (str[i] == "[") {
//             count = count + 1;
//         }

//         else if (str[i] == "]") {
//             count = count - 1;
//         }

//         else if (count < 0) {
//             console.log(false);
//             break;
//         }
//     }
//     if (count == 0) {
//         console.log(true);
//     }
//     else {
//         console.log(false);
//     }
// }

// myFunction("W(a{t}s[o(n{ c}o)m]e )h[e{r}e]!");
// myFunction("D(i{a}l[ t]o)n{e");

// // Aaron
// // Sydney
// // Micah


// // 04/07/2021
// function palindrome(intext) {
//     var revtext = intext.split('').reverse().join('');
//     console.log(revtext == intext);
//     }
    
// palindrome("racecar")

// function palindromeBig(intext) {
//     var intextSpl = intext.split('').reverse();
//     console.log (intextSpl);

//     for(var i = 0; i<intextSpl.length; i++) {
//         if(intextSpl[i-1] == intextSpl[i + 1]){
            
//         }
//     }
// }

// palindromeBig("here is my big racecar george");

Martin is writing his opus: a book of algorithm challenges, set as lyrics to a suite of a cappella fugues. Some of ‘those fugueing challenges’ are less popular than others, so he needs an index. Given a sorted array of pages where a term appears, produce an index string. Consecutive pages should form ranges separated by a hyphen. For
       
[1,13,14,15,37,38,70], return string "1, 13-15, 37-38, 70". Take care to get all the commas and spaces correct: Martin is palpably particular (practically persnickety!) about patchy punctuation.

// 04/08/2021
// var empty = arr.toString("");

// var arr = [1,13,14,15,37,38,70];
// var str = arr.toString();
// var result = [arr[0]];

// for(var i = 0; i<arr.length; i++) {
//     if ((str[i-1]%2 === 0)&&(str[i]%2 === 0)){
//         result.push('-', str[i]);
//     }
//     else{
//         result.push(arr[i]);
//     }
// }

// console.log((result.join('')));

function bookIndex(arr){
    var newStr = "";
    for(var i = 0; i < arr.length; i++){
        if(arr[i] + 1 == arr[i+1]) {
            newStr += arr[i] + "-";
            while(arr[i] + 1 == arr[i+1]){
                i++;
            }
            newStr += arr[i] + ", ";
        }
        else {
            newStr += arr[i];
            if(arr.length=1 != i) {
                newStr += ", ";
            }
        }
    }
    return newStr;
}

console.log(bookIndex([1, 13, 14, 15, 37, 38, 70]));

// Given an array, I want to loop through the array in order to find the start of a consecutive group of numbers. Once i locate the start, I want to be able to locate the end of the consecutive numbers.