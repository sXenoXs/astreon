import { Button } from "../components/button";
import { Header } from "../components/header";
import { Footer } from "../components/footer";
import "./signup.css";
export function SignUp() {
  return (
    <>
      <Header buttons={[{ anchorText: "Login", link: "/login" }]} />
      <form className="signup_form">
        <h2>Create an account</h2>
        <label htmlFor="name">Name</label>
        <input type="text" id="name" placeholder="Name" />

        <label htmlFor="Email">Email</label>
        <input type="email" id="email" placeholder="Email" />

        <label htmlFor="password">Password</label>
        <input type="password" id="password" placeholder="Password" />
        <div class="strength-meter">
          <div class="strength-bar"></div>
        </div>
        <p id="strength-text"></p>

        <label htmlFor="confirm_password">Confirm Password</label>
        <input
          type="password"
          id="confirm_password"
          placeholder="Confirm Password"
        />
        <div className="privacy_policy">
        <input type="checkbox" name="accept_policy" id="accept_policy" required/>
        <label>
        
          By creating an account, you agree to our Terms of Service and Privacy
          Policy.
        </label>
        </div>
        <div className="submit_sign_up">
          <Button anchorText="Sign Up"></Button>
        </div>
        
      
        
      </form>

      <Footer />
    </>
  );
<<<<<<< HEAD
}
=======
}
>>>>>>> feature/astreon-ai
