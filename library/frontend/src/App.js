import React from 'react';
import logo from './logo.svg';
import './App.css';
import UserList from './components/User.js';
import ProjectList from './components/Project.js';
import TodoList from './components/Todo.js';
import axios from 'axios';
import {BrowserRouter, Route, Link, Switch, Redirect} from 'react-router-dom';



function Footer(props) {
  return <h3>{props.item}</h3>;
}

const NotFound404 = ({ location }) => {
    return (
        <div>
            <h1>Страница по адресу '{location.pathname}' не найдена</h1>
        </div>
    )
}

class App extends React.Component {

   constructor(props) {
       super(props)
       this.state = {
           'users': [],
           'projects': [],
           'todos': []
        }
   }
   componentDidMount() {
       axios.get('http://127.0.0.1:8000/api/users/')
           .then(response => {
               const users = response.data
                   this.setState(
                   {
                       'users': users
                   }
               )
           }).catch(error => console.log(error));

       axios.get('http://127.0.0.1:8000/api/projects/')
           .then(response => {
               const projects = response.data
                   this.setState(
                   {
                       'projects': projects
                   }
               )
           }).catch(error => console.log(error));

       axios.get('http://127.0.0.1:8000/api/todolist/')
           .then(response => {
               const todos = response.data
                   this.setState(
                   {
                       'todos': todos
                   }
               )
           }).catch(error => console.log(error));
    }
   render() {
       return (
           <div className="App">
                <BrowserRouter>
                    <nav align='left'>
                        <ul>
                            <li>
                                <h3><Link to='/users'>Users</Link></h3>
                            </li>
                            <li>
                                <h3><Link to='/projects'>Projects</Link></h3>
                            </li>
                            <li>
                                <h3><Link to='/todolist'>ToDo</Link></h3>
                            </li>
                        </ul>
                    </nav>
                    <Switch>
                        <Route exact path='/users' component={() => <UserList users={this.state.users} />} />
                        <Route exact path='/projects' component={() => <ProjectList projects={this.state.projects} />} />
                        <Route exact path='/todolist' component={() => <TodoList todos={this.state.todos} />} />
                        <Redirect from='/projects' to='/' />
                        <Route component={NotFound404} />
                    </Switch>
                        <Footer item=<a href='https://gb.ru/lessons/199082/'>Copyright GeekBrains TODO &copy; 2022</a> />
                        <h5><Link to='https://gb.ru/lessons/199082/'>Django REST Framework</Link></h5>
                </BrowserRouter>
           </div>
       )
   }
}


export default App;
