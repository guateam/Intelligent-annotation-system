<template>
  <div id="app">
    <Myheader></Myheader>
    <router-view></router-view>
  </div>
</template>

<script>
    // @ is an alias to /src
    import Myheader from './components/myheader/myheader'

    export default {
        components: {
            Myheader
        }
    }
</script>
