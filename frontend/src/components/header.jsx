import { Button } from "../components/button";
import { ButtonGroup } from "./buttonGroup";
import "./header.css"

export function Header({ buttons }){
    return(
        
        <header className="header">
        <div className="brand_details">
<<<<<<< HEAD
          <img src="./imgs/Astreon.png" alt="Astreon Logo" />
          <span className="brand_details--name">Astreon Study Buddy </span>
=======
          <img className="icon" src="../../imgs/astreon-icon.jpeg" alt="Astreon Logo" />
          <span className="brand_details--name">Astreon Study Buddy</span>
>>>>>>> feature/astreon-ai
        </div>
      
        <ButtonGroup buttons={buttons} />

      </header>);

}