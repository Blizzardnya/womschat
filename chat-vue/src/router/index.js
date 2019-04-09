import Vue from 'vue'
import Router from 'vue-router'

import Home from '@/components/Home'
import Login from '@/components/Login'
import Room from "../components/rooms/Room";
import Dialog from "../components/rooms/Dialog";
import AddUser from "../components/rooms/AddUsers"

Vue.use(Router)

export default new Router({
    mode: 'history',
    routes: [
        {
            path: '/',
            name: 'room',
            component: Room
        },
        {
            path: '/login',
            name: 'login',
            component: Login
        },
        {
            path: '/dialog/:id',
            name: 'dialog',
            component: Dialog
        },
        {
            path: '/users/:id',
            name: 'addUser',
            component: AddUser
        }
    ]
})
