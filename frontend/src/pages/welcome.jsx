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
        <section className="hero_section">
          <h1 className="hero_section--heading">Get Instant Study Help</h1>
          <p className="hero_section--text">
            Upload your study materials and generate quizzes, flashcards, and
            more. Try it today!
          </p>
          <Button anchorText="Try it now" />
        </section>
      </main>
      <Footer />
    </>
  );
}
