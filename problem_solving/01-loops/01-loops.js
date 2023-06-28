//Draw a line
/*for (let index = 0; index < 5; index++) {
    console.log("*");

}
console.log("\n");
*/

//Draw a square
let string = ""
for (let row = 0; row < 5 ; row++) {
    for (let index = 0; index < 5; index++) {
        string += "*"

    }
    string += "\n"
}
console.log(string)

//Draw a half square
let string_2 = ""
for (let row = 0; row < 5 ; row++) {
    for (let index = 0; index < 5 - row; index++) {
        string_2 += "*"

    }
    string_2 += "\n"
}
console.log(string_2);

/*
* Sideways triangle
* #
* ##
* ###
* ##
* #
*
* */
let string_3 = "";

for(let row = 1 ; row < 7 ; row++){
    for(let x = 1 ; x < 4 - Math.abs(4- row) ; x++){
            string_3 += "*";
    }
    string_3+= "\n";

}
console.log(string_3)
