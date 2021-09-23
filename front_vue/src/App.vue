<template>
  <div id="app">
    <div id="nav">
      <v-touch v-on:swipeleft="swiperleft" v-on:swiperight="swiperright" class="wrapper">
        <router-view />
      </v-touch>
    </div>
  </div>
</template>

<script>

export default {
  methods:{
    swiperright: function () { //右滑切换到detail页
      if (this.$route.path == '/clock'){
        this.$router.replace({'path':'/historyChart'});
        return
      }
      if (this.$route.path == '/historyChart'){
        this.$router.replace({'path':'/dashboard'});
        return
      }
      if (this.$route.path == '/dashboard'){
        this.$router.replace({'path':'/clock'});
        return
      }
    },
    swiperleft: function () { //右滑切换到detail页
      if (this.$route.path === '/clock') {
        this.$router.replace({'path': '/dashboard'});
        return
      }
      if (this.$route.path === '/dashboard') {
        this.$router.replace({'path': '/historyChart'});
        return
      }
      if (this.$route.path === '/historyChart'){
        this.$router.replace({'path':'/clock'});
        return
      }
    }
  }

}
</script>

<style>
#app {
  font-family: pingfang, serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  height: 100%;
  color: #2c3e50;
  /*background: radial-gradient(ellipse at center, #2980b9 0%, #2c3e50 100%);*/
  background: rgb(67,61,92);
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
