import React from 'react'


const TodoItem = ({todo}) => {
   return (
       <tr>
            <td>
               {todo.id}
           </td>
           <td>
               {todo.title}
           </td>
           <td>
               {todo.content}
           </td>
           <td>
               {todo.created}
           </td>
           <td>
               {todo.isactive}
           </td>
       </tr>
   )
}


const TodoList = ({todos}) => {
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
               Isacitive
           </th>
           {todos.map((todo) => <TodoItem todo={todo} />)}
       </table>
   )
}


export default TodoList

