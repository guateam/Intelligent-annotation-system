<!--这里是author更应该是上传人的意思
<!--开始命名的时候搞错了
<!--懒得改了
<!--总之这个组建是用来显示上传的人的信息的
<!--在侧边栏使用-->
<template>
    <div class="teacher">
        <div class="teacher-detail">
            <div class="abox">
                <img src="./head.png" alt="头像" class="head-pic">
                <div class="name">
                    <h2>{{ teacher }}</h2>
                    <h3>{{ teacherTag }}</h3>
                </div>
            </div>
            <p class="detail-word">&nbsp;&nbsp;&nbsp;&nbsp;{{ teacherIntro }}</p>
            <div class="other">
                <h3>其他作品:</h3>
                <ul>-{{ teacherWork }}</ul>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: "good-student",
        data() {
            return {
                teacher: '张三三',  // 教师名
                teacherTag: '称号？',  // 教师称号，貌似用不上
                teacherIntro: '这里是教师简介这里是教师简介这里是教师简介这里是教师简介这里是教师简介这里是教师',  // 教师简介
                teacherWork: '作品一',  // 讲道理应该是教师上传的其他作品吧
            }
        }
    }
</script>

<style scoped>
    .teacher {
        margin-top: 55px;
    }

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

    .other {
        padding-left: 30px;
    }
</style>