import {useEffect, useRef, useState} from "react";
import {ReqResListado, User} from "../interfaces/reqRes";
import {reqResApi} from "../api/reqRes";

const useUsuarios = () => {

    const [users, setUsers] = useState<User[]>([]);
    const paginationRef = useRef(1);

    useEffect(() => {
        cargarUsuarios()
    }, []);


    const cargarUsuarios = async () =>{

        try {
            const response =  await reqResApi.get<ReqResListado>(`/users`, {
                params : { page : paginationRef.current}
            })

            if(response.data.data.length > 0){
                setUsers(response.data.data);

            }else{
                paginationRef.current--;

                alert("Ya no hay mas data")
            }
        }catch (e) {

        }
    };
    const handleNext =async (       ) =>{
        paginationRef.current++
         cargarUsuarios()
    }
    const handlePrev = async () =>{
        if(paginationRef.current > 1){
            paginationRef.current--;
            await cargarUsuarios()
        }

    }

    return{
        users,
        handleNext,
        handlePrev
    }
};

export default useUsuarios;