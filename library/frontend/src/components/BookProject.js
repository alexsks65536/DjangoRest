import React from 'react';
import { useParams } from 'react-router-dom';


const ProjectItem = ({item}) => {
    return (
        <tr>
            <td>{item.id}</td>
            <td>{item.name}</td>
            <td>{item.repository}</td>
            <td><button type='button'>Delete</button></td>
        </tr>
    )
}
const ProjectList = ({items}) => {
    let { id } = useParams();
    let filtered_projects = items.filter((item) => items.project.id == id)
    return (
        <table>
            <tr>
                <th>ID</th>
                <th>NAME</th>
                <th>REPOSITORY</th>
                <th></th>
            </tr>
            {filtered_projects.map((item) => <ProjectItem item={item} />)}
        </table>
    )
}
export default ProjectList;