const input = require('fs').readFileSync('/dev/stdin').toString().trim().split("\n");

const separation = input[0]
.split("-")
.map(a=>a.split("+")
.map(a=>Number(a)))
.map(a=>a.reduce((acc,cur) => acc + cur))

function parenthesis(separation) {
  let result = separation[0];
  if(separation.length > 1) {
    for(let i = 1; i < separation.length; i++) {
      result -= separation[i]
    }
  }
  return result;
}

console.log(parenthesis(separation));