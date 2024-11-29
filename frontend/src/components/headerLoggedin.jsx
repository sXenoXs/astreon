import { Button } from "../components/button";
import { ButtonGroup } from "./buttonGroup";
import "./headerLoggedin.css";

export function Header({ buttons }) {
    return (
        <header>
            <div className="Headercontainer">
                <div className="titleheader">
<<<<<<< HEAD
                    <img className="logo" src="./imgs/Astreon.png" alt="Astreon Logo" />
=======
>>>>>>> feature/astreon-ai
                    <p className="header">Astreon Study Buddy</p>
                </div>
                <div className="logindiv">
                    <input className="SearchButton" type="text" placeholder="Search" id="search" name="search" />
                    <button className="sessionbutton">New Study Session</button>
<<<<<<< HEAD
                    <a href="#"><img className="icon" src="./imgs/notification.png" alt="Notification" /></a>
                    <a href="#"><img className="icon" src="./imgs/calendar.png" alt="Calendar" /></a>
                    <a href="#"><img className="profile" src="./imgs/profile.png" alt="Profile" /></a>
                </div>
            </div>
            <hr></hr>
=======
                    <a href="#"><img className="iconButton" src="./imgs/svgs/notification.svg" alt="Notification" /></a>
                    <a href="#"><img className="iconButton" src="./imgs/svgs/calendar.svg" alt="Calendar" /></a>
                    <a href="#"><img className="profile" src="./imgs/profile.png" alt="Profile" /></a>
                </div>
            </div>
            <hr className="header-hr"></hr>
>>>>>>> feature/astreon-ai
        </header>
    );
}