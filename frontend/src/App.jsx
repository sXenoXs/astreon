import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { ChatBox } from "./pages/chatbox.jsx";
import { Welcome } from "./pages/welcome.jsx";
import { Login } from "./pages/login.jsx";
import { SignUp } from "./pages/signUp.jsx";
import { Session } from "./pages/session.jsx"; 
import { Quiz } from "./pages/quiz.jsx";

function App() {
    return (
        <Router>
            <Routes>
                <Route path="/chatbox" element={<ChatBox />} />
                <Route path="/" element={<Welcome />} />
                <Route path="/login" element={<Login />} />
                <Route path="/sign-up" element={<SignUp />} />
                <Route path="/session" element={<Session />} />
                <Route path="/quizme" element={<Quiz />} />
            </Routes>
        </Router>
    );
}

export default App;
