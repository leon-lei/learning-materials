// object literals

let user = {
    name: 'leon',
    age: 28,
    email: 'leonlei35t@gmail.com',
    location: 'New York',
    blogs: ['django', 'flask'],
    login: function(){
        console.log('user logged in');
    },
    logout: function(){
        console.log('user logged out');
    },
    logBlogs(){    // alternate syntax to create regular functions
        //console.log(this.blogs);    // 'this' is context object set by javascript
        console.log('this user has written the following blogs');
        this.blogs.forEach(blog => {
            console.log(blog);
        })
    }
};

console.log(user);
console.log(user.name);    // dot notation
user.age = 29
console.log(user['age']);    // square bracket notation
console.log(typeof user);

// calling method on object
user.login();
user.logout();
user.logBlogs();

// Math object
console.log(Math);
console.log(Math.PI);
const random = Math.random();
console.log(Math.round(random * 100));

// stack and heap
// copies of primitive values (integer here) is stored on stack
// each variable have their own copy
let scoreOne = 50;
let scoreTwo = scoreOne;
scoreOne = 75;
console.log(`scoreOne: ${scoreOne}`, `scoreTwo: ${scoreTwo}`);

// copies of reference objects have both pointers on stack point to same object on heap
let userOne = {name: 'leon', food: 'ramen'};
let userTwo = userOne
userOne.food = 'pizza'
console.log(`userOne: ${userOne.food}`, `userTwo: ${userTwo.food}`);
