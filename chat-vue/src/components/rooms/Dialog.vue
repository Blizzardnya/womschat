<template>
    <mu-col span="8" xl="10">
        <mu-container class="dialog">
            <mu-row v-for="dialog in dialogs"
                    direction="column"
                    justify-content="start"
                    align-items="end">
                <p><strong>{{dialog.user.username}}</strong></p>
                <p>{{dialog.text}}</p>
                <span>{{dialog.date}}</span>
            </mu-row>
        </mu-container>
        <mu-container>
            <mu-flex align-items="center">
                <mu-text-field v-model="form.textarea"
                               multi-line :rows="3"
                               placeholder="Введите сообщение"></mu-text-field>
                <mu-button round color="success">Отпрвить</mu-button>
            </mu-flex>
        </mu-container>
    </mu-col>
</template>

<script>
    export default {
        name: "Dialog",
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
            this.loadDialog()
        },
        methods: {
            loadDialog() {
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/chat/dialog/",
                    type: "GET",
                    data: {
                        room: this.id
                    },
                    success: (response) => {
                        this.dialogs = response.data.data
                    }
                })
            }
        }
    }
</script>

<style scoped>
    .dialog {
        border: 1px solid #000;
    }
</style>
