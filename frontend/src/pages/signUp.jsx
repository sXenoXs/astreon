import { Header } from "../components/header";
import {Footer} from "../components/footer"
export function SignUp(){
    return(
        <>
            <Header buttons={[{anchorText:"Login"}]} />  
            <Footer/>
        </>
    );

}