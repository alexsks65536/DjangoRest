import React from 'react'
import { useParams } from 'react-router-dom'


const BookItem = ({item}) => {
    return (
        <tr>
            <td>{item.id}</td>
            <td>{item.name}</td>
            <td>{item.repository}</td>
        </tr>
    )
}
const BookList = ({items}) => {
    let { id } = useParams();
    let filtered_items = items.filter((item) => items.project.id == id)
    return (
        <table>
            <tr>
                <th>ID</th>
                <th>NAME</th>
                <th>REPOSITORY</th>
            </tr>
            {filtered_items.map((item) => <BookItem item={item} />)}
        </table>
    )
}
export default BookList