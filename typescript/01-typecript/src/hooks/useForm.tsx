import React, {useState} from 'react';

const useForm = <T extends Object>(form : T ) => {

    const [state, setForm] = useState(form);

    const onChange = (value: string, name: keyof T) =>{
        setForm({
            ...state,
            [name] : value
        })
    }

    return{
        state,
        onChange
    }
};

export default useForm;