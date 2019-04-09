<template>
    <DialogSlot>
        <mu-flex>
            <mu-col xl="6">
                <mu-select full-width v-model="options">
                    <mu-option v-for="user in list"
                               :label="user.username"
                               :value="user.id">
                        {{user.username}}
                    </mu-option>
                </mu-select>
            </mu-col>
            <mu-col xl="6">
                <mu-button full-width class="btn-send" small
                           color="success" @click="addUser">
                    Добавить пользователя
                </mu-button>
            </mu-col>
        </mu-flex>
    </DialogSlot>
</template>


<script>
    import DialogSlot from './Dialog'

    export default {
        name: "AddUsers",
        props: {
            id: ''
        },
        components: {DialogSlot},
        data() {
            return {
                options: '',
                list: ''
            }
        },
        created() {
             $.ajaxSetup({
                headers: {"Authorization": "token " + sessionStorage.getItem("auth_token")}
            });
            this.loadUsers()
        },
        methods: {
            loadUsers() {
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/chat/users/",
                    type: "GET",
                    data: {
                        id: this.$route.params.id
                    },
                    success: (response) => {
                        this.list = response.data.users
                    }
                })
            },
            addUser() {
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/chat/users/",
                    type: "POST",
                    data: {
                        room: this.$route.params.id,
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
