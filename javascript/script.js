function closeMe(){
    x=document.getElementById("demo");
    // Option 1: Change the style attribute directly
    // x.style.display="none";
    // Option 2: Change the class
    x.className="closed";
}

function openMe(){
    x=document.getElementById("demo");
    // Option 1: Change the style attribute directly
    // x.style.display="block";
    // Option 2: Change the class
    x.className="open";
}

function displayId(element){
    console.log(element.id)
}

function showProperties(element){
    document.getElementById('message').innerHTML=element.alt;
}

var fruits = ["Banana", "Orange", "Apple", "Mango"];

function loadFruits(){
 document.getElementById("fruits").innerHTML= fruits;   
}

function myFunction(){
    var fruit = prompt("What is your favorite fruit? ");
    fruits[fruits.length] = fruit;
    document.getElementById("fruits").innerHTML = fruits;

}

function check(){
    let email1 = document.getElementById('email_addr');
    let email2 = document.getElementById('email_repeat');
    if (email1.value != email2.value){
        alert("The two emails must match!");
        return false;
    } else{
        alert("Emails matched!");
        return true;
    }
}

function nicknameFunction(){
    if (document.getElementById('yesNick').checked){
        document.getElementById('nick').style.display="inline";
        document.getElementById("nickname").setAttribute('required',true);
    }
    else{
        document.getElementById('nickname').removeAttribute('required');
        document.getElementById('nick').style.display="none";
    }
}