import React from 'react'


const UserItem = ({item}) => {
    return (
        <tr>
            <td>
               {item.id}
            </td>
            <td>
               {item.username}
            </td>
            <td>
               {item.firstname}
            </td>
            <td>
               {item.lastname}
            </td>
            <td>
               {item.email}
            </td>
        </tr>
    )
}


const UserList = ({items}) => {
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
            {items.map((item) => <UserItem item={item} />)}
       </table>
   )
}


export default UserList
