import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { Welcome } from "./pages/welcome.jsx";
import { Login } from "./pages/login.jsx";
import { SignUp } from "./pages/signUp.jsx";

function App() {
  return (
    
    <Router>
      <Routes>
        <Route path="/" element={<Welcome />} />
        <Route path="/login" element={<Login />} />
        <Route path="/sign-up" element={<SignUp />} />
      </Routes>
    </Router>);
}

export default App;

