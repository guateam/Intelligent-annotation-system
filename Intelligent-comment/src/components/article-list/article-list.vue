<template>
    <div class="article">
        <div class="tag">-书籍推荐-</div>
        <h1 class="header">这是书名</h1>
        <img class="book-pic" src="./pic-book.png" alt="封面">
        <p class="someword">&nbsp;&nbsp;&nbsp;&nbsp;这里都是正文这里都是正文这里都是正文这里都是正文这里都是正文这里都是正文这里都是正文这里都是正文这里都是正文这里都是正文这里都是正文这里都是正文这里文这里都是正文这里都是正文这里是正文...
            <router-link class="lookmore" to="article-detail">&nbsp;阅读全文&nbsp;&rsaquo;</router-link>
        </p>
        <div class="items">
            <span>like</span>
            <span>评论</span>
            <span>分享</span>
            <span>收藏</span>
            <span>更多</span>
        </div>
    </div>
</template>

<script>

    export default {
        name: "article-list",
    }
</script>

<style scoped>
    .article{
        width: 52%;
        background-color: white;
        margin: 30px 5% 30px 10%;
        height: 270px;
        line-height: 1.8;
        float: left;
    }
    .tag{
        width: 100%;
        text-align: center;
    }
    .header{
        font-weight: bold;
        font-size: 1.4em;
        margin-left: 30px;
    }
    .book-pic{
        float: right;
        width: 80px;
        height: 120px;
        margin: 0 50px auto;
    }
    .someword{
        margin-left: 30px;
    }
    .lookmore{
        color: deepskyblue;
    }
    .items{
        width: 100%;
        display: flex;
        align-items: center;
        justify-content: center;
        height: 80px;
        bottom: 0;
    }
</style>