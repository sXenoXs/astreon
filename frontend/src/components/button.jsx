import "./button.css";
export function Button(props) {
  return (
    <a
      href={props.link || "#"}
      className="btn"
<<<<<<< HEAD

      style={{
        backgroundColor: props.bgColor || "#009963",
        color: props.color || "white",
        
=======
      style={{
        backgroundColor: props.bgColor || "#009963",
        color: props.color || "white",
>>>>>>> feature/astreon-ai
      }}
    >
      {props.anchorText}
    </a>
  );
}
