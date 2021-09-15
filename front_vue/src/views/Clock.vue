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

<style lang='scss' scoped>
.clock-container {
  display: flex;
  align-items: center;
}
</style>