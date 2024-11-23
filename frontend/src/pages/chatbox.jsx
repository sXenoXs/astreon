import { Link } from 'react-router-dom';    
import { Header } from "../components/headerLoggedin";
import { Footer } from "../components/footer";
import "./chatbox.css";

export function ChatBox() {
  return (
    <div className="body">
      <Header />
      <div className="grid">
        <div className="sidebar">
          <p className="header">Astreon</p>
          <button className="sidebarbutton">
            <img
              className="sidebaricon"
              src="/Astreon/icon/AIStudyButton.png"
              alt="AI Study"
            />
            AI Study
          </button>
          <button className="sidebarbutton">
            <img
              className="sidebaricon"
              src="/Astreon/icon/quizmebutton.png"
              alt="Quiz Me"
            />
            Quiz Me
          </button>
          <button className="sidebarbutton">
            <img
              className="sidebaricon"
              src="/Astreon/icon/flashcardbutton.png"
              alt="Flashcards"
            />
            Flashcards
          </button>
          <button className="sidebarbutton">
            <img
              className="sidebaricon"
              src="/Astreon/icon/sessionsbutton.png"
              alt="Sessions"
            />
            Sessions
          </button>
          <button className="sidebarbutton">
            <img
              className="sidebaricon"
              src="/Astreon/icon/learnmodebutton.png"
              alt="Learning Modes"
            />
            Learning Modes
          </button>
          <div className="helpbuttonsdiv">
            <a className="helplink" href="#">
              <img
                className="helpbuttons"
                src="/Astreon/icon/helpbutton.png"
                alt="Help"
              />
              <p className="phelpbuttons">Help</p>
            </a>
          </div>
          <div className="helpbuttonsdiv">
            <a className="helplink" href="#">
              <img
                className="helpbuttons"
                src="/Astreon/icon/feedbackbutton.png"
                alt="Feedback"
              />
              <p className="phelpbuttons">Feedback</p>
            </a>
          </div>
        </div>

        <div className="chat-box">
          <div className="chat-bot-title">
            <i
              className="fa fa-chevron-left"
              style={{ fontSize: "24px", color: "#A1824A", marginTop: "3px" }}
            ></i>
            <div className="ai-chat">AI Chat</div>
          </div>
          <div className="astreon-chat-box">
            <img
              className="astreon"
              src="/Astreon/imgs/AstreonProfile.png"
              alt="Astreon"
            />
            <div>
              <div className="astreon2">Astreon</div>
              <div className="_9-03-am">9:03 AM</div>
              <div className="startphrase">
                Hi, I’m here to help you study. What would you like to learn
                today?
              </div>
            </div>
          </div>
          <div className="chatbox">
            <input
              className="userinput"
              type="text"
              placeholder="Type a message or upload a file/image..."
              id="userinput"
              name="userinput"
            />
            <button className="send">Send</button>
          </div>
          <div className="quick-response">
            <div className="aisuggestions">
              Share your question, and I’ll help you solve it!
            </div>
          </div>
        </div>
      </div>
      <Footer />
    </div>
  );
}
