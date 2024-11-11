import "./button.css";
export function Button(props) {
  return (
    <a
      href={props.link || "#"}
      className="btn"
      style={{
        backgroundColor: props.bgColor || "#009963",
        color: props.color || "white",
      }}
    >
      {props.anchorText}
    </a>
  );
}
