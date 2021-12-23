<template>
  <div :style="{height:allHeight+ 'px', width: allWidth + 'px', position: 'absolute'}">
    <div class="main" style="height: 70%">

    </div>
    <div class="panel" style="height: 30%">
      <a-row class="panel-context" :gutter="10">
        <a-col :span="5">
          <div style="border-radius: 6px; padding: 0 5px; box-shadow: 3px 2px 6px #343a40; margin-top: 20px; color: #e9ecef"
               :style="{background: AQI.background}">
            <span style="text-align: left" :style="{'font-size': allHeight * 0.035 + 'px'}">空气质量指数</span>
            <span class="number" style="text-align: right;display: block" :style="{'font-size': allHeight * 0.11 + 'px', 'line-height': allHeight * 0.11 + 'px'}">{{AQI.value}}</span>
          </div>
        </a-col>
        <a-col :span="4"></a-col>
        <a-col :span="3">
          <div>
            <span>PM2.5</span>
            <div style="width: 80%;margin: 0 auto;border-radius: 2px" :style="{'border-bottom': '4px solid '+ this.pm25.color}" ></div>
            <div style="color: #dee2e6">
              <span class="number" :style="{'font-size': allHeight * 0.14 + 'px', 'line-height': allHeight * 0.14 + 'px'}">{{pm25.value}}</span>
              <span> ㎍/㎥</span>
            </div>
          </div>
        </a-col>
        <a-col :span="3">
          <div>
            <span>PM2.5</span>
            <div style="width: 80%;margin: 0 auto;border-radius: 2px" :style="{'border-bottom': '4px solid '+ this.pm25.color}" ></div>
            <div style="color: #dee2e6">
              <span class="number" :style="{'font-size': allHeight * 0.14 + 'px', 'line-height': allHeight * 0.14 + 'px'}">{{pm25.value}}</span>
              <span> ㎍/㎥</span>
            </div>
          </div>
        </a-col>
        <a-col :span="4">
          <div>
            <span>PM2.5</span>
            <div style="width: 80%;margin: 0 auto;border-radius: 2px" :style="{'border-bottom': '4px solid '+ this.pm25.color}" ></div>
            <div style="color: #dee2e6">
              <span class="number" :style="{'font-size': allHeight * 0.14 + 'px', 'line-height': allHeight * 0.14 + 'px'}">{{pm25.value}}</span>
              <span> ㎍/㎥</span>
            </div>
          </div>
        </a-col>
        <a-col :span="4">
          <div>
            <span>PM2.5</span>
            <div style="width: 80%;margin: 0 auto;border-radius: 2px" :style="{'border-bottom': '4px solid '+ this.pm25.color}" ></div>
            <div style="color: #dee2e6">
              <span class="number" :style="{'font-size': allHeight * 0.14 + 'px', 'line-height': allHeight * 0.14 + 'px'}">{{pm25.value}}</span>
              <span> ㎍/㎥</span>
            </div>

          </div>
        </a-col>
        <a-col :span="4">
          <div>
            <span>PM2.5</span>
            <div style="width: 80%;margin: 0 auto;border-radius: 2px" :style="{'border-bottom': '4px solid '+ this.pm25.color}" ></div>
            <div style="color: #dee2e6">
              <span class="number" :style="{'font-size': allHeight * 0.14 + 'px', 'line-height': allHeight * 0.14 + 'px'}">{{pm25.value}}</span>
              <span> ㎍/㎥</span>
            </div>
          </div>
        </a-col>
      </a-row>
    </div>
  </div>
</template>

<script>
export default {
  name: "DashBoard",
  data() {
    return {
      allHeight: document.body.clientHeight,
      allWidth: document.body.clientWidth,
      AQI: {value: 0, background: '#FF0000'},
      pm25: {value: 9.99, color: '#7E0023'},
    }
  }
}
</script>

<style scoped>
.panel {
  width: 100%;
  height: 200px;
  position: absolute;
  right: 0;
  bottom: 0;
  background: inherit;
  overflow: hidden;
  padding: 5px;
}
.panel::before {
  content: '';
  position: absolute;
  top:0;
  right: 0;
  bottom: 0;
  left: 0;
  background: inherit;
  background-attachment: fixed;
  filter: blur(4px);
}
.panel::after {
  content: "";
  position: absolute;
  top:0;
  right: 0;
  bottom: 0;
  left: 0;
  background: rgba(0, 0, 0, 0.25);
}
.panel-context{
  z-index: 1;
  color: white;
  position: relative;
  margin: 0;
}
.number {
  color: #e9ecef;
  font-weight: 800;
  text-shadow: 1px 1px 2px #adb5bd;
  font-family: "digital-7";
}
</style>