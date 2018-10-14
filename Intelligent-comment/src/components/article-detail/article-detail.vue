<template>
    <div class="article-detail">
        <div class="detail">
            <div class="title">
                <img class="book-pic" src="./pic-book.png" alt="封面">
                <div class="title-more">
                    <h1>{{ bookName }}</h1>
                    <h3>作者：<span>{{ bookAuthor }}</span></h3>
                    <h3>类别: <span>{{ bookTag }}</span></h3>
                    <span>
                        <Rate disabled show-text allow-half v-model="valueCustomText">
                            <span style="color: #f5a623">{{ valueCustomText }}</span>
                        </Rate>
                    </span>
                    <div class="title-more-foot">
                        <button>阅读</button>
                        <span><img src="./share.png" alt="">分享</span>
                        <span>收藏</span>
                    </div>
                </div>
            </div>
            <div class="information">
                <Tabs value="name1">
                    <TabPane label="书籍简介" name="intro">{{ intro }}</TabPane>
                    <TabPane label="目录" name="contents">{{ contents }}</TabPane>
                </Tabs>
            </div>
            <div class="comment">
                <Tabs value="name1">
                    <TabPane label="热门批注" name="intro">
                        <p>&nbsp;&nbsp;&nbsp;&nbsp;“{{ part }}”</p>
                        <p>&nbsp;&nbsp;&nbsp;&nbsp;“{{ annotation }}”</p>
                        <Page :total="100"/>
                    </TabPane>
                    <TabPane label="书籍评论" name="contents">{{ comment }}</TabPane>
                </Tabs>
            </div>
        </div>
        <div class="right">
            <Author :author_id="uploader"></Author>
            <SomeTag></SomeTag>
            <RealAd></RealAd>
        </div>
    </div>
</template>

<script>
    import SomeTag from "../some-tag/some-tag";
    import RealAd from "../real-ad/real-ad";
    import Author from '../author/author'
    import axios from 'axios'

    export default {
        name: "article-detail",
        components: {RealAd, SomeTag, Author},
        data() {
            return {
                bookTag: '社会科学',  // 书籍的标签（分类）
                bookName: '看不见的城市',  // 书名
                bookAuthor: '王老三',  // 作者
                intro: '这里是简介这里是简介这里是简介这里是简介这里是简介这里是简介这里是简介这里是简介这里是简介这里是简介这里是简介这里是简介这里是简介这里是简介这里是简介...',  // 简介
                valueCustomText: 3.8,  // 书籍评分
                contents: '暂时还不知道怎么获取书籍目录，先空着',  // 书籍目录
                part: '书籍里面摘抄的段落或者句子或者什么玩意的吧emm书籍里面摘抄的段落或者句子或者什么玩意的吧emm书籍里面摘抄的段落或者句子或者什么玩意的吧emm',  // 书籍摘抄的段落，下面显示的就是对这一段的批注
                annotation: '这里是批注这里是批注这里是批注这里是批注这里是批注这里是批注这里是批注这里是批注这里是批注这里是批注这里是批注这里是批注',  // 书籍批注
                comment: '评论吧,不过暂时貌似还没讨论清楚评论和批注的关系所以暂时先空着',  // 书籍评论
                uploader:1
            }
        },
        created() {
            var that = this
            axios.get(this.GLOBAL.ajax_path + '/api/reading/get_book_info/' + this.$route.params.book_id).then((data) => {
                if (data.status == 200) {
                    if (data.data) {
                        if (data.data.code == 1) {
                            data = data.data.data;
                            that.bookTag = '没实装~';
                            that.bookName = data.title;
                            that.bookAuthor = data.author;
                            that.intro = '没实装~没实装~没实装~没实装~没实装~没实装~没实装~没实装~没实装~没实装~没实装~没实装~';
                        }
                    }
                }
            })
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
        width: 55%;
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
        display: flex;
        align-items: center;
        justify-content: center;
        flex: 0 0 30%;
    }

    .title-more-foot span img {
        width: 20px;
        height: 20px;
    }

    .information {
        height: 350px;
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

    .ivu-page {
        text-align: center;
    }
</style>