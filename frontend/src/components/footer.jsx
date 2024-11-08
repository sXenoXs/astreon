import "./footer.css"
export function Footer(){
    return (
        <footer className="footer">
            <div className="footer_links">
               <a href="#">About</a>
               <a href="#">Careers</a>
               <a href="#">Blog</a>
               <a href="#">Help Center</a>
            
            </div>
            <p className="copyright_statement">
                @ 2024 <span>Astreon Study Buddy</span> 
            </p>
        </footer>
    );
}