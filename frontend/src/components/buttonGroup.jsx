import { Button } from "../components/button";

export function ButtonGroup({ buttons = [] }) {
    return (
        <div className="btn_group">
            {buttons.map((button, index) => (
                <Button
                    key={index}
                    anchorText={button.anchorText}
                    link={button.link}
                    bgColor={button.bgColor}
                    color={button.color}
                    
                />
            ))}
        </div>
    );
}