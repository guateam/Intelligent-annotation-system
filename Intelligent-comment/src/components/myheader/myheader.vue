<template>
    <div class="tab">
        <span class="tab-logo">
            <img src="./logo.png" alt="logo">
            圈点阅读
        </span>
        <router-link tag="div" class="tab-item mainpage" to="/mainpage">
            <span class="tab-link tab-link-word">首页</span>
        </router-link>
        <router-link tag="div" class="tab-item findmore" to="/findmore">
            <span class="tab-link tab-link-word">发现</span>
        </router-link>
        <span class="tab-item search">
            <Search></Search>
        </span>
        <router-link tag="div" class="tab-item notice" to="/notice">
            <span class="tab-link tab-link-pic"><img src="./消息通知.png" alt=""></span>
        </router-link>
        <router-link tag="div" class="tab-item myself" to="/myself">
            <span class="tab-link tab-link-pic tab-link-pic-myself"><img src="./默认头像.png" alt=""></span>
        </router-link>
    </div>
</template>

<script type="text/ecmascript-6">
    import Search from '../search/search'

    export default {
        name: "myheader",
        components: {Search},
        comments: "Search"
    }
</script>

<style scoped lang="stylus" rel="stylesheet/stylus">
    @import "../../common/style/variable.styl"
    .tab
        z-index: 500
        position: fixed
        top: 0
        left: 10%
        background: rgb(250, 250, 250)
        display: flex
        height: 44px
        line-height: 44px
        width: 80%
        font-size: $font-size-medium
        .tab-logo
            display: flex
            align-items: center
            font-weight: bolder
            font-size: 1.5em
            flex: 0 0 20%
            img
                width: 33px
                height: 33px
                margin-right: 5px
        .tab-item
            text-align: left
            img
                width: 30px
                height: 30px
            .tab-link
                color: $color-text-l
            &.router-link-active
                .tab-link-word
                    color: $color-theme
                    border-bottom: 2px solid $color-theme
        .mainpage
            flex: 0 0 10%
        .findmore
            flex: 0 0 10%
        .search
            flex: 0 0 48%
        .notice
            flex: 0 0 6%
        .myself
            flex: 0 0 6%
        .tab-link-pic
            width: 100%
            height: 100%
            display: flex
            align-items: center
            justify-content: center
        .tab-link-pic-myself
            display: flex
            justify-content: flex-end
</style>