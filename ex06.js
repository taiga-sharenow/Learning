//Strings
let answer = "";
let toRemove = "";
let product = "";
let option = "";

//Arrays
var arr_freeze = [];
var arr_fruit = [];
var arr_milk = [];
var arr_candy = [];

//I use in inputs .toLocaleLowerCase, because i think this is more easy to treat the information

while (answer != 'no'){

    //First interact
    answer = prompt('Do you wanna input a item in your list, yes or no? \n Or do you wanna remove any item? If yes, write "remove"').toLocaleLowerCase();
    
    //Exit
    if (answer == 'no') {
        break;
    }

    //Validation
    while (answer != 'yes' && answer != 'no' && answer != 'remove') {
        alert('invalid option');
        answer = prompt('Do you wanna input a item in your list, yes or no? \n Or do you wanna remove any item? If yes, write "remove"').toLocaleLowerCase();
    }
    
    //Add some item to list
    if (answer == 'yes') {
        
        product = prompt('Insert the name of product to add: '); //Input
        option = prompt('1 - Frozen products \n 2 - Fruits \n 3 - Dairy products \n 4 - Candies') //Option where input
        
        switch (option) {
            case '1' :
                arr_freeze.push(product);
                break;
            case '2' :
                arr_fruit.push(product);
                break;
            case '3' :
                arr_milk.push(product);
                break;
            case '4' :
                arr_candy.push(product);
                break;
            default : 
                alert('Insert a valid option');
        }
    }

    //Function to remove some item
    if (answer == 'remove') {
        if (arr_freeze === 0 && arr_candy === 0 && arr_fruit === 0 && arr_milk === 0) {
            alert("Don't exist any product in your list.");
        } else {
            toRemove = prompt(`What product do you want to remove? \n List: \n Frozen products ${arr_freeze} \n Fruits ${arr_fruit} \n Dairy products ${arr_milk} \n Candies ${arr_candy}`);
            if (arr_freeze.indexOf(toRemove) != -1){
                arr_freeze.splice(arr_freeze.indexOf(toRemove), 1);
                alert(`${toRemove} has been removed`);
            } else if(arr_fruit.indexOf(toRemove) != -1){
                arr_fruit.splice(arr_fruit.indexOf(toRemove), 1);
                alert(`${toRemove} has been removed`);
            } else if(arr_milk.indexOf(toRemove) != -1){
                arr_milk.splice(arr_milk.indexOf(toRemove), 1);
                alert(`${toRemove} has been removed`);
            } else if(arr_candy.indexOf(toRemove) != -1){
                arr_candy.splice(arr_candy.indexOf(toRemove), 1);
                alert(`${toRemove} has been removed`);
            } else {
                alert('Nonexistent item');
            }
        }
    }

    //Relation Loop
    answer = prompt('Do want continue, Yes or no?').toLocaleLowerCase();
}

alert(`List: \n Frozen products: ${arr_freeze} \n Fruits: ${arr_fruit} \n Dairy products: ${arr_milk} \n Candies: ${arr_candy}`);