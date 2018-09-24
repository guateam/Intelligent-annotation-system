<template>
    <div class="teacher">
        <h2>热门教师推荐<a href="javascript:" class="lookmore">更多 > </a></h2>
        <div class="teacher-detail">
            <div class="abox">
                <div class="name">
                    <h2>老师一</h2>
                    <h3>称号1、称号2</h3>
                </div>
                <img src="./head.png" alt="头像" class="head-pic">
            </div>
            <p class="detail-word">&nbsp;&nbsp;&nbsp;&nbsp;师简介教师师简介教师教师简介教师简介教师简介教师简介教师简介教师简介教师简介教师简介教师简介</p>
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
    }


    .abox {
        height: 60px;
        display: flex;
        justify-content: space-between;
        margin-top: 5px;
    }

    .name {
        margin-left: 30px;
        text-align: center;
    }

    .head-pic {
        margin-right: 30px;
        width: 60px;
        height: 60px;
        border-radius: 50%;
    }

    .detail-word {
        margin: 5px 30px 5px;
    }
</style>