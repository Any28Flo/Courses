import {Persona} from "./ObjetosLiterales";

const Funciones = () => {
    const printName =(user: Persona):string=>{
        return (`${user.name} ${user.age}`)
    }
    const add = (a:number, b:number):number => {
      return  a +b
    }
    let pepita : Persona ={
        name : "pepia",
        age: 12,
        direccion:{
            calle :"ad",
            numero:12
        }
    }
    return (
        <div>
            {printName(pepita)}
            <br/>

            <p>El resultado es {add(12,1)}</p>
        </div>
    );
};

export default Funciones;