import React from 'react';


class TodoForm extends React.Component {
    constructor(props) {
        super(props)
        this.state = {title: '', content: '', projects: '', user: props.users[0].id}
    }

    handleChange(event)
    {
        this.setState(
            {
                [event.target.name]: event.target.value
            }
        );
    }

    handleSubmit(event) {
        this.props.createTodo(this.state.title, this.state.content, this.state.projects, this.state.user)

        event.preventDefault()
    }

    render() {
        return (
            <form onSubmit={(event)=> this.handleSubmit(event)}>
                <div className="form-group">
                    <label for="title">title</label>
                    <input type="text" className="form-control" name="title"
                    value={this.state.title} onChange={(event)=>this.handleChange(event)} />
                </div>
                <div className="form-group">
                    <label for="content">content</label>
                    <input type="text" className="form-control" name="content"
                    value={this.state.content} onChange={(event)=>this.handleChange(event)} />
                </div>
                <div className="form-group">
                    <label for="projects">projects</label>
                    <input type="number" className="form-control" name="projects"
                    value={this.state.projects} onChange={(event)=>this.handleChange(event)} />
                </div>
                <div className="form-group">
                    <label for="user">user</label>
                    <select name="user" className='form-control'
                        onChange={(event)=>this.handleChange(event)}>
                        {this.props.users.map((item)=><option
                        value={item.id}>{item.username}</option>)}
                    </select>
                </div>
                <input type="submit" className="btn btn-primary" value="Save" />
            </form>
        );
    }
}
export default TodoForm;