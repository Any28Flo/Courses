
const Tiposbasicos = () => {
    const name:string = "Erika";
    const age:number = 29;
    const isProgrammer: boolean = true;
    let superPowers : string[] =[];
    superPowers.push("volar");
    superPowers.push("inteligencia")
    return (
        <div>
            <h2>Tipos basicos</h2>
            <hr/>
            <p>Hello my name is {name} I'm {age} years old </p>
            <p>{`I'm a ${isProgrammer ? "programmer" : "hero"}`}</p>
            <ul>
                {
                    superPowers.map( (elem,idx) =>{
                        return(
                            <li key={`item-${idx}`}>
                                {elem}
                            </li>
                        )
                    })
                }

            </ul>
            <p></p>


        </div>
    );
};

export default Tiposbasicos;