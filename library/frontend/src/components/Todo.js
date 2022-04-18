import React from 'react';
import {Link} from 'react-router-dom';

const TodoItem = ({item, deleteTodo}) => {
   return (
       <tr>
            <td>
               {item.id}
           </td>
           <td width='20%'>
               {item.title}
           </td>
           <td width='40%'>
               {item.content}
           </td>
           <td>
               {item.user.username}
           </td>
           <td>
               {item.created}
           </td>
           <td>
               {item.isactive}
           </td>
           <td><button onClick={()=>deleteTodo(item.id)}type='button'>Delete</button></td>
       </tr>
   )
}

const TodoList = ({items, deleteTodo}) => {
   return (
    <div>
       <table>
            <th>
               id
           </th>
           <th>
               Title
           </th>
           <th>
               Content
           </th>
           <th> User </th>
           <th>
               Created
           </th>
           <th>
               IsActive
           </th>
           <th> </th>
           {items.map((item) => <TodoItem item={item} deleteTodo={deleteTodo}/>)}
       </table>
       <Link to='/todolist/create'>Create</Link>
     </div>
   )
}

export default TodoList;

