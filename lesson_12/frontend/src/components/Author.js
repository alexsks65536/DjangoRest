import React from 'react'


const AuthorItem = ({item}) => {
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


const AuthorList = ({items}) => {
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
            {items.map((item) => <AuthorItem item={item} />)}
       </table>
   )
}


export default AuthorList
