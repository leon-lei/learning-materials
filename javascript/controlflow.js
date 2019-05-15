// for loops
for(let i = 0; i < 5; i++){
    console.log('in for loop:', i);
}

const names = ['leon', 'stephen', 'shawn'];
for(let i = 0; i < names.length; i++){
    // console.log(names[i]);
    let html = `<div>${names[i]}</div>`;
    console.log(html);
}

// while loop
let a = 0;
while(a < 5){
    console.log('in while loop:', a);
    a++;
}

let b = 0
while(b < names.length){
    console.log(names[b]);
    b++;
}

// do while loop
// runs at least once even though 'y' doesn't satisfy condition
let y = 5;
do{
    console.log('val of y is: ', y);
    y++;
} while(y < 5);

// if statements
const password = 'p@ssword1234';
if(password.length >= 12){
    console.log('Super Strong password');
} else if(password.length >= 8){
    console.log('Strong password');
} else {
    console.log('Weak password');
}

// logical operators - OR || and AND &&
if(password.length >= 12 && password.includes('@')){
    console.log('Super Strong password');
} else if(password.length >= 8 || password.includes('@')){
    console.log('Strong password');
} else {
    console.log('Weak password');
}

// logical NOT (!)
let user = false;
if(!user){
    console.log('You must be logged in to continue');
}

// break and continue
const scores = [50,0,35,100,90];
for(let i = 0; i < scores.length; i++){
    if(scores[i] == 0){
        continue;
    }
    console.log('Your score: ', scores[i]);
    if(scores[i] == 100){
        console.log('Top score!');
        break;
    }
}

// switch statements
const grade = 'C';

switch(grade){
    case 'A':
        console.log('You got an A');
        break;
    case 'B':
        console.log('You got an B');
        break;
    case 'C':
        console.log('You got an C');
        break;
    case 'D':
        console.log('You got an D');
        break;
    default:
        console.log('not a valid grade');
}

// variables & block scope
let broth = 'shio';
if(true){
    // broth = 'shoyu';    // will overwrite the global scope broth variable as well
    let broth = 'tonkotsu';    // local scope
    let noodles = 'straight';
    console.log(`Inside 1st code block: ${broth} broth with ${noodles} noodles`);
    
    if(true){
        let broth = 'tsukemen'
        console.log(`Inside 2nd code block: ${broth} broth with ${noodles} noodles`);
        var dessert = 'mochi';
    }
}

// console.log(`Outside code block: ${broth} broth with ${noodles} noodles`);     // noodles variable not defined globally and throws error
console.log(`Outside code block calling var dessert from code block: ${dessert} `)    // var ignores block scope