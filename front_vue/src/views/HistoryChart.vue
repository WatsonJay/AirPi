<template>
  <div :style="{height:allHeight+ 'px', width: '100%'}">

  </div>
</template>

<script>
export default {
  name: "historyChart",
  data () {
    return {
      allHeight: document.body.clientHeight - 20
    }
  },
  mounted() {
    const that = this
    window.onresize = () => {
      that.allHeight = document.body.clientHeight - 20
    }
  }
}
</script>

<style scoped>

</style>