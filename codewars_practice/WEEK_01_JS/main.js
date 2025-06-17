/// Multiplying numbers as strings --> 4kyu
// function multiply(a, b) {
//   if (a === "0" || b === "0") return "0";
//
//   let result = Array(a.length + b.length).fill(0);
//
//   for (let i = a.length - 1; i >= 0; i--) {
//     for (let j = b.length - 1; j >= 0; j--) {
//       const mul = Number(a[i]) * Number(b[j]);
//       const p1 = i + j, p2 = i + j + 1;
//       const sum = mul + result[p2];
//
//       result[p2] = sum % 10;
//       result[p1] += Math.floor(sum / 10);
//     }
//   }
//
//   while (result[0] === 0) result.shift();
//
//   return result.join('');
// }
//
// console.log(multiply(12,12))


/// Convert a String to a Number! --> 8kyu
// const stringToNumber = function(str){
//   return parseInt(str)
// }
// console.log(stringToNumber("14"))

///
