<template>
    <div>
        <div class="article" v-for="item in data">
            <div class="tag">- {{ item.bookTag }} -</div>
            <h1 class="header">{{ item.bookName }}</h1>
            <img class="book-pic" src="./pic-book.png" alt="封面">
            <p class="someword">
                {{ item.intro }}
                <router-link class="lookmore" :to="'/article-detail/'+item.id">&nbsp;阅读全文&nbsp;&rsaquo;
                </router-link>
            </p>
            <div class="items">
                <span>like</span>
                <span class="comment"><img src="./comment.png" alt="">共有{{ item.commentNumber }}条评论</span>
                <span><img src="./share.png" alt="">分享</span>
                <!--收藏的logo暂时出了点问题先不管了-->
                <span><img :src="item.ifcollection" alt="">收藏</span>
                <!--暂时不需要 更多 这个功能-->
                <span>更多</span>
            </div>
        </div>
    </div>
</template>

<script>
    import collectionNo from './collection-no.png'
    import collectionYes from './collection.png'
    import axios from 'axios'

    export default {
        name: "article-list",
        data() {
            return {
                data: []
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
        },
        created() {
            var that = this
            axios.get(this.GLOBAL.ajax_path + '/api/reading/article_recommend?token=' + this.$cookies.get('token')).then((data) => {
                if (data.status == 200) {
                    if (data.data) {
                        if (data.data.code == 1) {
                            data = data.data.data
                            for(let i=0;i<data.length;i++){
                                that.data.push({
                                    bookTag:'文章推荐',
                                    bookName:data[i].title,
                                    intro:'这里是介绍，但是没有实装。。。',
                                    commentNumber:data[i].num_comment,
                                    ifcollection:data[i].collection?'collectionNo':'collectionYes',
                                    id:data[i].id
                                })
                            }
                        }
                    }
                }
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