let age = 28;
console.log(age);

// loose vs strict comparions 
console.log(age == '28');
console.log(age === '28');
console.log(age != '28');
console.log(age !== '28');

// template string with backticks
console.log(`the age is ${age}`);

// throws TypeError for assigning to constant
const points = 100;
console.log(points);
// points = 50;

// array methods
let ninjas = ['alpha', 'beta', 'gamma'];
// let results = ninjas.join('-');
// let results = ninjas.indexOf('gamma');
// ninjas.push('zeta');
// result = ninjas.pop();
// console.log(result);
let results = ninjas.concat(['delta', 'epsilon']);    // similiar to Python list.extends()
console.log(results);

// explicit type conversion
let score = '100';
score = Number(score);
console.log(score + 1);
console.log(typeof score);