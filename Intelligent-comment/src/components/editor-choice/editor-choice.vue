<template>
    <div class="article">
        <div class="tag">- 编辑推荐 -</div>
        <h1 class="header">{{ bookName }}</h1>
        <img class="book-pic" src="./pic-book.png" alt="封面">
        <p class="someword">
            &nbsp;&nbsp;&nbsp;&nbsp;{{ word }}
            <router-link class="lookmore" to="article-detail">&nbsp;阅读全文&nbsp;&rsaquo;</router-link>
        </p>
        <div class="items">
            <h2>《放弃了我好困啊我要先睡觉嘤嘤嘤》<span></span></h2>
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
                bookName: '看不见的城市',  // 书名
                word: '这里都是编辑推荐的话这里都是编辑推荐的话这里都是编辑推荐的话这里都是编辑推荐的话这里都是编辑推荐的话这里都是编辑推荐的话这里都是编辑推荐的话这里都是编辑推荐的话这里都是...',  // 推荐的话
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