import React, { Component } from 'react';
import '../App.css';
import MovieCard from './MovieCard';

// send the movie list here from backend! 
const movies_list = ["m1", "m2", "m3", "m4", "m5", "m6", "m7","m8", "m9", "m10"];

const UserProfile = () => {
    return (
        <div>
            <h2 className='titles' style={{color: "#CBC3E3", padding: 10}}>Top 10 recommendations: </h2>
            <div className='movie'>
                {movies_list.map((x, index) => (<MovieCard key={"movie_"+index} movie_name={x} />))}
            </div>
            <h2 className='titles' style={{color: "#CBC3E3", padding: 10}}>Movie list: </h2>
            <div className='movie'>
                {movies_list.map((x, index) => (<MovieCard key={"movie_"+index} movie_name={x} />))}
            </div>
        </div>
    );
}


class User extends Component {

    render(){
        return(
            <UserProfile />
        )
    }
}
 
export default User;

