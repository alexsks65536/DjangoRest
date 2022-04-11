import React from 'react'
import { useParams } from 'react-router-dom'


const ProjectItem = ({project}) => {
    return (
        <tr>
            <td>{project.id}</td>
            <td>{project.name}</td>
            <td>{project.repository}</td>
        </tr>
    )
}
const ProjectList = ({projects}) => {
    let { id } = useParams();
    let filtered_projects = projects.filter((project) => projects.project.id == id)
    return (
        <table>
            <tr>
                <th>ID</th>
                <th>NAME</th>
                <th>REPOSITORY</th>
            </tr>
            {filtered_projects.map((project) => <ProjectItem project={project} />)}
        </table>
    )
}
export default ProjectList