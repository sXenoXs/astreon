import { useState } from 'react';
import { Header } from "../components/headerLoggedin";
import { Footer } from "../components/footer";
import ReactMarkdown from 'react-markdown';
import remarkGfm from 'remark-gfm'; // For GitHub Flavored Markdown support (links, tables, etc.)
import rehypeRaw from 'rehype-raw'; 
import "./chatbox.css";

export function ChatBox() {
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [isImageModalOpen, setIsImageModalOpen] = useState(false);
  const [isFileUploadModalOpen, setIsFileUploadModalOpen] = useState(false); // Fix: Add this state
  const [message, setMessage] = useState('');
  const [files, setFiles] = useState([]);
  const [conversation, setConversation] = useState([
    { sender: 'ai', message: "Hi, I'm here to help you study. What would you like to learn today?" }
  ]);
  const [loading, setLoading] = useState(false);

  function renderMessageContent(message) {
    return (
      <ReactMarkdown
        remarkPlugins={[remarkGfm]}
        rehypePlugins={[rehypeRaw]} // This allows HTML inside markdown
        components={{
          p: ({ children }) => <>{children}</> // Override the paragraph component to not wrap in <p> tags
        }}
      >
        {message}
      </ReactMarkdown>
    ); 
  }

  function RenderMessage({ msg }) {
    return (
      <div className="message-content">
        {renderMessageContent(msg.message)}
        {msg.files && msg.files.map((file, fileIndex) => (
          <div key={fileIndex} className="uploaded-file">📄 {file}</div>
        ))}
      </div>
    );
  }

  const handleFileUploadClick = () => setIsFileUploadModalOpen(true); // Fix: toggle file upload modal
  const handleImageUploadClick = () => setIsImageModalOpen(true);
  const handleCloseModal = () => setIsModalOpen(false);
  const handleCloseImageModal = () => setIsImageModalOpen(false);
  const handleCloseFileModal = () => setIsFileUploadModalOpen(false); // Fix: close file upload modal

  const handleFileUpload = (event) => {
    const uploadedFiles = Array.from(event.target.files); 
    setFiles(prevFiles => [...prevFiles, ...uploadedFiles]);
    setIsModalOpen(false);
  };

  const handleImageUpload = (event) => {
    const uploadedImages = Array.from(event.target.files);
    setFiles(prevFiles => [...prevFiles, ...uploadedImages]);
    setIsImageModalOpen(false);
  };

  const handleSendMessage = async () => {
    if (!message.trim() && files.length === 0) return; // check if there is user input

    const formData = new FormData();
    formData.append('message', message); // Append the message

    // Append each file to the FormData object
    files.forEach((file) => {
        formData.append('files', file); //Append file object (returns non-file object from rest) 
    });

    const userMessageEntry = { 
        sender: 'user', 
        message: message, 
        files: files.map(file => file.name) // Store only file names for local display
    };

    setConversation(prevConversation => [...prevConversation, userMessageEntry]);
    setLoading(true); // Show loading animation

    

    const token = localStorage.getItem('authToken')
    console.log(token)
    try {
        const response = await fetch('http://localhost:8000/api/chat/', {
            method: 'POST',
            headers:{
              'Authorization': `Token ${token}`,
            },
            body: formData,
        });

        const data = await response.json();
        if (response.ok) {
            //fetch response 
            const aiMessageEntry = { sender: 'ai', message: data.text }; 
            setConversation(prevConversation => [...prevConversation, aiMessageEntry]);
            setMessage(''); 
            setFiles([]); 
        } else {
            setConversation(prevConversation => [
                ...prevConversation,
                { sender: 'ai', message: 'Sorry, there was an error processing your request.' }
            ]);
        }
    } catch (error) {
        console.error('Error:', error);
        setConversation(prevConversation => [
            ...prevConversation,
            { sender: 'ai', message: 'An error occurred. Please try again.' }
        ]);
    } finally {
        setLoading(false); 
    }
}; 

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
          <i
            className="fa fa-chevron-left"
            style={{ fontSize: "24px", color: "#A1824A", marginTop: "3px" }}
          ></i>
        </div>
        <div className="astreon-chat-box">
          <img
            className="astreon"
            src="./imgs/astreonprofile.jpeg"
            alt="Astreon"
          />
          <div>
            <div className="astreon2">Astreon</div>
            <div className="_9-03-am">9:03 AM</div>
          </div>
        </div>

        <div className="chat-messages">
          {conversation.map((msg, index) => (
              <div key={index} className={`message ${msg.sender === 'ai' ? 'ai-message' : 'user-message'}`}>
                  <RenderMessage msg={msg} />
              </div>
          ))} 
        
          {loading && <div className="loader"></div>}
        </div>

        <div className="chat-input-container">
            <input
                className="userinput"
                type="text"
                placeholder="Type a message or upload a file/image..."
                id="userinput"
                name="userinput"
                value={message}
                onChange={(e) => setMessage(e.target.value)}
            />
            <div className="image-file-send">
                <img
                    className="uploadicon"
                    src="./imgs/svgs/upload_image.svg"
                    alt="Upload Image"
                    onClick={handleImageUploadClick} 
                />
            </div>

            {isImageModalOpen && (
                <div className="modal">
                  <div className="modal-content">
                    <span className="close" onClick={handleCloseImageModal}>&times;</span>
                    <h2>Upload Image</h2>
                    <input type="file" accept="image/*" onChange={handleImageUpload} />
                    <button onClick={handleCloseImageModal} className="uploadfilebutton">Upload</button>
                  </div>
                </div>
            )}

            {/* Fix: File upload modal */}
            <div className="file-upload-container">
                <img
                    className="uploadicon"
                    src="./imgs/svgs/upload_file.svg"
                    alt="Upload File"
                    onClick={handleFileUploadClick}
                />
            </div>
        <button className="send-button" onClick={handleSendMessage}>
          Send
        </button>
            {isFileUploadModalOpen && (
                <div className="modal">
                    <div className="modal-content">
                        <span className="close" onClick={handleCloseFileModal}>&times;</span>
                        <h2>Upload Files</h2>
                        <input type="file" multiple accept=".txt, .pdf, .doc, .docx, .csv, .pptx" onChange={handleFileUpload} />
                        <button onClick={handleCloseFileModal} className="uploadfilebutton">Upload</button>
                    </div>
                </div>
            )}
        </div>

      </div>
    </div>
    <Footer />
  </div>
);
} 
