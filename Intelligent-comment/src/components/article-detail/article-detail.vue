<template>
    <div class="main">
        <div class="detail">
            <div class="title">
                <img class="book-pic" src="./pic-book.png" alt="封面">
                <div class="title-more">
                    <h1>这是书名</h1>
                    <h3>作者：<span>张老三</span></h3>
                    <h3>类别: <span>文学、社会科学</span></h3>
                    <span>这里应该是评分，暂时没用iview不好做</span>
                    <div class="title-foot">
                        <button>阅读</button>
                        <span>分享</span>
                        <span>收藏</span>
                    </div>
                </div>
            </div>
            <div class="information">
                这里还是先空出来吧，用iview的组件好写多了，原生我要死了
            </div>
            <div class="comment">
                <h1>热门批注</h1>
                <p>&nbsp;&nbsp;&nbsp;&nbsp;“这里是批注这里是批注这里是批注这里是批注这里是批注这里是批注这里是批注这里是批注这里是批注这里是批注这里是批注这里是批注这里是批注这里是批注”</p>
                <p>&nbsp;&nbsp;&nbsp;&nbsp;“这里是批注这里是批注这里是批注这里是批注这里是批注这里是批注这里是批注这里是批注这里是批注这里是批注这里是批注这里是批注这里是批注这里是批注”</p>
                <p>&nbsp;&nbsp;&nbsp;&nbsp;“这里是批注这里是批注这里是批注这里是批注这里是批注这里是批注这里是批注这里是批注这里是批注这里是批注这里是批注这里是批注这里是批注这里是批注”</p>
                <p>&nbsp;&nbsp;&nbsp;&nbsp;“这里是批注这里是批注这里是批注这里是批注这里是批注这里是批注这里是批注这里是批注这里是批注这里是批注这里是批注这里是批注这里是批注这里是批注”</p>
            </div>
        </div>
        <div class="right">
            <Author></Author>
            <SomeTag></SomeTag>
            <RealAd></RealAd>
        </div>
    </div>
</template>

<script>
    import SomeTag from "../some-tag/some-tag";
    import RealAd from "../real-ad/real-ad";
    import Author from '../author/author'

    export default {
        name: "article-detail",
        components: {RealAd, SomeTag,Author},
    }
</script>

<style scoped>
    .main {
        z-index: 200;
    }
    .right {
        width: 22%;
        background-color: white;
        margin: 30px 10% 30px 5%;
        line-height: 1.8;
        right: 0;
        position: absolute;
    }
    .detail {
        width: 52%;
        margin: 30px 5% 30px 10%;
        line-height: 1.8;
        float: left;
    }

    .title {
        width: 100%;
        background: white;
        height: 200px;
    }

    .book-pic {
        width: 80px;
        height: 120px;
        float: left;
        margin-top: 40px;
        margin-left: 40px;
    }
    .title-more{
        padding-top: 40px;
    }
    .title-foot {
        bottom: 0;
        display: flex;
        align-items: center;
        justify-content: center;
    }
    .title-foot button{
        flex: 0 0 20%;
    }
    .title-foot span{
        text-align: center;
        flex: 0 0 40%;
    }
    .information{
        height: 400px;
        background-color: white;
        margin-top: 20px;
    }
    .comment{
        background-color: white;
        margin-top: 20px;
    }
    .comment p{
        padding: 10px 20px ;
    }
</style>