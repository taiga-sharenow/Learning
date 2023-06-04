
//Functions
function add(x,y){
    return x + y;
}
function sub(x,y){
    return x - y;
}
function multi(x,y){
    return x * y;
}
function divi(x,y){
    return x / y;
}


//let choice = prompt('Choice the operation \n 1 - Add \n 2 - Subtract \n 3 - Multiplication \n 4 - Division \n 5 - Exit');
let x ;
let y ;
let choice = "";

//Loop Init
do {

    //Init option
    choice = prompt('Choice the operation \n 1 - Add \n 2 - Subtract \n 3 - Multiplication \n 4 - Division \n 5 - Exit');
    
    //Exit
    if (choice == '5') {
        break;
    }

    //Validation
    while (choice != '1' && choice != '2' && choice != '3' && choice != '4' && choice != '5') {
        alert('Invalid operation!');
        choice = prompt('Choice the operation \n 1 - Add \n 2 - Subtract \n 3 - Multiplication \n 4 - Division \n 5 - Exit');
    }

    //If the user choice a valid option
    x = parseFloat(prompt('Input the first value: ')); //First value
    y = parseFloat(prompt('Input the second value: ')); //Secont Value

    switch (choice) {
        case '1' :
            alert(add(x, y));
            break;
        case '2' :
            alert(sub(x, y));
            break;
        case '3' :
            alert(multi(x, y));
            break;
        case '4' :
            alert(divi(x, y));
            break;
    }

} while(choice === '1' || choice ===  '2' || choice === '3' || choice === '4') //Conditions

alert("That's all folks!!")