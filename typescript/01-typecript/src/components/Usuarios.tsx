import {useEffect, useRef, useState} from "react";
import {ReqResListado, User} from "../interfaces/reqRes";
import {reqResApi} from "../api/reqRes";
import useUsuarios from "../hooks/useUsuarios";

const Usuarios = () => {

    const {users, handleNext, handlePrev} = useUsuarios();


    const renderUser = ({id, first_name, last_name, avatar}: User, index: number) => {
        return (
            <tr key={`${id}`}>
                <th scope="row">{index + 1}</th>
                <td>{first_name}</td>
                <td>{last_name}</td>
                <td><img src={`${avatar}`} alt="avatar"/></td>
            </tr>
        )
    };

    return (
        <>
            <table className="table">
                <thead>
                <tr>
                    <th scope="col">#</th>
                    <th scope="col">First</th>
                    <th scope="col">Last</th>
                    <th scope="col">Avatar</th>
                </tr>
                </thead>
                <tbody>
                {
                    users.map(renderUser)
                }
                </tbody>
            </table>

            <button onClick={handleNext}>Next</button>
            <button onClick={handlePrev}>Prev</button>

        </>
    );
};

export default Usuarios;