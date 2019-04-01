<template>
    <div>
        <input v-model="login" type="text" placeholder="Логин">
        <input v-model="password" type="password" placeholder="Пароль">
        <button @click="setlogin">Войти</button>
    </div>
</template>

<script>
    import $ from 'jquery';
    import axios from 'axios';
    export default {
        name: "Login",
        data(){
            return{
                login:'',
                password:''
            }
        },
        methods:{
            setlogin(){
                $.ajax({
                    url: "http://127.0.0.1:8000/auth/token/create/",
                    type: "POST",
                    data: {
                        username: this.login,
                        password: this.password
                    },
                    success: (response) => {
                        alert("Спасибо что вы с нами")
                        sessionStorage.setItem("auth_token", response.data.attributes.auth_token)
                        // localStorage.setItem("auth_token", response.data.attributes.auth_token)
                        this.$router.push({name: "home"})
                    },
                    error: (response) =>{
                        if (response.status === 400){
                            alert("Логин или пароль не верен")
                        }
                    }
                })
            },
            setlogin2() {
                axios
                    .post("http://127.0.0.1:8000/auth/token/create/", {
                        headers: {
                            'Content-Type': 'application/x-www-form-urlencoded'
                        },
                        data: {
                            username: this.login,
                            password: this.password
                        }
                    })
                    .then(function(response){
                        alert("Спасибо что вы с нами");
                        sessionStorage.setItem("auth_token", response.data.attributes.auth_token);
                    })
                    .catch(function(error){
                        alert(error)
                    });
            }
        },
    }
</script>

<style scoped>

</style>
