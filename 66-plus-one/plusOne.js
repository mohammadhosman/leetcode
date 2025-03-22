/**
 * @param {number[]} digits
 * @return {number[]}
 */
var plusOne = function(digits) {
    let number = 0n;
    for (let i = 0; i < digits.length; i++) {
      number += BigInt(digits[i]);
      number *= BigInt(10);
    }
    //   digits.array.forEach((element) => {
    //     number += element;
    //     number *= 10;
    //   });
    //   number = digits.map((digit) => {
    //     number += digit;
    //     number *= 10;
    //   });
    number = number / 10n;
    number++;
    let answer = [];
    let split_nums = number.toString().split("");
    answer = split_nums.map(Number);
    return answer;
  };