<template>
    <div class="login">
        <Register v-if="register"></Register>
        <div class="main">
            <div class="box">
                <div class="box-header">
                    <h1 class="box-header-title"><img src="./logo.png" alt="">圈点阅读</h1>
                    <h2>不止能做批注的阅读软件</h2>
                </div>
                <div class="user-login">
                    <Input v-model="username" placeholder="请输入用户名、手机号或邮箱" clearable/>
                    <Input v-model="password" placeholder="请输入密码" clearable type="password"/>
                    <Button type="primary" long v-on:click="login()">登录</Button>
                </div>
                <div class="box-foot">
                    <h2><span>扫描二维码登录</span>|<span>社交账号登录</span></h2>
                    <h3>没有账号？<a v-on:click="userRegister()">注册</a></h3>
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
    import Register from "../register/register";
    import  axios  from "axios"
    import qs from 'qs'
    export default {
        name: "login",
        components: {Register, RealAd},
        data() {
            return {
                username: '',
                password: '',
                register: false
            }
        },
        methods: {
            // 这里有问题我知道的等做功能的之后再来改吧嘤嘤嘤
            userRegister() {
                this.register = !this.register;
            },
            login: function () {
                axios.post(this.GLOBAL.ajax_path+'/api/account/login',qs.stringify({
                    username:this.username,
                    password: this.password
                })).then((data) => {
                    if(data.status==200){
                        if(data.data){
                            if(data.data.code==1){
                                data=data.data.data
                                this.$cookies.set('token',data.token)
                                this.$cookies.set('group',data.group)
                                this.$router.push('/mainpage')
                            }
                        }
                    }
                })
            }
        }
    }
</script>

<style scoped>
    .login {
        height: 100%;
        width: 100%;
        z-index: 1111;
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