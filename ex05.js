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
    answer = prompt('Do you wanna input a item in your list, yes or no?').toLocaleLowerCase();
    
    //Exit
    if (answer == 'no') {
        break;
    }

    //Validation
    while (answer != 'yes' && answer != 'no') {
        alert('invalid option');
        answer = prompt('Do you wanna input a item in your list, yes or no?').toLocaleLowerCase();
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

    //Relation Loop
    answer = prompt('Do want continue, Yes or no?').toLocaleLowerCase();
}

alert(`List: \n Frozen products: ${arr_freeze} \n Fruits: ${arr_fruit} \n Dairy products: ${arr_milk} \n Candies: ${arr_candy}`);