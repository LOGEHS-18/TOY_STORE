import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { toast, ToastContainer } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';
import Navbar from './Navbar';
const UsersPage = () => {
  const [users, setUsers] = useState([]);
  const [newUser, setNewUser] = useState({ email: '', password: '' });
  const [editUser, setEditUser] = useState(null);

  useEffect(() => {
    axios.get('http://localhost:5000/users')
      .then(response => setUsers(response.data))
      .catch(error => console.error('Error fetching users:', error));
  }, []);

  const handleAddUser = () => {
    axios.post('http://localhost:5000/users', newUser)
      .then(response => {
        setUsers([...users, response.data]);
        setNewUser({ email: '', password: '' });
        toast.success('User Added successfully!');
      })
      .catch(error => console.error('Error adding user:', error));
  };

  const handleEditUser = (user) => {
    setEditUser(user);
    setNewUser({ email: user.email, password: user.password });
  };

  const handleSaveEdit = () => {
    axios.put(`http://localhost:5000/users/${editUser.id}`, newUser)
      .then(response => {
        const updatedUsers = users.map(user =>
          user.id === editUser.id ? response.data : user
        );
        setUsers(updatedUsers);
        setEditUser(null);
        setNewUser({ email: '', password: '' });
        toast.success('Updated successfully!');
      })
      .catch(error => console.error('Error updating user:', error));
  };

  const handleDeleteUser = (id) => {
    axios.delete(`http://localhost:5000/users/${id}`)
      .then(() => {
        setUsers(users.filter(user => user.id !== id));
        toast.success('User Deleted successfully!');
      })
      .catch(error => console.error('Error deleting user:', error));
  };

  return (
    <div>
      <Navbar/>
      <h2>Users</h2>
      <div className="mb-3">
        <input
          type="email"
          placeholder="Email"
          value={newUser.email}
          onChange={(e) => setNewUser({ ...newUser, email: e.target.value })}
        />
        <input
          type="password"
          placeholder="Password"
          value={newUser.password}
          onChange={(e) => setNewUser({ ...newUser, password: e.target.value })}
        />
        {editUser ? (
          <button onClick={handleSaveEdit} className="btn btn-success">Save Edit</button>
        ) : (
          <button onClick={handleAddUser} className="btn btn-primary">Add User</button>
        )}
      </div>
      <table className="table">
        <thead>
          <tr>
            <th>ID</th>
            <th>Email</th>
            <th>Password</th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>
          {users.map(user => (
            <tr key={user.id}>
              <td>{user.id}</td>
              <td>{user.email}</td>
              <td>{user.password}</td>
              <td>
                <button onClick={() => handleEditUser(user)} className="btn btn-warning">Edit</button>
                <button onClick={() => handleDeleteUser(user.id)} className="btn btn-danger">Delete</button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default UsersPage;
