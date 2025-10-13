import {pizzaService} from "../services/pizzaService";
import {useForm} from "react-hook-form";


const PizzaForm = () =>{
    const {register, handleSubmit, reset} = useForm()
    const save = async (pizza) =>{
        await pizzaService.create(pizza)
    }
    return(
        <div>
            <form onSubmit={handleSubmit(save)}>
                <input type="text" placeholder={'name'} {...register('name')}/>
                <input type="text" placeholder={'name'} {...register('name')}/>
                <input type="text" placeholder={'name'} {...register('name')}/>
                <input type="text" placeholder={'name'} {...register('name')}/>
            </form>
        </div>
    )
}
export {
    PizzaForm
}