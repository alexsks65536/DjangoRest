import React from 'react';
import './App.css';
import UserList from './components/User.js';
import ProjectList from './components/Project.js';
import TodoList from './components/Todo.js';
import BookProjectList from './components/BookProject.js';
import LoginForm from './components/Auth.js'
import axios from 'axios';
import Cookies from 'universal-cookie';
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
           'todos': [],
           'token': ''
        }
   }

    set_token(token) {
        //const cookies = new Cookies()
        localStorage.setItem('token', token)
        this.setState({'token': token}, ()=>this.load_data())
    }

    is_authenticated() {
        return this.state.token != ''
    }

    logout() {
        this.set_token('')
    }

    get_token_from_storage() {
        //const cookies = new Cookies()
        const token = localStorage.getItem('token')
        this.setState({'token': token}, ()=>this.load_data())
    }

    get_token(username, password) {
       axios.post('http://127.0.0.1:8000/api-token-auth/', {username: username, password: password}).then(response =>
       {
            this.set_token(response.data['token'])
       }).catch(error => alert('Неверный логин или пароль'))
    }

    get_headers() {
        let headers = {
            'Content-Type': 'application/json'
        }
        if (this.is_authenticated())
        {
            headers['Authorization'] = 'Token ' + this.state.token
        }
        return headers
    }

   load_data() {
       axios.get('http://127.0.0.1:8000/api/users/')
           .then(response => {
               this.setState({users: response.data})


           }).catch(error => console.log(error));

       axios.get('http://127.0.0.1:8000/api/projects/')
           .then(response => {
              this.setState({projects: response.data})


           }).catch(error => console.log(error));

       axios.get('http://127.0.0.1:8000/api/todolist/')
           .then(response => {
               this.setState({todos: response.data})


           }).catch(error => console.log(error));
    }

    componentDidMount() {
        this.get_token_from_storage()
        this.load_data()
    }


   render() {
       return (
           <div className="App">
                <BrowserRouter>
                    <nav align='left'>
                        <ul>
                            <li>
                                <h3><Link to='/'>Users</Link></h3>
                            </li>
                            <li>
                                <h3><Link to='/projects'>Projects</Link></h3>
                            </li>
                            <li>
                                <h3><Link to='/todolist'>ToDo</Link></h3>
                            </li>
                            <li>
                                {this.is_authenticated() ? <button onClick={()=>
                                    this.logout()}>Logout</button> : <Link to='/login'>Login</Link>}
                            </li>
                        </ul>
                    </nav>
                    <Switch>
                        <Route exact path='/' component={() => <UserList items={this.state.users} />} />
                        <Route exact path='/projects' component={() => <ProjectList items={this.state.projects} />} />
                        <Route path="/project/:id">
                            <BookProjectList items={this.state.projects} />
                        </Route>
                        <Route exact path='/todolist' component={() => <TodoList items={this.state.todos} />} />
                        <Route exact path='/login' component={() => <LoginForm get_token={(username, password) =>
                            this.get_token(username, password)} />} />
                        <Redirect from='/users' to='/' />
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
