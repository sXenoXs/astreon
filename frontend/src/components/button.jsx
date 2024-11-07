import "./button.css";
export function Button(props) {
  return (
    <a
      href={props.link || "#"}
      className="btn"
      style={{
        backgroundColor: props.bgColor || "green",
        color: props.color || "black",
      }}
    >
      {props.anchorText}
    </a>
  );
}
