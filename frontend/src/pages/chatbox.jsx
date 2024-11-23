import { Link } from 'react-router-dom';    
import { Button } from "../components/button";
import { Header } from "../components/headerLoggedin";
import { Footer } from "../components/footer";

import "./chatbox.css";
import React from 'react';

export const ChatBox = () => {
    return (
        <div className="body">
        <Header/>
        <div className="grid">
        <div class="body">
        <div class="grid">
            <div class="sidebar">
                <p class="header">Astreon</p>
                <button class="sidebarbutton"><img class="sidebaricon" src="/Astreon/icon/AIStudyButton.png"/>AI Study</button>
                <button class="sidebarbutton"><img class="sidebaricon" src="/Astreon/icon/quizmebutton.png"/>Quiz Me</button>
                <button class="sidebarbutton"><img class="sidebaricon" src="/Astreon/icon/flashcardbutton.png"/>Flashcards</button>
                <button class="sidebarbutton"><img class="sidebaricon" src="/Astreon/icon/sessionsbutton.png"/>Sessions</button>
                <button class="sidebarbutton"><img class="sidebaricon" src="/Astreon/icon/learnmodebutton.png"/>Learning modes</button>
                <div class="helpbuttonsdiv">
                    <a class="helplink" href=""><img class ="helpbuttons" src="/Astreon/icon/helpbutton.png"/> <p class="phelpbuttons">Help</p></a>
                </div>
                <div class="helpbuttonsdiv">
                    <a class="helplink" href=""><img class ="helpbuttons" src="/Astreon/icon/feedbackbutton.png"/> <p class="phelpbuttons">Feedback</p></a>
                </div>
                
     
            </div>
                
            <div class="chat-box">
        <div class="chat-bot-title">
            <div class="depth-3-frame-0">
                <i class="fa fa-chevron-left" style="font-size:24px; color: #A1824A; margin-top:3px"></i>
            <div class="depth-4-frame-0"></div>
            </div>
            <div class="depth-5-frame-0">
            <div class="ai-chat">AI chat</div>
            </div>
        </div>
        <div class="astreon-chat-box">
            <img class="astreon" src="/Astreon/imgs/AstreonProfile.png" />
            <div class="depth-5-frame-1">
            <div class="depth-6-frame-0">
                <div class="depth-7-frame-0">
                <div class="depth-8-frame-0">
                    <div class="astreon2">Astreon</div>
                </div>
                <div class="depth-8-frame-1">
                    <div class="_9-03-am">9:03 AM</div>
                </div>
                </div>
                <div class="depth-7-frame-1">
                <div
                    class="startphrase"
                >
                    Hi, I&#039;m here to help you study. What would you like to learn
                    today?
                </div>
                </div>
            </div>
            </div>
        </div>
        <div class="chatbox">
            <div class="depth-5-frame-02">
            <div class="depth-6-frame-02">
                <input class="userinput" type="text" placeholder="Type a message or upload a file/image..." id="userinput" name="userinput"/>
                <div class="depth-7-frame-12">
                <div class="depth-8-frame-02">
                    <div class="depth-9-frame-2">
                        <div class="depth-10-frame-0">
                        <div class="depth-11-frame-02">
                            <div class="depth-12-frame-0">
                            <a href=""><img class="vector-0" src="/Astreon/icon/imguploadicon.png"/></a>
                            <div class="depth-13-frame-0"></div>
                            </div>
                        </div>
                        </div>
                    </div>
                    <div class="depth-9-frame-2">
                    <div class="depth-10-frame-0">
                        <div class="depth-11-frame-02">
                        <div class="depth-12-frame-0">
                            <a href=""><img class="vector-0" src="/Astreon/icon/fileuploadicon.png"/></a>
                            <div class="depth-13-frame-0"></div>
                        </div>
                        </div>
                    </div>
                    </div>
                    <button class="send">Send</button>
                </div>
                </div>
            </div>
            </div>
        </div>
        <div class="quick-response">
            <div class="depth-5-frame-03">
            <div class="depth-6-frame-02">
                <div class="depth-7-frame-03">
                <div class="aisuggestions">
                    Share your question, and I’ll help you solve it!
                </div>
                </div>
            </div>
            </div>
            <div class="icon2">
            <img class="guidance-study-room" src="/Astreon/icon/shareai.png" />
            <div class="depth-9-frame-02"></div>
            </div>
        </div>
        <div class="quick-response-2">
            <div class="depth-5-frame-04">
            <div class="depth-6-frame-02">
                <div class="depth-7-frame-03">
                <div class="aisuggestions">
                    Need lesson ideas? Tell me the topic!
                </div>
                </div>
            </div>
            </div>
            <div class="icon2">
            <img class="mdi-teacher" src="/Astreon/icon/ideasai.png" />
            </div>
        </div>
        <div class="quick-response-3">
            <div class="depth-5-frame-04">
            <div class="depth-6-frame-02">
                <div class="depth-7-frame-03">
                <div class="aisuggestions">
                    Looking for resources? Ask me!
                </div>
                </div>
            </div>
            </div>
            <div class="icon2">
            <div class="icon3">
                <img
                class="grommet-icons-resources"
                src="/Astreon/icon/resourcesai.png"
                />
            </div>
            </div>
        </div>
        </div>                        
        
            </div>
        
    </div>
        </div>
        <Footer />
    </div>
    );
};

