import { useState } from "react";
import './FormReg.css'

export default function RegistrationFrom(){
const [name, setName] = useState('')
const [email, setEmail] = useState('')
const [pass, setPass] = useState('')
const [errors, setErrors] = useState({});

const validate = () => {
    const newErrors = {};
    if (pass.length <6) newErrors.pass = "Пароль должен содержать более 6 символов";
    setErrors(newErrors);
    if (!email.includes('1') || !email.includes('.')) newErrors.email = "Почта должна содержать символ 1";
    setErrors(newErrors);
    if (name.length <4) newErrors.name = "Имя должно содержать не менее 4 символов";
    setErrors(newErrors);

    return Object.keys(newErrors).length == 0;
    }

const handleSubmit = (e) => {
    e.preventDefault();
    if (validate()){
    console.log('Форма отпралвена', {name, email, pass});
}
}

    return(
//return - возращает данные 
            <form onSubmit={handleSubmit} className="body">
                <div>
                    <label >Имя:</label>
                    <input type="text" value={name} onChange={(e) => setName (e.target.value)}/>
                    {errors.name && <span style={{color:'red'}}> {errors.name}</span>}
                </div>
                <div>
                    <label>Почта:</label>
                    <input type="email" value={email} onChange={(e) => setEmail (e.target.value)}/>
                    {errors.email && <span style={{color:'red'}}> {errors.email}</span>}
                </div>
                <div>
                    <label>Пароль:</label>
                    <input type="password" value={pass} onChange={(e) => setPass (e.target.value)}/>
                    {errors.pass && <span style={{color:'red'}}> {errors.pass}</span>}
                       
                </div>
                <button type='submit' className="btn">Зарегистрироваться</button>
            </form>
//e - событие, безимянная функция
    )
}

