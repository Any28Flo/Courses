import useForm from "../hooks/useForm";


const Form = () => {

  const {state, onChange} = useForm({
      username: "",
      password: ""
  });

    return (
        <div>
            <h2>Formulario</h2>
            <input
                className = "form-control mt-2 mb-2"
                type="text"
                value={state.username}
                placeholder="Tu username"
                onChange={(event) => onChange(event.target.value, "username")}
            />
            <input
                className = "form-control mt-2 mb-2"
                type="password"
                value={state.password}
                placeholder="Tu password"
                onChange={({target})=>onChange(target.value, "password")}
            />
            <code>
                <pre>{JSON.stringify({state})}</pre>
            </code>
        </div>
    );
};

export default Form;