import React from 'react';
import {Link} from 'react-router-dom';

const ProjectItem = ({item, deleteProject}) => {
   return (
    <tbody>
       <tr>
           <td>
               <Link to={`project/${item.id}`}>{item.id}</Link>
           </td>
           <td>{item.name}</td>
           <td>{item.repository}</td>
           <td>{item.author.username}</td>
           <td><button onClick={()=>deleteProject(item.id)} type='button'>Delete</button></td>
       </tr>
    </tbody>
   )
}

const ProjectList = ({items, deleteProject}) => {
   return (
    <div>
       <table>

                <tr>
                   <th>id</th>
                   <th>Name</th>
                   <th>Repository</th>
                   <th>Author</th>
                   <th> </th>
                </tr>
                   {items.map((item) => <ProjectItem item={item} deleteProject={deleteProject}/>)}

       </table>
       <Link to='/projects/create'>Create</Link>
    </div>
   )
}

export default ProjectList;