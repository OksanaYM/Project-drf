import {PizzasComponent} from "../components/PizzasComponent";
import {PizzaForm} from "../components/PizzaForm";
import {Chat} from "../components/Chat";

const PizzasPage = () => {
    return(
        <>
            <PizzaForm/>
            <hr/>
            <PizzasComponent/>
            <hr/>
            <Chat/>
        </>
    )

}
export {PizzasPage}