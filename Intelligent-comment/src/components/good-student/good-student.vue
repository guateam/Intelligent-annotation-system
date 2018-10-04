<template>
    <div class="student">
        <h2>热门学生推荐<a href="javascript:" class="lookmore">更多 > </a></h2>
        <div class="student-detail">
            <div class="abox">
                <div class="name">
                    <h2>{{ student }}</h2>
                    <h3>{{ studentTag }}</h3>
                </div>
                <img src="./head.png" alt="头像" class="head-pic">
            </div>
            <p class="detail-word">&nbsp;&nbsp;&nbsp;&nbsp;{{ studentIntro }}</p>
        </div>
    </div>
</template>

<script>
    export default {
        name: "good-student",
        data(){
            return{
                student:'赵找找',  // 学生名
                studentTag: '称号一',  // 其实这个我也不知道是个啥
                studentIntro: '这里是学生简介这里是学生简介这里是生简介简介这里是学学生简介这里是生简介这里是生简介这里是生简学生简介',  // 学生简介
            }
        }
    }
</script>

<style scoped>
    .student-detail {
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