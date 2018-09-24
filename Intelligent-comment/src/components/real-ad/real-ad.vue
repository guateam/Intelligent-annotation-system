<template>
    <div class="ad">
        <div class="real-ad-title">
            <h2>App&nbsp;&nbsp;&nbsp;【圈点阅读】</h2>
            <h5>不止能做批注的阅读软件</h5>
        </div>
        <div class="qr">
            <div class="ios">
                <h3>ios</h3>
                <img src="./ios.png" alt="ios">
            </div>
            <div class="android">
                <h3>Android</h3>
                <img src="./android.png" alt="Android">
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: "real-ad"
    }
</script>

<style scoped>
    .real-ad-title {
        text-align: center;
        width: 100%;
        height: 60px;
    }

    .qr {
        display: flex;
        justify-content: space-between;
    }

    .qr img {
        width: 85px;
        height: 85px;
    }

    .ios, .android {
        text-align: center;
    }
    .ios{
        margin-left: 30px;
    }
    .android{
        margin-right: 30px;
    }
</style>