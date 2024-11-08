import { Button } from "../components/button";
import "./header.css"

export function Header(){
    return(
        
        <header className="header">
        <div className="brand_details">
          <img src="./imgs/Astreon.png" alt="Astreon Logo" />
          <span className="brand_details--name">Astreon Study Buddy</span>
        </div>
        <div className="btn_group">
          <Button anchorText="Login"></Button>
          <Button anchorText="Sign Up" bgColor="#F5F0E5" color="black"></Button>
        </div>
      </header>);

}