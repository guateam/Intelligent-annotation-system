<template>
    <div class="article-detail">
        <div class="detail">
            <div class="title">
                <img class="book-pic" src="./pic-book.png" alt="封面">
                <div class="title-more">
                    <h1>这是书名</h1>
                    <h3>作者：<span>张老三</span></h3>
                    <h3>类别: <span>文学、社会科学</span></h3>
                    <span>
                        <Rate disabled show-text allow-half v-model="valueCustomText">
                            <span style="color: #f5a623">{{ valueCustomText }}</span>
                        </Rate>
                    </span>
                    <div class="title-more-foot">
                        <button>阅读</button>
                        <span>分享</span>
                        <span>收藏</span>
                    </div>
                </div>
            </div>
            <div class="information">
                <Tabs value="name1">
                    <TabPane label="标签一" name="name1">标签一的内容</TabPane>
                    <TabPane label="标签二" name="name2">标签二的内容</TabPane>
                    <TabPane label="标签三" name="name3">标签三的内容</TabPane>
                </Tabs>
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
        components: {RealAd, SomeTag, Author},
        data() {
            return {
                valueCustomText: 3.8
            }
        }
    }
</script>

<style scoped>
    .article-detail {
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
        display: flex;
    }

    .book-pic {
        width: 80px;
        height: 120px;
        float: left;
        margin-top: 40px;
        margin-left: 40px;
    }

    .title-more {
        padding-top: 40px;
        flex: 0 0 60%;
    }

    .title-more-foot {
        bottom: 0;
        display: flex;
        align-items: center;
        justify-content: center;
        width: 100%;
    }

    .title-more-foot button {
        flex: 0 0 20%;
    }

    .title-more-foot span {
        text-align: center;
        flex: 0 0 40%;
    }

    .information {
        height: 400px;
        background-color: white;
        margin-top: 20px;
    }

    .comment {
        background-color: white;
        margin-top: 20px;
    }

    .comment p {
        padding: 10px 20px;
    }
</style>