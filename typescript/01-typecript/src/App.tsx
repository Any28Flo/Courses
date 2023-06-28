import {useState} from 'react'
import Tiposbasicos from "./typescript/Tiposbasicos";
import ObjetosLiterales from "./typescript/ObjetosLiterales";
import Funciones from "./typescript/Funciones";
import Contador from "./components/Contador";
import ContadorHook from "./components/ContadorHook";
import Login from "./components/Login";
import Form from "./components/Form";

function App() {

    return (
        <div className="App container">
            {/*<Tiposbasicos/>*/}
            {/*<ObjetosLiterales/>*/}
            {/*<Funciones/>*/}
            {/*<Contador/>*/}
            {/*<ContadorHook/>*/}
           {/* <Login/>*/}
            <Form/>
        </div>
    )
}

export default App