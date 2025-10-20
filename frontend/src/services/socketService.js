import {w3cwebsocket as W3cwebsocket} from "websocket";
import {authService} from "./authService";

const baseURL = 'ws://localhost/api'
const socketService = async() => {
    const{data:{token}} = await authService.getSocketToken()
    return{
        chat:(room) => new W3cwebsocket(`${baseURL}/chat/${room}/?token=${token}`),
        pizzas:() => new W3cwebsocket(`${baseURL}/pizzas/?token=${token}`)
    }
}
export {
    socketService
}