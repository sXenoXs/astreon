import { useState } from 'react';
import { Link } from 'react-router-dom';
import { Header } from "../components/headerLoggedin";
import { Footer } from "../components/footer";
import "./chatbox.css";
import "./sidebar.css";


export function ChatBox() {
  const [isModalOpen, setIsModalOpen] = useState(false); // For file upload modal
  const [isImageModalOpen, setIsImageModalOpen] = useState(false); // For image upload modal

  const handleUploadClick = () => {
    setIsModalOpen(true); // Show file upload modal
  };

  const handleImageUploadClick = () => {
    setIsImageModalOpen(true); // Show image upload modal
  };

  const handleCloseModal = () => {
    setIsModalOpen(false); // Hide file upload modal
  };

  const handleCloseImageModal = () => {
    setIsImageModalOpen(false); // Hide image upload modal
  };

  const handleFileUpload = (event) => {
    const file = event.target.files[0];
    if (file) {
      // Handle the file upload logic here (e.g., send to server)
      console.log("File uploaded: ", file.name);
      setIsModalOpen(false); // Close modal after upload
    } else {
      alert("Please select a file.");
    }
  };

  const handleImageUpload = (event) => {
    const imageFile = event.target.files[0];
    if (imageFile) {
      // Handle the image upload logic here (e.g., send to server)
      console.log("Image uploaded: ", imageFile.name);
      setIsImageModalOpen(false); // Close modal after upload
    } else {
      alert("Please select an image.");
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
            <div className="ai-chat">AI Chat</div>
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
            </div>

            <div className="quick-response">
                <div className="aisuggestions">
                    Need lesson ideas? Tell me the topic!
                </div>
            </div>

            <div className="quick-response">
                <div className="aisuggestions">
                    Looking for resources? Ask me!
                </div>
            </div>

          </div>
          
        </div>
      </div>
      <Footer />
    </div>
  );
}