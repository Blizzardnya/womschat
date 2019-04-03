<template>
    <mu-col span="4" xl="2">
        <mu-paper :z-depth="2">
            <div v-for="room in rooms">
                <h3 @click="openDialog(room.id)">{{room.creator.username}}</h3>
                <small>{{room.date}}</small>
                <mu-divider></mu-divider>
            </div>
        </mu-paper>
    </mu-col>
</template>

<script>
    export default {
        name: "Room",
        data(){
            return{
                rooms: '',
            }
        },
        created() {
            $.ajaxSetup({
                headers: {"Authorization": "token " + sessionStorage.getItem("auth_token")}
            });
            this.loadRoom()
        },
        methods: {
            loadRoom(){
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/chat/room/",
                    type: "GET",
                    success: (response) =>{
                        this.rooms = response.data.data
                    }
                })
            },
            openDialog(id){
                this.$emit("openDialog", id)
            }
        }
    }
</script>

<style scoped>
    h3 {
        cursor: pointer;
    }
    .rooms-list{
        box-shadow: 1px 2px 3px aliceblue;
    }
</style>
