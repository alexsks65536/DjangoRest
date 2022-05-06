import React from 'react';
import './App.css';
import AuthorList from './components/Author.js';
import ProjectList from './components/Project.js';
import TodoList from './components/Todo.js';
import BookProjectList from './components/BookProject.js';
import ProjectForm from './components/ProjectForm.js';
import TodoForm from './components/TodoForm.js';
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
           'authors': [],
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
       axios.get('http://127.0.0.1:8000/api/authors/')
           .then(response => {
               this.setState({authors: response.data})

           }).catch(error => console.log(error));

       axios.get('http://127.0.0.1:8000/api/projects/')
           .then(response => {
              this.setState({projects: response.data})

           }).catch(error => console.log(error));

       axios.get('http://127.0.0.1:8000/api/todolist/')
           .then(response => {
               this.setState({todolist: response.data})

           }).catch(error => console.log(error));
    }

    deleteProject(id) {
        const headers = this.get_headers()
        axios.delete(`http://127.0.0.1:8000/api/project/${id}/`, {headers})
        .then(response => {
            this.setState({projects: this.state.projects.filter((item)=>item.id !== id)})
        }).catch(error => {
            console.log(error)
        })
    }

    createProject(name, repository, author) {
        const headers = this.get_headers()
        const data = {name: name, repository: repository, author: author}
        axios.post(`http://127.0.0.1:8000/api/projects/`, data, {headers})
        .then(response => {
        let new_project = response.data
        const author = this.state.authors.filter((item) => item.id === new_project.author)[0]
        new_project.author = author
        this.setState({projects: [...this.state.projects, new_project]})
        }).catch(error => console.log(error))
    }

    deleteTodo(id) {
        const headers = this.get_headers()
        axios.delete(`http://127.0.0.1:8000/api/todolist/${id}`, {headers})
        .then(response => {
        this.setState({todolist: this.state.todolist.filter((item)=>item.id !==
        id)})
        }).catch(error => console.log(error))
    }

    createTodo(title, content, projects, author) {
        const headers = this.get_headers()
        const data = {title: title, content: content, projects: projects, author: author}
        axios.post(`http://127.0.0.1:8000/api/todolist/`, data, {headers})
        .then(response => {
        let new_todo = response.data
        const author = this.state.authors.filter((item) => item.id === new_todo.author)[0]
        new_todo.author = author
        this.setState({todolist: [...this.state.todolist, new_todo]})
        }).catch(error => console.log(error))
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
                                <h3><Link to='/'>Authors</Link></h3>
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
                        <Route exact path='/' component={() => <AuthorList items={this.state.authors} />} />

                        <Route path="/project/:id">
                            <BookProjectList items={this.state.projects} />
                        </Route>
                        <Route exact path='/projects' component={() => <ProjectList
                            items={this.state.projects} deleteProject={(id)=>this.deleteProject(id)} />} />
                        <Route exact path='/projects/create' component={() => <ProjectForm
                            authors={this.state.authors} createProject={(name, repository, author) => this.createProject(name, repository, author)} />} />
                        <Route exact path='/todolist' component={() => <TodoList
                            items={this.state.todolist} deleteTodo={(id)=>this.deleteTodo(id)} />} />
                        <Route exact path='/todolist/create' component={() => <TodoForm
                            authors={this.state.authors} createTodo={(title, content, projects, author) => this.createTodo(title, content, projects, author)} />} />
                        <Route exact path='/login' component={() => <LoginForm get_token={(username, password) =>
                            this.get_token(username, password)} />} />
                        <Redirect from='/authors' to='/' />
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
