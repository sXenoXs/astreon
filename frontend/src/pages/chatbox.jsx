import { useState } from 'react';
import { Link } from 'react-router-dom';
import { Header } from "../components/headerLoggedin";
import { Footer } from "../components/footer";
import "./chatbox.css";

export function ChatBox() {
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [isImageModalOpen, setIsImageModalOpen] = useState(false);
  const [message, setMessage] = useState('');
  const [files, setFiles] = useState([]);
  const [conversation, setConversation] = useState([
    { sender: 'ai', message: "Hi, I'm here to help you study. What would you like to learn today?" }
  ]);
  const [loading, setLoading] = useState(false);

  const handleUploadClick = () => setIsModalOpen(true);
  const handleImageUploadClick = () => setIsImageModalOpen(true);
  const handleCloseModal = () => setIsModalOpen(false);
  const handleCloseImageModal = () => setIsImageModalOpen(false);

  const handleFileUpload = (event) => {
    const uploadedFiles = Array.from(event.target.files) 
    setFiles(prevFiles => [...prevFiles, ...uploadedFiles]);
    setIsModalOpen(false);
  };

  const handleImageUpload = (event) => {
    const uploadedImages = Array.from(event.target.files)
    setFiles(prevFiles => [...prevFiles, ...uploadedImages]);
    setIsImageModalOpen(false);
  };

  const handleSendMessage = async () => {
    if (!message.trim() && files.length === 0) return; // Don't send if empty

    const formData = new FormData();
    formData.append('message', message); // Append the message

    // Append each file to the FormData object
    files.forEach((file) => {
        formData.append('files', file); // Append the actual file object
    });

    const userMessageEntry = { 
        sender: 'user', 
        message: message, 
        files: files.map(file => file.name) // Store only file names for local display
    };

    setConversation(prevConversation => [...prevConversation, userMessageEntry]);
    setLoading(true); // Show loading animation

    try {
        const response = await fetch('http://localhost:8000/api/chat/', {
            method: 'POST',
            body: formData, // Send FormData instead of JSON
        });

        const data = await response.json();
        if (response.ok) {
            // Add AI response to the conversation
            const aiMessageEntry = { sender: 'ai', message: data.text }; // Assuming the response structure has 'text'
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
<<<<<<< HEAD
              src="../../imgs/astreon-icon.jpeg"

              src="./imgs/astreonprofile.jpeg"
>>>>>>> a44927123e1f29c3ef7a6c0172f1d84b6d420796
              alt="Astreon"
            />
            <div>
              <div className="astreon2">Astreon</div>
              <div className="_9-03-am">9:03 AM</div>
            </div>
          </div>
<<<<<<< HEAD

         
          <div className="chat-messages">
    {conversation.map((msg, index) => (
        <div key={index} className={`message ${msg.sender === 'ai' ? 'ai-message' : 'user-message'}`}>
            <div className="message-content">
                <p>{msg.message}</p>
                {msg.files && msg.files.map((file, fileIndex) => (
                    <div key={fileIndex} className="uploaded-file">📄 {file}</div> // Render file names only
                ))}
=======
          <div className="chatbox">
            <input
              className="userinput"
              type="text"
              placeholder="Type a message or upload a file/image..."
              id="userinput"
              name="userinput"
            />
               <div className="main-container-imagefilesend">
                  <div className="image-file-send">
                    <div className="image-div">
                        <div className="image-div-1">
                          <img
                            className="uploadicon"
                            src="./imgs/svgs/upload_image.svg"
                            alt="Upload Image"
                            onClick={handleImageUploadClick} // Add click handler to open image upload modal
                          />
                        </div>

                          {/* Modal Structure for Image Upload */}
                          {isImageModalOpen && ( // Use a separate state for the image modal
                            <div id="imageUploadModal" className="modal">
                              <div className="modal-content">
                                <span className="close" onClick={handleCloseImageModal}>&times;</span>
                                <h2>Upload Image</h2>
                                <input type="file" accept="image/*" id="imageInput" onChange={handleImageUpload} />
                                <button onClick={handleCloseImageModal} className="uploadfilebutton">Upload</button> {/* Close modal after uploading */}
                              </div>
                      </div>
                    
                    )}
                    </div>
                  </div>
                    <div className="file-div">
                      <div className="files-div">
                        <img
                          className="uploadicon"
                          src="./imgs/svgs/upload_file.svg"
                          alt="Upload File"
                          id="uploadFileIcon"
                          onClick={handleUploadClick} // Add click handler to open modal
                        />

                        {/* Modal Structure */}
                        {isModalOpen && (
                          <div id="uploadModal" className="modal">
                            <div className="modal-content">
                              <span className="close" onClick={handleCloseModal} >&times;</span>
                              <h2>Upload File</h2>
                              <input type="file" id="fileInput" onChange={handleFileUpload} />
                              <button onClick={handleCloseModal} className="uploadfilebutton">Upload</button> {/* Close modal after uploading */}
                            </div>
                          </div>
                        )}
                      </div>
                    </div>
                    <div className="send-button">
                      <button className="send-button">Send</button>
                    </div>
                 
                </div>
       
          </div>
          <div className="grid-1">
            <div className="quick-response">
                <div className="aisuggestions">
                    Share your question, and I’ll help you solve it!
                </div>
 a44927123e1f29c3ef7a6c0172f1d84b6d420796
            </div>
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
                value={files}
                onChange={(e) => {handleImageChange(e)}}
            />
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
        </div>
        <div className="file-div">
            <img
                className="uploadicon"
                src="./imgs/svgs/upload_file.svg"
                alt="Upload File"
                onClick={handleUploadClick} // Opens the file upload modal
                value={files}
                onChange={(e) => setFiles(e.target.value)}
            />
                 {isModalOpen && (
                <div className="modal">
                  <div className="modal-content">
                    <span className="close" onClick={handleCloseModal}>&times;</span>
                    <h2>Upload File</h2>
                    <input type="file" id="fileInput" onChange={handleFileUpload} />
                    <button onClick={handleCloseModal} className="uploadfilebutton">Upload</button>
                  </div>
                </div>
              )}
        </div>
        <div className="send">
            <button className="send-button" onClick={handleSendMessage}>Send</button>
        </div>
</div> 
        </div>
      </div>
      <Footer />
    </div>
  );
}