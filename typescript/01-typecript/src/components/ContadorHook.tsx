import {useCounter} from "../hooks/useCounter";

const ContadorHook = () => {

    const {value, add} = useCounter(100);

    return (
        <>
            <h1>Contador hook</h1>
            <h2>Counter <small>{value}</small></h2>
            <button
                className="btn btn-primary"
                onClick={() => add(1)}> +1
            </button>
            &nbsp;
            <button
                className="btn btn-primary"
                onClick={() => add(-1)}> -1</button>

        </>
    );

};

export default ContadorHook;