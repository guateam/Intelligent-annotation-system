<template>
    <div>
        <Login v-if="!isLogin"></Login>
    </div>
</template>

<script>
    import Login from '../login/login'

    export default {
        name: "myself",
        components: {Login},
        data() {
            return {
                isLogin: false,  // 是否登录
            }
        },
    }
</script>

<style scoped>
</style>