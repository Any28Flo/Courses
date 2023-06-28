require("colors");

const {askNumber}  =require ("./helpers/inquire");
const {doubleDigitValue} = require("./helpers/helpers");


const main = async () => {
   // const digit = await askNumber("Enter a one-digit number");
    let digit = "";
    let position = 1;
    let oddLengthCheckSum = 0;
    let evenLengthCheckSum = 0;

    digit = await askNumber("Enter a one-digit number");
    let charCode = digit.charCodeAt(0);
    console.log(charCode)
    while(digit  != 10){

        if(position % 2 === 0 ){
            oddLengthCheckSum += doubleDigitValue(digit -'0');
            evenLengthCheckSum += digit - '0';

        }else{
            oddLengthCheckSum += digit - '0';
            evenLengthCheckSum += doubleDigitValue(digit -'0');
        }
        digit = await askNumber("Enter a one-digit number");

        position++;
    }
    let checksum;
    if((position -1 ) % 2 === 0 ) checksum = evenLengthCheckSum;
    else checksum = oddLengthCheckSum;

    console.log( `Checksum is ${ checksum}`);
    if(checksum % 10 ===0) {
        console.log("Checksum is divisible by 10. " +" Valid ".green);
    }else{
        console.log("Checksum is not divisible by 10. " +"Invalid ".red);

    }
  //  console.log(typeof  digit)

}
main();
