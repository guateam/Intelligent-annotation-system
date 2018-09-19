<template>
    <div class="demo-split">
        <Split v-model="split1">
            <div slot="left" class="demo-split-pane">
                Left Pane
            </div>
            <div slot="right" class="demo-split-pane">
                Right Pane
            </div>
        </Split>
    </div>
</template>

<script>
    export default {
        name: "article-list",
        data () {
            return {
                split1: 0.75
            }
        },
    }
</script>

<style scoped>
    .demo-split{
        height: 200px;
        border: 1px solid #dcdee2;
    }
    .demo-split-pane{
        padding: 10px;
    }
</style>