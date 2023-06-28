const inquirer = require("inquirer");

const askNumber = async str =>{
    const question = [
        {
            name : "digit",
            type: "input",
            message : str,
            validate : (input) =>{
                    if( isNaN(input)){
                        return "please enter a number"
                    }

                    return true
            }
        }
    ]
    try {
        const { digit } = await  inquirer.prompt(question);
        console.log(typeof  digit)
        return digit


    }catch (e) {

    }
}
module.exports ={
    askNumber
}
