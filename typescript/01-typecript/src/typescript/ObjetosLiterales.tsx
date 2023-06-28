export interface Persona {
    name : string,
    age: number,
    direccion : Address

}
interface Address{
    calle: string,
    numero : number
}
const ObjetosLiterales = () => {

    let chucho : Persona ={
        name :"chucho",
        age: 12,
        direccion:{
            calle: "siempre viva",
            numero: 12
        }

    }
    return (
        <div>
            <code>
                <pre>
                    {JSON.stringify(chucho,null, 2)}
                </pre>
            </code>
        </div>
    );
};

export default ObjetosLiterales;