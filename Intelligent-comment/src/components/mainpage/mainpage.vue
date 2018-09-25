<template>
    <div class="mainpage" ref="mainpage">
        <ArticleList></ArticleList>
        <div class="right">
            <SomeTag></SomeTag>
            <GoodTeacher></GoodTeacher>
            <GoodStudent></GoodStudent>
            <RealAd></RealAd>
        </div>
        <router-view></router-view>
    </div>
</template>

<script>
    import ArticleList from "../article-list/article-list"
    import RealAd from "../real-ad/real-ad";
    import GoodStudent from "../good-student/good-student";
    import GoodTeacher from "../good-teacher/good-teavher";
    import SomeTag from "../some-tag/some-tag";

    export default {
        name: "mainpage",
        components: { ArticleList, SomeTag, GoodStudent, RealAd, GoodTeacher},
    }
</script>

<style scoped>
    .right {
        width: 22%;
        background-color: white;
        margin: 30px 10% 30px 5%;
        line-height: 1.8;
        right: 0;
        position: absolute;
    }
</style>