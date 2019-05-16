// function declaration
function greet(){
    console.log('hello world');
}

// function expression
// cannot change function because assigned to constant
// expressions also do not get hoisted unlike declarations
const speak = function(name='lei', time='night'){
    console.log(`good ${time} ${name}`);
};

greet();
speak('leon', 'morning');
speak();

// regular function
const calcArea = function(radius){
    return 3.14 * radius**2;
};
const area = calcArea(5);
console.log(area);
console.log(calcArea(6));

// arrow function
const calcArea2 = (radius) => 3.14 * radius**2;
console.log(calcArea2(7));

const speak2 = (name='foobar', time='dawn') => console.log(`good ${time} ${name}`);
speak2('templar', 'evening');
speak2();

const bill = (products, tax) => {
    let total = 0;
    for(let i = 0; i < products.length; i++){
        total += products[i] + products[i] * tax;
    }
    return total;
};
console.log(bill([10,15,30], 0.2));

// callbacks & forEach
const logPerson = (person, index) => {
    console.log(index, person, 'from logPerson');
};

const people = ['alpha', 'beta', 'gamma', 'delta']

// passing in arrow function
people.forEach((person, index) => {
    console.log(index, person);
});

// passing in function expression
people.forEach(logPerson);

// get a reference to 'ul'
const ul = document.querySelector('.people');
let html = ``;
people.forEach(person => html += `<li style="color: purple">${person}</li>`);


ul.innerHTML = html;