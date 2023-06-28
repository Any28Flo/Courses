import {useEffect, useReducer} from "react";
import Usuarios from "./Usuarios";


interface AuthState {
    token: string | null,
    username: string,
    name: string,
    loading: boolean
}


const initState: AuthState = {
    loading: true,
    name: "",
    token: null,
    username: ""

}
type LoginPayload = {
    name: string,
    username: string,
    token: string
}

type  AuthType = { type: "loading" } | { type: "login", payload: LoginPayload } | { type: "logout" };

function reducer(state: AuthState, action: AuthType): AuthState {
    switch (action.type) {
        case 'loading':
            return {
                loading: false,
                name: "",
                token: "",
                username: ""
            }
        case "login":
            const { name , username, token } = action.payload;
            return {
                ...state,
                name,
                username,
                token
            }
        case "logout":
            return {
                ...initState,
                loading: false,
            }

        default:
            return state
    }
}

const Login = () => {

    const [{loading, token}, dispatch] = useReducer(reducer, initState);

    useEffect(() => {
        setTimeout(() => {
            dispatch({type: "loading"})
        }, 1500)

    }, []);

    if (loading) {
        return (
            <>
                <div className="alert alert-info">Validando....</div>
            </>
        )
    }


    return (
        <>
            {
                token ?
                    <>
                        <div className="alert alert-success">Autencado</div>
                        <Usuarios/>
                        <butt on className="btn btn-primary"
                                onClick={() => dispatch({type: "logout"})}
                        >
                            Log out
                        </button>
                    </>
                    :
                    <>
                        <div className="alert alert-danger">No autenticado</div>


                        <button className="btn btn-primary"
                                onClick={() => dispatch({
                                    type: "login", payload: {
                                        name: "Eri",
                                        username: "Daedra",
                                        token: "123"
                                    }
                                })}
                        >
                            Login
                        </button>
                    </>

            }

        </>
    );
};

export default Login;
