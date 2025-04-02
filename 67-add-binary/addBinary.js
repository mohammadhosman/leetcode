/**
 * @param {string} a
 * @param {string} b
 * @return {string}
 */

function calculateBinary(expr) {
    let [pre, post] = expr
      .split(/[+|\-|\*|\/]/)
      .map((binary) => parseInt(parseInt(binary, 2).toString(10).trim()));
    let sign = expr.match(/[+|\-|\*|\/]/)[0];
    let res = eval(pre + sign + post);
    return res.toString(2);
  }
  
  var addBinary = function(a, b) {
    let expr = a + b;
    return calculateBinary(expr);
  };