
import { Button } from "../components/button";
import { ButtonGroup } from "./buttonGroup";
import { Link } from 'react-router-dom';
import "./headerLoggedin.css";

export function Header({ buttons }) {
    return (
        <header>
            <div className="Headercontainer">
                <div className="titleheader">
                    <h1 className="header">Astreon Study Buddy</h1>
                </div>
                <div className="logindiv">
                   
                    <button className="sessionbutton">New Study Session</button>
                   
                    <Link to="/notification">
                    <div className="headerBox">
                       
                            <img 
                                className="iconButton" 
                                src="./imgs/svgs/notification.svg" 
                                alt="Notification" 
                                title="Notification"
                            />
                       
                    </div>
                    </Link>
                        <Link to="/calendar">
                        <div  className="headerBox">
                            <a href="#">
                                <img 
                                    className="iconButton" 
                                    src="./imgs/svgs/calendar.svg" 
                                    alt="Calendar" 
                                    title="Calendar"
                                />
                            </a>
                        </div>
                        </Link>


                    <Link to="/profile">
                        <img 
                            className="profile" 
                            src="./imgs/profile.png" 
                            alt="Profile" 
                            title="Profile"
                        />
                    </Link>
                </div>
            </div>
            <hr className="header-hr"></hr>
        </header>
    );
}