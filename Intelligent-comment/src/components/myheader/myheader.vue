<template>
    <div class="tab">
        <router-link tag="div" class="tab-item" to="/mainpage">
            <span class="tab-link">首页</span>
        </router-link>
        <router-link tag="div" class="tab-item" to="/findmore">
            <span class="tab-link">发现</span>
        </router-link>
        <router-link tag="div" class="tab-item" to="/search">
            <span class="tab-link">搜索</span>
        </router-link>
        <router-link tag="div" class="tab-item" to="/notice">
            <span class="tab-link">消息</span>
        </router-link>
        <router-link tag="div" class="tab-item" to="/myself">
            <span class="tab-link">我的</span>
        </router-link>
    </div>
</template>

<script type="text/ecmascript-6">
    export default {name: "myheader"}
</script>

<style scoped lang="stylus" rel="stylesheet/stylus">
    @import "../../common/style/variable.styl"
    .tab
        display: flex
        height: 44px
        line-height: 44px
        font-size: $font-size-medium
        .tab-item
            flex: 1
            text-align: center
            .tab-link
                padding-bottom: 5px
                color: $color-text-l
            &.router-link-active
                .tab-link
                    color: $color-theme
                    border-bottom: 2px solid $color-theme
</style>