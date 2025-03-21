/**
 * @param {number[]} digits
 * @return {number[]}
 */
var plusOne = function(digits) {
    let number = 0n;
       digits.array.forEach((element) => {
         number += element;
         number *= 10;
       });
       number = digits.map((digit) => {
         number += digit;
         number *= 10;
       });
       return number;
  };