// CSS selector
const head2 = document.querySelector('h2'); // tag selector
head2.innerText = 'Shio ramen';
// const para = document.querySelector('.first'); // class selector
// const para = document.querySelector('p#demo'); // tag and id selector
// console.log(para);

const paras = document.querySelectorAll('p'); // returns NodeList
paras.forEach(para => {
    console.log(para);
});
console.log(paras[2]);

// get an element by ID
const demo = document.getElementById('demo');
console.log(demo);

// get elements by their class name
// returns HTMLCollection
const firsts = document.getElementsByClassName('first');
console.log(firsts);

// get elements by their tag name
const paras2 = document.getElementsByTagName('p');
console.log(paras2);

// update element style
const title = document.querySelector('h1');
title.style.margin = '30px';
title.style.color = 'crimson';
title.style.fontSize = '60px';
console.log(title.style);

// updating class
const content = document.querySelector('h3');
content.classList.add('error');
console.log(content.classList);
content.classList.remove('error');
content.classList.add('success');

// updating multiple elements' classes
const hfours = document.querySelectorAll('h4');
console.log(hfours)
hfours.forEach(hfour => {
    if(hfour.textContent.includes('success')){
        hfour.classList.add('success');
    } else if(hfour.textContent.includes('error')){
        hfour.classList.add('error');
    }
});

// toggle classes on an element
const toggled = document.querySelector('.toggleMe');
toggled.classList.toggle('test');
toggled.classList.toggle('test');