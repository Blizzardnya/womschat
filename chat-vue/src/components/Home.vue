<template>
    <mu-container>
        <mu-appbar style="width: 100%;" color="primary">
            Чат на vue.js
            <!--<mu-button flat slot="right">LOGIN</mu-button>-->
            <mu-button flat slot="right" color="success" v-if="!auth" @click="gologin">Вход</mu-button>
            <mu-button flat slot="right" color="error" v-else @click="logout">Выход</mu-button>
        </mu-appbar>
        <!--<mu-row>-->
            <!--<Room v-if="auth" @openDialog="openDialog"></Room>-->
            <!--<Dialog v-if="dialog.show" :id="dialog.id"></Dialog>-->
        <!--</mu-row>-->
        <slot></slot>
    </mu-container>
</template>

<script>
    // import Room from "./rooms/Room";
    // import Dialog from "./rooms/Dialog";

    export default {
        name: "Home",
        // components: {Dialog, Room},
        data() {
            return {
                dialog: {
                    id: '',
                    show: false
                }
            }
        },
        computed: {
            auth() {
                if (sessionStorage.getItem("auth_token")) {
                    return true
                }
            }
        },
        methods: {
            gologin() {
                this.$router.push({name: "login"})
            },
            logout() {
                sessionStorage.removeItem("auth_token")
                window.location = '/'
            },
            // openDialog(id) {
            //     this.dialog.id = id
            //     this.dialog.show = true
            // }
        }
    }
</script>

<style scoped>

</style>
