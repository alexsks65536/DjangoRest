import React from 'react'
import {Link} from 'react-router-dom'

const ProjectItem = ({item}) => {
   return (
       <tr>
            <td>
               <Link to={`project/${item.id}`}>{item.id}</Link>
           </td>
           <td>
               {item.name}
           </td>
           <td>
               {item.repository}
           </td>
           <td>
               {item.user}
           </td>
       </tr>
   )
}

const ProjectList = ({items}) => {
   return (
       <table>
           <th>
               Name
           </th>
           <th>
               Repository
           </th>
           <th>
               User
           </th>
           {items.map((item) => <ProjectItem item={item} />)}
       </table>
   )
}

export default ProjectList