import React from 'react'
import {Link} from 'react-router-dom'

const ProjectItem = ({project}) => {
   return (
       <tr>
            <td>
               {project.id}
           </td>
           <td>
               {project.name}
           </td>
           <td>
               {project.repository}
           </td>
           <td>
               {project.user}
           </td>
       </tr>
   )
}

const ProjectList = ({projects}) => {
   return (
       <table>
            <th>
               id
           </th>
           <th>
               Name
           </th>
           <th>
               Repository
           </th>
           <th>
               User
           </th>
           {projects.map((project) => <ProjectItem project={project} />)}
       </table>
   )
}


export default ProjectList