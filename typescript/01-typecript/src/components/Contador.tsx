import React, {useState} from 'react';

const Contador = () => {

    const [counter, setCounter] = useState(0);

    const add = (value : number) => {
        setCounter( counter + value)
    };

    return (
        <>
            <h2>Counter <small>{counter}</small></h2>
            <button onClick={()=>add(1)}> +1</button>
            <button onClick={ () =>add(-1) }> -1</button>

        </>
    );
};

export default Contador;