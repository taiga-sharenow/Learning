//Strings
let response = "";

let secret = Math.floor(Math.random() * (10 - 0 + 1) + 0); //Get a random number
let chances = 3; //Three is a good number
let victory = false; //You can't start winning

console.log(secret); //For don't think why I were cheating

//Init because is True and True
while (chances > 0 && victory == false) {
    response = parseInt(prompt('Try to guess a number between 0 and 10'));
    if (response === secret) {  
        //To change the state and break, don't needed \break;
        victory = true; 
        alert('You win');
    } else {
        chances = chances - 1;
        alert(`You wrong, try again, chances: ${chances}`);
    }
}
if (chances == 0 && victory == false) {
    alert(`You lose, the number was ${secret}`);
}