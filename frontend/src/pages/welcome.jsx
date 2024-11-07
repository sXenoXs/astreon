import { Button } from "../components/button";
export function Welcome() {
  return (
    <header className="header">
      <div className="brand_details">
        <img src="./imgs/Astreon.png" alt="" />
        <span>Astreon Study Buddy</span>
      </div>
      <div className="btn_group">
        <Button anchorText="Log In"></Button>
        <Button anchorText="Sign Up" bgColor="gray" color="white"></Button>
      </div>
    </header>
  );
}
