import React from 'react'


const TodoItem = ({item}) => {
   return (
       <tr>
            <td>
               {item.id}
           </td>
           <td>
               {item.title}
           </td>
           <td>
               {item.content}
           </td>
           <td>
               {item.created}
           </td>
           <td>
               {item.isactive}
           </td>
       </tr>
   )
}


const TodoList = ({items}) => {
   return (
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
           <th>
               Created
           </th>
           <th>
               IsActive
           </th>
           {items.map((item) => <TodoItem item={item} />)}
       </table>
   )
}


export default TodoList

