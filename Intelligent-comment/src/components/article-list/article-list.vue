<template>
    <div class="article">
        <div class="tag">- {{ bookTag }} -</div>
        <h1 class="header">{{ bookName }}</h1>
        <img class="book-pic" src="./pic-book.png" alt="封面">
        <p class="someword">
            {{ intro }}
            <router-link class="lookmore" to="article-detail">&nbsp;阅读全文&nbsp;&rsaquo;</router-link>
        </p>
        <div class="items">
            <span>like</span>
            <span class="comment"><img src="./comment.png" alt="">共有{{ commentNumber }}条评论</span>
            <span><img src="./share.png" alt="">分享</span>
            <!--收藏的logo暂时出了点问题先不管了-->
            <span><img :src="ifcollection" alt="">收藏</span>
            <!--暂时不需要 更多 这个功能-->
            <span>更多</span>
        </div>
    </div>
</template>

<script>
    import collectionNo from './collection-no.png'
    import collectionYes from './collection.png'

    export default {
        name: "article-list",
        data() {
            return {
                bookTag: '书籍推荐',  // 这一块的内容的标签，分文章、书籍、批注推荐等
                bookName: '看不见的城市',  // 书名
                intro: '这里都是正文这里都是正文这里都是正文这里都是正文这里都是正文这里都是正文这里都是正文这里都是正文这里都是正文这里都是正文这里都是正文这里都是正文这里文这里都是正文这里都是正文这里是正文...',  // 简介
                commentNumber: '1954',  // 文章所有评论的数目
                ifcollection: 'collectionNo',  // 未收藏状态的logo
            }
        },
        methods: {
            changecollection() {
                this.ifcollection = collectionNo;
            }
        },
        mounted() {
            changecollection()
            axios.get('', {}).then((response) => {
                this.intro = response.data.data['intro'];
            })
        }
    }
</script>

<style scoped>
    .article {
        width: 55%;
        background-color: white;
        margin: 55px 5% 30px 10%;
        height: 230px;
        line-height: 1.8;
        float: left;
    }

    .tag {
        width: 100%;
        text-align: center;
    }

    .header {
        font-weight: bold;
        font-size: 1.4em;
        margin-left: 30px;
    }

    .book-pic {
        float: right;
        width: 80px;
        height: 120px;
        margin: 0 50px auto;
    }

    .someword {
        margin-left: 30px;
    }

    .lookmore {
        color: deepskyblue;
    }

    .items {
        width: 100%;
        display: flex;
        align-items: center;
        justify-content: center;
        height: 60px;
        bottom: 0;
    }

    .items span {
        flex: 0 0 20%;
        align-items: center;
        justify-content: center;
        display: flex;
    }

    .items span img {
        width: 20px;
        height: 20px;
    }
</style>