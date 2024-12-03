import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { ChatBox } from "./pages/chatbox.jsx";
import { Welcome } from "./pages/welcome.jsx";
import { Login } from "./pages/login.jsx";
import { SignUp } from "./pages/signUp.jsx";
import { Session } from "./pages/session.jsx"; 
import { Quiz } from "./pages/quiz.jsx";
import { Calendar } from "./pages/calendar.jsx";
import { Flashcards } from "./pages/flashcards.jsx";
import { Profile } from "./pages/profile.jsx";



function App() {
    return (
        <Router>
            <Routes>
                <Route path="/chatbox" element={<ChatBox />} />
                <Route path="/" element={<Welcome />} />
                <Route path="/login" element={<Login />} />
                <Route path="/sign-up" element={<SignUp />} />
                <Route path="/sessions" element={<Session />} />
                <Route path="/quizme" element={<Quiz />} />
                <Route path="/calendar" element={<Calendar />} />
                <Route path="/flashcards" element={<Flashcards />} />
                <Route path="/profile" element={<Profile />} />

            </Routes>
        </Router>
    );
}

export default App;