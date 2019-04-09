<template>
    <mu-container>
         <mu-alert color="error" @delete="errorAlert = false" delete v-if="errorAlert" transition="mu-scale-transition">
             Пароль введён неверно
         </mu-alert>
        <mu-form ref="form" :model="formVal">
            <mu-form-item label="Логин">
                <mu-text-field v-model="formVal.username" type="text"></mu-text-field>
            </mu-form-item>
            <mu-form-item label="Пароль">
                <mu-text-field v-model="formVal.password" type="password"></mu-text-field>
            </mu-form-item>
            <mu-form-item >
                <mu-button color="success" @click="setlogin">Войти</mu-button>
            </mu-form-item>
        </mu-form>
    </mu-container>
</template>

<script>
    export default {
        name: "Login",
        data(){
            return{
                formVal: {
                    username: '',
                    password: ''
                },
                errorAlert: false
            }
        },
        methods:{
            setlogin(){
                $.ajax({
                    url: "http://127.0.0.1:8000/auth/token/create/",
                    type: "POST",
                    data: {
                        username: this.formVal.username,
                        password: this.formVal.password
                    },
                    success: (response) => {
                        // alert("Спасибо что вы с нами")
                        sessionStorage.setItem("auth_token", response.data.attributes.auth_token)
                        this.$router.push({name: "room"})
                    },
                    error: (response) =>{
                        console.log(response)
                        if (response.status === 400){
                            this.errorAlert = true
                            // alert("Логин или пароль не верен")
                        }
                    }
                })
            },
        },
    }
</script>

<style scoped>

</style>
