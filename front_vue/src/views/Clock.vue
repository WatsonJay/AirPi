<template>
  <div :style="{height:allHeight+ 'px', width: '100%'}" class="test-clock-container">
    <FlipClock />
  </div>
</template>

<script>
import FlipClock from "../components/FlipClock/FlipClock";
export default {
  name: "Clock",
  components: {
    FlipClock
  },
  data () {
    return {
      allHeight: document.body.clientHeight
    }
  },
  mounted() {
    const that = this
    window.onresize = () => {
      that.allHeight = document.body.clientHeight
    }
  }
}
</script>

<style lang='scss' scoped>
.clock-container {
  display: flex;
  align-items: center;
  font: normal 12px 'Helvetica Neue', Helvetica, sans-serif;
  user-select: none;
  text-shadow: 0 1px 0 rgba(0, 0, 0, 0.3);
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
}
</style>
