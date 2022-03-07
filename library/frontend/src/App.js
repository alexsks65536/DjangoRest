import React from 'react';
import logo from './logo.svg';
import './App.css';
import UserList from './components/User.js';
import axios from 'axios';


function Menu(props) {
  return <li>{props.item}</li>;
}

function Footer(props) {
  return <h3>{props.item}</h3>;
}

class App extends React.Component {

   constructor(props) {
       super(props)
       this.state = {
           'users': [],
       }
   }

   componentDidMount() {
   axios.get('http://127.0.0.1:8000/api/users/')
       .then(response => {
           const users = response.data
               this.setState(
               {
                   'users': users,
               }
           )
       }).catch(error => console.log(error));
}


   render () {
       return (
           <div>
                <Menu item=<a href='#'>"Главная"</a> />
                <Menu item=<a href='#'>"TODO-заметки"</a> />
                <Menu item=<a href='#'>"Вход/Регистрация"</a> />
                <UserList users={this.state.users} />
                <Footer item=<a href='https://gb.ru/lessons/199082/'>Copyright GeekBrains TODO &copy; 2022</a> />


           </div>
       )
   }
}


export default App;
