import { Button } from "../components/button";
import { Header } from "../components/header";
import { Footer } from "../components/footer";
import { useState } from "react";
import "./login.css";

// Function to get CSRF token from the cookies
async function fetchCSRFToken(){
  const response = await fetch('http://127.0.0.1:8000/api/csrf/', {
    credentials: 'include',
  });
  const data = await response.json();
  return data.csrfToken;
}

export function Login() {
  const [formData, setFormData] = useState({
    usernameOrEmail: "",
    password: "",
    remember_user: false
  });

  const [error, setError] = useState(null);

  const handleChange = (e) => {
    const { id, type, checked, value } = e.target;
    setFormData({
      ...formData,
      [id]: type === 'checkbox' ? checked : value
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError(null);

    // Get the CSRF token asynchronously
    const csrfToken = await fetchCSRFToken();

    try {
      // POST the login request with CSRF token
      const response = await fetch('http://127.0.0.1:8000/api/dj-rest-auth/login/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',  // Use 'application/json' for JSON data
          'X-CSRFToken': csrfToken,  // Include the CSRF token in the header
        },
        credentials: 'include',  // Ensure cookies (including CSRF) are sent
        body: JSON.stringify({
          username: formData.usernameOrEmail,
          password: formData.password,
          remember: formData.remember_user,
        })
      });

      

      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(
          errorData.non_field_errors?.[0] || 
          errorData.detail || 
          'Login failed. Please check your credentials.'
        );
      }else{
        const data = await response.json();
        localStorage.setItem('authToken', data.token);
        window.location.href = '/chatbox'; // Redirect to the chatbox  page after successful login
      }

  } catch (err) {
    console.error('Login error:', err);
    setError(err.message); // Display the error message on failure
  }
};
  return (
    <>
      <Header />
      <main>
        <form className="login_form" onSubmit={handleSubmit}>
          <h2>Welcome back to Astreon Study Buddy</h2>
          {error && <p style={{ color: "red" }}>{error}</p>}

          <label htmlFor="usernameOrEmail">Username or Email</label>
          <input
            type="text"
            name="usernameOrEmail"
            id="usernameOrEmail"
            placeholder="Username or Email"
            value={formData.usernameOrEmail}
            onChange={handleChange}
            required
          />

          <label htmlFor="password">Password</label>
          <input
            type="password"
            name="password"
            id="password"
            placeholder="Password"
            value={formData.password}
            onChange={handleChange}
            required
          />

          <div className="checkboxes">
            <label htmlFor="remember_user">
              <input
                type="checkbox"
                name="remember_user"
                id="remember_user"
                checked={formData.remember_user}
                onChange={handleChange}
              />
              Remember Me
            </label>
            <a href="/forgot-password" className="forgot_password">Forgot Password?</a>
          </div>

          <div className="submit_btns">
            <button type="submit">Log In</button>
            <p>Or</p>
            <Button
              anchorText="Continue With Google"
              color="black"
              bgColor="#f5f0e5"
            />
            <p>Don't have an account?</p>
            <a href="/sign-up" className="signup_btn">Sign Up</a>
          </div>
        </form>
      </main>
      <Footer />
    </>
  );
}
