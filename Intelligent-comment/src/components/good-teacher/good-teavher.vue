<template>
    <div class="teacher">
        <h2>热门教师推荐<a href="javascript:" class="lookmore">更多 > </a></h2>
        <div class="teacher-detail">
            <div class="abox">
                <div class="name">
                    <h2>{{ teacher }}</h2>
                    <h3>{{ teacherTag }}</h3>
                </div>
                <img src="./head.png" alt="头像" class="head-pic">
            </div>
            <p class="detail-word">&nbsp;&nbsp;&nbsp;&nbsp;{{ teacherIntro }}</p>
        </div>
    </div>
</template>

<script>
    export default {
        name: "good-student",
        data() {
            return{
                teacher: '王汪汪',  // 教师名
                teacherTag: '称号一',  // 其实这个我也不知道是个啥
                teacherIntro: '这里是教师简介这里是教师简介这里是生简介简介这里是学教师简介这里是生简介这里是生简介这里是生简教师简介',  // 教师简介
            }
        }
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