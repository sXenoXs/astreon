import { Button } from "../components/button";
import { Header } from "../components/header";
import { Footer } from "../components/footer";
import "./welcome.css";

export function Welcome() {
  return (
    <>
      <Header
        buttons={[
          { anchorText: "Login", link: "/login" },
          {
            anchorText: "Sign Up",
            link: "/sign-up",
            bgColor: "#F5F0E5",
            color: "black",
           
          },
        ]}
      />
      <main>
          
      </main>
      <Footer />
    </>
  );
}
