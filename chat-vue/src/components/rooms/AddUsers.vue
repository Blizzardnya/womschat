<template>
    <div>
        <select v-model="options">
            <option v-for="user in list"
                    :value="user.id">
                {{user.username}}
            </option>
        </select>
        <mu-button class="btn-send" round
                   color="success" @click="addUser">
            Добвать пользователя
        </mu-button>
    </div>
</template>

<script>
    export default {
        name: "AddUsers",
        props: {
            room: ''
        },
        data (){
            return {
                options: '',
                list: ''
            }
        },
        created() {
            this.loadUsers()
        },
        methods: {
            loadUsers(){
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/chat/users/",
                    type: "GET",
                    success: (response) => {
                        this.list = response.data.users
                    }
                })
            },
            addUser(){
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/chat/users/",
                    type: "POST",
                    data: {
                        room: this.room,
                        user: parseInt(this.options)
                    },
                    success: (response) => {
                        alert('Пользователь добавлен')
                    },
                    error: (response) => {
                        alert('Ошибка добавления')
                    }
                })
            }
        }
    }
</script>

<style scoped>

</style>
