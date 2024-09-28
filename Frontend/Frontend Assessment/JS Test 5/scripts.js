// Write a JavaScript function that takes an array of numbers as an argument and converts it to an object. The object should have a key
//  for each unique value in the array, and the corresponding value should be the number of times the key occurs within the array.

function count(arr){
    const  occurrence ={};

    arr.forEach((num) => {
        occurrence[num] = (occurrence[num] || 0) + 1;
    });
    return occurrence;
} 

const array = [1,55,6,3,7,8,5,1,2,2,55,99,99,55]
const result = count(array);
console.log(result);