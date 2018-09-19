<template>
  <div id="app">
    <Myheader></Myheader>
    <ArticleList></ArticleList>
  </div>
</template>

<script>
    // @ is an alias to /src
    import Myheader from '@/components/myheader/myheader'
    import ArticleList from '@/components/article-list/article-list'

    export default {
        components: {
            Myheader,
            ArticleList
        }
    }
</script>
