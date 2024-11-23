import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { ChatBox } from "./pages/chatbox.jsx";
import { Welcome } from "./pages/welcome.jsx";
import { Login } from "./pages/login.jsx";
import { SignUp } from "./pages/signUp.jsx";



function App() {
 
  return (
    
    <Router>
      <Routes>
        <Route path="/chatbox" element={<ChatBox />} />
        <Route path="/" element={<Welcome />} />
        <Route path="/login" element={<Login />} />
        <Route path="/sign-up" element={<SignUp />} />

        
      </Routes>
    </Router>);
}

export default App;
