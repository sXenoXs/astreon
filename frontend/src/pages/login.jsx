import { Header } from "../components/header";
import {Footer} from "../components/footer"
import "./login.css"
export function Login(){
 return(
    <>
        <Header></Header>
        <main>
          
            <form className="login_form">
            <h2>Welcome back to Astreon Study Buddy</h2>
                <label htmlFor="username">Username</label>
                <input type="text" name="username" id="username" placeholder="Username"/>
                <label htmlFor="username">Password</label>
                <input type="password" name="password" id="password" placeholder="Password"/>
            </form>
        </main>
        <Footer></Footer>
    
    </>
 )
}