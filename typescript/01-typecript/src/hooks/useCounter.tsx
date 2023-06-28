import {useState} from "react";

export const useCounter = (initValue: number = 0) => {

    const [value, setValue] = useState(initValue);

    const add = (number: number) => {
        setValue(value + number)
    };
    return {
        value,
        add
    }

};