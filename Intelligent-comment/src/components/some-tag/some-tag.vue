<template>
    <div class="sometag">
        <h2>热门分类<a href="javascript:" class="lookmore">更多 > </a></h2>
        <div class="sometag-box">
            <div class="tag-items">分类一</div>
            <div class="tag-items">分类一</div>
            <div class="tag-items">分类一</div>
        </div>
        <div class="sometag-box" style="border-bottom: 1px solid grey">
            <div class="tag-items">分类一</div>
            <div class="tag-items">分类一</div>
        </div>
    </div>
</template>

<script>
    export default {
        name: "some-tag"
    }
</script>

<style scoped>
    .lookmore {
        float: right;
        margin-right: 5px;
    }
    .sometag-box {
        width: 100%;
        height: 50px;
        display: flex;
        align-items: center;
        justify-content: center;
    }

    .tag-items {
        width: 60px;
        height: 35px;
        border: 1px solid yellow;
        margin: 10px;
        border-radius: 5px;
        display: flex;
        align-items: center;
        justify-content: center;
    }
</style>