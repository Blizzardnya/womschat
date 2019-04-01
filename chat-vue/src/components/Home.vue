<template>
    <div>
        <h1>Чат на vue.js</h1>
        <button v-if="!auth" @click="gologin">Вход</button>
        <button v-else @click="logout">Выход</button>
        <room v-if="auth"></room>
    </div>
</template>

<script>
    import Room from "./Room";

    export default {
        name: "Home",
        components: {Room},
        computed: {
            auth(){
                if (sessionStorage.getItem("auth_token")){
                    return true
                }
            }
        },
        methods: {
            gologin(){
                this.$router.push({name: "login"})
            },
            logout(){
                sessionStorage.removeItem("auth_token")
                window.location = '/'
            }
        }
    }
</script>

<style scoped>

</style>
