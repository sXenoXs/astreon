import { useState, useRef } from 'react';
import { Link } from 'react-router-dom';
import { Header } from "../components/headerLoggedin";
import { Footer } from "../components/footer";
import "./homepage.css";
import "./sidebar.css";

export function HomePage() {
        // Step 2: Define state for progress
        const [progress, setProgress] = useState({
            "Dimensions of The Cybersecurity Cube": 0,
            "History of Rizal": 0,
            "Math in the modern world": 0
        }); // Initial progress percentage
        
        // Step 3: Function to update progress
        const increaseProgress = (subject) => {
            setProgress(prev => ({ ...prev, [subject]: Math.min(prev[subject] + 10, 100) }));
        };
    return (
        <div className="body">
        <Header />
        <div className="grid">
            <div className="sidebar">
                <Link to="/chatbox" className="sidebarbutton">
                    <img
                        className="sidebaricon"
                        src="./imgs/svgs/aichat.svg"
                        alt="AI Study"
                    />
                    AI Study
                </Link>
                <Link to="/quizme" className="sidebarbutton">
                    <img
                        className="sidebaricon"
                        src="./imgs/svgs/quiz.svg"
                        alt="Quiz Me"
                    />
                    Quiz Me
                </Link>
                <Link to="/flashcards" className="sidebarbutton">
                    <img
                        className="sidebaricon"
                        src="./imgs/svgs/cards.svg"
                        alt="Flashcards"
                    />
                    Flashcards
                </Link>
                <Link to="/sessions" className="sidebarbutton">
                    <img
                        className="sidebaricon"
                        src="./imgs/svgs/sessions.svg"
                        alt="Sessions"
                    />
                    Sessions
                </Link>

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

            <div className="main-page-div">
                <div className="main-age-title-div">
                    <div className="page-title">Daily Progression</div>
                    <hr />
                </div>
                <div className="main-div-01">
                    
                </div>
                <div className="main-div-02">
                        <div className="page-title">Session Progression</div>
                        <br />
                        {Object.keys(progress).map((subject) => (
                            <div className="progress-bar-border" key={subject}>
                                
                                <div className="progression-bar-main">
                                    <div className="progression-bar" style={{ width: `${progress[subject]}%` }}>
                                        <span className="subject-title">{subject}</span>
                                        <button className="progress-bar">
                                            <div className="user-progress" style={{ width: `${progress[subject]}%`, backgroundColor: '#009963', borderRadius: '12px 0 0 12px' }}></div>
                                            <div className="user-not-progressed" style={{ width: `${100 - progress[subject]}%`, backgroundColor: 'rgba(0, 153, 99, 0.5)', borderRadius: '0 12px 12px 0' }}></div>
                                        </button>
                                        <span className="progress-bar-2">{progress[subject]}% </span>
                                        <div className="arrow-icon">
                                            <img
                                                 className="vector"
                                                src="./imgs/svgs/arrow-icon.svg"
                                                alt="nextbutton"
                                                />
                                            </div>
                                        
                                    </div>
                                    
                                    {/* Step 4: Add a button to increase progress */}
                                    <button onClick={() => increaseProgress(subject)}>Increase Progress</button>

                                </div>
                                
                            </div>
                        ))}
                    </div>
                </div>
            </div>
            <Footer />
        </div>
    );
}
