<template>
    <div class="register" v-if="register">
        <div class="main">
            <div class="box">
                <div class="box-header">
                    <h1 class="box-header-title"><img src="./logo.png" alt="">圈点阅读</h1>
                    <h2>不止能做批注的阅读软件</h2>
                </div>
                <div class="user-register">
                    <Input v-model="phone" placeholder="请输入手机号" clearable/>
                    <Input v-model="password" placeholder="请输入密码" clearable/>
                    <Button type="primary" long>注册</Button>
                </div>
                <div class="box-foot">
                    <h2>注册即代表同意圈点阅读隐私政策</h2>
                    <h3>已有账号？<a v-on:click="userLogin()">登录</a></h3>
                </div>
                <div class="box-real-ad">
                    <RealAd></RealAd>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import RealAd from "../real-ad/real-ad";
    import Login from "../login/login";

    export default {
        name: "register",
        components: {Login, RealAd},
        data() {
            return {
                phone: '',
                password: '',
                register: true
            }
        },
        methods: {
            userLogin() {
                this.register = false;
            }
        }
    }
</script>

<style scoped>
    .register {
        height: 100%;
        width: 100%;
        z-index: 2111;
        position: fixed;
        background: #eee;
    }

    .main {
        width: 30%;
        margin: 3% 35%;
    }

    .box {
        width: 90%;
        margin: 3% 5%;
        background-color: #ffffff;
        padding-bottom: 20px;
    }

    .ivu-btn, .ivu-input-wrapper {
        width: 80%;
        margin: 10px 10%;
    }

    .box-header {
        padding-top: 10px;
        text-align: center;
        height: 100px;
    }

    .box-header-title {
        display: flex;
        align-items: center;
        justify-content: center;
    }

    .box-foot {
        text-align: center;
        height: 60px;
    }

    .box-real-ad {
        text-align: center;
        width: 80%;
        margin: 0 10%;
    }
</style>