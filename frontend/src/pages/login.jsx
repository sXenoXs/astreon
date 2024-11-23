import { Button } from "../components/button";
import { Header } from "../components/header";
import { Footer } from "../components/footer";
import "./login.css";
export function Login() {
  const googleIcon= `<svg width="20" height="20" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
<g clip-path="url(#clip0_98_371)">
<path fill-rule="evenodd" clip-rule="evenodd" d="M17.5 10C17.5002 13.6456 14.8788 16.7633 11.2873 17.3891C7.6958 18.0148 4.17452 15.9673 2.94178 12.5364C1.70905 9.10558 3.12197 5.28518 6.29043 3.48203C9.45889 1.67887 13.4651 2.41528 15.7852 5.22734C15.9371 5.3983 15.9835 5.6386 15.9062 5.85384C15.8289 6.06909 15.6401 6.22491 15.4141 6.26009C15.1881 6.29528 14.961 6.20421 14.8219 6.02266C12.9264 3.72439 9.67233 3.08336 7.04684 4.49105C4.42136 5.89874 3.15434 8.96382 4.01955 11.8145C4.88476 14.6651 7.64168 16.5089 10.6067 16.2198C13.5717 15.9307 15.9205 13.5891 16.2188 10.625H10C9.65482 10.625 9.375 10.3452 9.375 10C9.375 9.65482 9.65482 9.375 10 9.375H16.875C17.2202 9.375 17.5 9.65482 17.5 10Z" fill="#1C170D"/>
</g>
<defs>
<clipPath id="clip0_98_371">
<rect width="20" height="20" fill="white"/>
</clipPath>
</defs>
</svg>;
`
  return (
    <>
      <Header></Header>
      <main>
        <form className="login_form">
          <h2>Welcome back to Astreon Study Buddy</h2>
          <label htmlFor="username">Username</label>
          <input
            type="text"
            name="username"
            id="username"
            placeholder="Username"
          />
          <label htmlFor="username">Password</label>
          <input
            type="password"
            name="password"
            id="password"
            placeholder="Password"
          />
          <div className="checkboxes">
            
           
            <label htmlFor="remember_user"> <input type="checkbox" name="remember_user" id="remember_user" />     Remember Me</label>
            <a href="#" className="forgot_password">Forgot Password?</a>
          </div>
          <div className="submit_btns">
           <Button anchorText="Log in"/>
             <p>Or</p>
            <Button anchorText="G Continue With Google" color="black" bgColor="#f5f0e5"/>
            <p>Don't have an account?</p>
            <a href="/sign-up" className="signup_btn">Sign Up</a>
          </div>

        </form>
      </main>
      <Footer></Footer>
    </>
  );
}