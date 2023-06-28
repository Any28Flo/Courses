const doubleDigitValue = (digit) => {
  let doubleDigit = digit * 2;
  let sum;
  if(doubleDigit >= 10){
      sum = 1 + doubleDigit %10;
  }else{
      sum = doubleDigit;
  }
  return sum
}
module.exports ={ doubleDigitValue}
