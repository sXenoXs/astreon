import { useState } from 'react';
import { Link } from 'react-router-dom';
import { Header } from "../components/headerLoggedin";
import { Footer } from "../components/footer";
import "./quiz.css";
import "./sidebar.css";


export function Quiz() {
    const [sessions, setSessions] = useState([
        {
            id: 1,
            title: "AI Study",
            subject: "Math In the Modern World",
            percentage: 20
        },
        {
            id: 2,
            title: "Quiz Me",
            subject: "English Communication",
            percentage: 20
        },
        {
            id: 3,
            title: "Flashcards",
            subject: "Economical Transitions",
            percentage: 20
        },
        {
            id: 4,
            title: "Learning Modes",
            subject: "Dimensions of The Cybersecurity Cube",
            percentage: 20
        },
    ]);

    return (
        <div className="body">
            <Header />
            <div className="grid">
                <div className="sidebar">
                    <button className="sidebarbutton">
                        <img
                            className="sidebaricon"
                            src="./imgs/svgs/aichat.svg"
                            alt="AI Study"
                        />
                        AI Study
                    </button>
                    <button className="sidebarbutton">
                        <img
                            className="sidebaricon"
                            src="./imgs/svgs/quiz.svg"
                            alt="Quiz Me"
                        />
                        Quiz Me
                    </button>
                    <button className="sidebarbutton">
                        <img
                            className="sidebaricon"
                            src="./imgs/svgs/cards.svg"
                            alt="Flashcards"
                        />
                        Flashcards
                    </button>
                    <button className="sidebarbutton">
                        <img
                            className="sidebaricon"
                            src="./imgs/svgs/sessions.svg"
                            alt="Sessions"
                        />
                        Sessions
                    </button>
                    <button className="sidebarbutton">
                        <img
                            className="sidebaricon"
                            src="./imgs/svgs/learn_mode.svg"
                            alt="Learning Modes"
                        />
                        Learning Modes
                    </button>
                    <div className="helpbuttonsdiv">
                        <a className="helplink" href="#">
                            <img
                                className="helpbuttons"
                                src="./imgs/svgs/help.svg"
                                alt="Help"
                            />
                            <p className="phelpbuttons">Help</p>
                        </a>
                    </div>
                    <div className="helpbuttonsdiv">
                        <a className="helplink" href="#">
                            <img
                                className="helpbuttons"
                                src="./imgs/svgs/feedback.svg"
                                alt="Feedback"
                            />
                            <p className="phelpbuttons">Feedback</p>
                        </a>
                    </div>
                </div>

                <div className="chat-box">
                    <div className="chat-bot-title">
                        <div className="page-title">Quiz</div>
                        <hr />
                    </div>

                    <div className="session-main-div">

                    </div>
                </div>
            </div>
            <Footer />
        </div>
    );
}