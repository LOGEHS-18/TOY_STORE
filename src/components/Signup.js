import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { Link } from 'react-router-dom';
import 'bootstrap/dist/css/bootstrap.min.css';
import { toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';

function Signup() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const navigate = useNavigate();

  const handleSignup = async (e) => {
    e.preventDefault();
    try {
      const response = await fetch('http://localhost:8000/api/mymodels/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ email, password })
      });
      if (response.ok) {
        navigate('/login');
        toast.success('Signed up successfully! You can log in now!');
      } else {
        toast.error('Error during signup');
      }
    } catch (error) {
      toast.error('Error during signup:', error);
    }
  };

  return (
    <div className="container-fluid vh-100">
      <div className="row h-100">
        <div className="col-md-6 d-flex align-items-center justify-content-center">
          <div className="card p-4" style={{ width: '80%' }}>
            <h2 className="text-center">Signup</h2>
            <form onSubmit={handleSignup}>
              <div className="form-group row">
                <label htmlFor="email" className="col-sm-3 col-form-label">Email</label>
                <div className="col-sm-9">
                  <input
                    type="email"
                    className="form-control"
                    id="email"
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                    required
                  />
                </div>
              </div>
              <div className="form-group row">
                <label htmlFor="password" className="col-sm-3 col-form-label">Password</label>
                <div className="col-sm-9">
                  <input
                    type="password"
                    className="form-control"
                    id="password"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                    required
                  />
                </div>
              </div>
              <div className="text-center">
                <button type="submit" className="btn btn-primary">Signup</button>
                <br /><br />
                <Link to="/login" className="btn btn-link">Already have an account?</Link>
              </div>
            </form>
          </div>
        </div>
        <div className="col-md-6 d-none d-md-flex align-items-center justify-content-center" style={{ background: 'url("https://okplay.in/wp-content/uploads/2023/10/Best-baby-toys-in-2023-scaled.jpg") no-repeat center center', backgroundSize: 'cover' }}>
        </div>
      </div>
    </div>
  );
}

export default Signup;
