import React from 'react'


const UserItem = ({user}) => {
    return (
        <tr>
            <td>
               {user.id}
            </td>
            <td>
               {user.username}
            </td>
            <td>
               {user.firstname}
            </td>
            <td>
               {user.lastname}
            </td>
            <td>
               {user.email}
            </td>
        </tr>
    )
}


const UserList = ({users}) => {
   return (
       <table>
            <th>
               id
            </th>
            <th>
               User Name
            </th>
            <th>
               First Name
            </th>
            <th>
               Last Name
            </th>
            <th>
               eMail
            </th>
            {users.map((user) => <UserItem user={user} />)}
       </table>
   )
}


export default UserList
