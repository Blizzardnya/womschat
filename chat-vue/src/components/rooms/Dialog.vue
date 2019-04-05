<template>
    <RoomSlot>
        <mu-col span="8" xl="10" style="margin-top: 2%;">
            <AddUsers :room="id"></AddUsers>
            <mu-container class="dialog">
                <mu-row v-for="dialog in dialogs"
                        direction="column"
                        justify-content="start"
                        align-items="end">
                    <mu-flex>
                        <mu-avatar style="margin-right: 10px;" text-color="blue300" color="indigo900" :size="32">MB
                        </mu-avatar>
                        <mu-paper class="demo-paper" :z-depth="1">
                            <strong>{{dialog.user.username}}</strong><br>
                            {{dialog.text}}
                        </mu-paper>
                    </mu-flex>
                    <br>
                    <!--<p><strong>{{dialog.user.username}}</strong></p>-->
                    <!--<p>{{dialog.text}}</p>-->
                    <!--<span>{{dialog.date}}</span>-->
                </mu-row>
            </mu-container>
            <mu-container>
                <mu-flex align-items="center">
                    <mu-text-field v-model="form.textarea"
                                   multi-line :rows="3"
                                   full-width
                                   placeholder="Введите сообщение"></mu-text-field>
                    <mu-button @click="sendMessage" round color="success">Отпрвить</mu-button>
                </mu-flex>
            </mu-container>
        </mu-col>
    </RoomSlot>
</template>

<script>
    import RoomSlot from './Room'
    import AddUsers from './AddUsers'

    export default {
        name: "Dialog",
        components: {AddUsers, RoomSlot},
        props: {id: ''},
        data() {
            return {
                dialogs: '',
                form: {
                    textarea: '',
                }
            }
        },
        created() {
            $.ajaxSetup({
                headers: {"Authorization": "token " + sessionStorage.getItem("auth_token")}
            });
            setInterval(() => {
                this.loadDialog()
            }, 5000)
            this.loadDialog()
        },
        methods: {
            loadDialog() {
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/chat/dialog/",
                    type: "GET",
                    data: {
                        room: this.$route.params.id
                    },
                    success: (response) => {
                        this.dialogs = response.data.data
                    }
                })
            },
            sendMessage() {
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/chat/dialog/",
                    type: "POST",
                    data: {
                        room: this.$route.params.id,
                        text: this.form.textarea
                    },
                    success: (response) => {
                        this.loadDialog()
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

</style>
