import {useEffect, useState} from "react";
import {pizzaService} from "../services/pizzaService";
import {PizzaComponent} from "./PizzaComponent";

const PizzasComponent = () => {
    const [pizzas, setPizzas ] = useState([])
    useEffect(()=>{
        pizzaService.getAll().then( ({data}) => setPizzas(data.data))
    }, [])
    return(
        <>
            {
                pizzas.map(pizza =><PizzaComponent key={pizza.id} pizza={pizza}/> )
            }
        </>
    )

}
export {PizzasComponent}