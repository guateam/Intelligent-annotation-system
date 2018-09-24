<template>
    <div class="teacher">
        <div class="teacher-detail">
            <div class="abox">
                <img src="./head.png" alt="头像" class="head-pic">
                <div class="name">
                    <h2>老师一</h2>
                    <h3>称号1、称号2</h3>
                </div>
            </div>
            <p class="detail-word">&nbsp;&nbsp;&nbsp;&nbsp;师简介教师师简介教师教师简介教师简介教师简介教师简介教师简介教师简介教师简介教师简介教师简介</p>
            <div class="other">
                <h3>其他作品:</h3>
                <ul>-作品1</ul>
                <ul>-作品2</ul>
                <ul>-作品3</ul>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: "good-student"
    }
</script>

<style scoped>
    .teacher-detail {
        border-bottom: 1px solid grey;
        padding-bottom: 10px;
    }

    .abox {
        height: 60px;
        display: flex;
        justify-content: space-between;
        margin-top: 5px;
    }

    .name {
        margin-right: 30px;
        text-align: center;
    }

    .head-pic {
        margin-left: 30px;
        width: 60px;
        height: 60px;
        border-radius: 50%;
    }

    .detail-word {
        margin: 5px 30px 5px;
    }
    .other{
        padding-left: 30px;
    }
</style>