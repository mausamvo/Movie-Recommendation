import React, { Component } from 'react';
import '../App.css';

const LoginForm = () => {
    return (
        <div className='container'>
            <form  className='Auth-form'>
                <div className='alignment'>
                    <label style={{color: 'white', fontWeight: 'bold', padding: 17, fontSize: 20, textDecorationLine: 'underline' }}>LOGIN</label>
                </div>
                <div className='alignment'>
                    <input type="email" name="useremail" placeholder='Your Email' required></input>
                </div>
                <div className='alignment'>
                    <input type="password" placeholder='Password' name="userpassword" required></input>
                </div>
                <div className='alignment'>
                    <input style={{fontWeight: 'bold', padding: 5, marginTop:20, marginBottom:20 }} type="submit"></input>
                </div>
            </form>
        </div>
    );
}


class Counter extends Component {

    render(){
        return(
            <LoginForm />
        )
    }
}
 
export default Counter;

