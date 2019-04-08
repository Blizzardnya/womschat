<template>
    <HomeSlot>
        <mu-row>
            <mu-col span="4" xl="2">
                <mu-button color="success" full-width @click="addRoom">Создать комнату</mu-button>
                <mu-paper :z-depth="2">
                    <div v-for="room in rooms">
                        <h3 @click="openDialog(room.id)">{{room.creator.username}}</h3>
                        <small>{{room.date}}</small>
                        <mu-divider></mu-divider>
                    </div>
                </mu-paper>
            </mu-col>
            <slot></slot>
        </mu-row>
    </HomeSlot>
</template>

<script>
    import HomeSlot from '../Home'

    export default {
        name: "Room",
        components: {HomeSlot},
        data() {
            return {
                rooms: '',
            }
        },
        created() {
            if (sessionStorage.getItem("auth_token")) {
                $.ajaxSetup({
                    headers: {"Authorization": "token " + sessionStorage.getItem("auth_token")}
                });
                this.loadRoom()
            }
        },
        methods: {
            loadRoom() {
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/chat/room/",
                    type: "GET",
                    success: (response) => {
                        this.rooms = response.data.data
                    }
                })
            },
            openDialog(id) {
                // this.$emit("openDialog", id)
                this.$router.push({name: 'dialog', params: {id: id}})
            },
            addRoom() {
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/chat/room/",
                    type: "POST",
                    success: (response) => {
                        this.loadRoom()
                    },
                    error: (response) => {
                        alert(response.statusText)
                    }
                })
            }
        }
    }
</script>

<style scoped>
    h3 {
        cursor: pointer;
    }
</style>
