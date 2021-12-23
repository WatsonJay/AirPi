<template>
  <div :style="{height:allHeight+ 'px', width: allWidth + 'px', position: 'absolute'}">
    <div class="main" style="height: 70%">
      <a-row>
        <a-col :span="12">
          <v-chart autoresize :option="optionHCHO" :style="{width: allHeight * 0.82 + 'px',height: allHeight * 0.60 + 'px'}"/>
          <a-row style="padding:0 5px">
            <a-col :span="3">
              <div style="width: 100%;margin: 0 auto;" :style="{'border-bottom': '6px solid '+ this.AQILevel[0]}" ></div>
            </a-col>
            <a-col :span="3">
              <div style="width: 100%;margin: 0 auto;" :style="{'border-bottom': '6px solid '+ this.AQILevel[1]}" ></div>
            </a-col>
            <a-col :span="3">
              <div style="width: 100%;margin: 0 auto;" :style="{'border-bottom': '6px solid '+ this.AQILevel[2]}" ></div>
            </a-col>
            <a-col :span="3">
              <div style="width: 100%;margin: 0 auto;" :style="{'border-bottom': '6px solid '+ this.AQILevel[3]}" ></div>
            </a-col>
            <a-col :span="3">
              <div style="width: 100%;margin: 0 auto;" :style="{'border-bottom': '6px solid '+ this.AQILevel[4]}" ></div>
            </a-col>
            <a-col :span="3">
              <div style="width: 100%;margin: 0 auto;" :style="{'border-bottom': '6px solid '+ this.AQILevel[5]}" ></div>
            </a-col>
          </a-row>
          <a-row style="margin-left: -18px">
            <a-col :span="3">
              <span>0</span>
            </a-col>
            <a-col :span="3">
              <span>50</span>
            </a-col>
            <a-col :span="3">
              <span>100</span>
            </a-col>
            <a-col :span="3">
              <span>150</span>
            </a-col>
            <a-col :span="3">
              <span>200</span>
            </a-col>
            <a-col :span="3">
              <span>300</span>
            </a-col>
          </a-row>
        </a-col>
        <a-col :span="12">

        </a-col>
      </a-row>
    </div>
    <div class="panel" style="height: 30%">
      <a-row class="panel-context" :gutter="10">
        <a-col :span="5">
          <a-row style="margin-top: 20px">
            <a-col :span="20">
              <span class="number" :style="{'font-size': allHeight * 0.18 + 'px', 'line-height': allHeight * 0.18 + 'px'}">{{AQI.value}}</span>
            </a-col >
            <a-col :span="4">
              <span style="font-size: 18px">AQI</span><br/>
              <div style="width: 50px;height: 26px;margin: 5px auto;border-radius: 2px" :style="{'background': this.AQI.background}" >
                  <span style="line-height: 26px">{{ this.AQI.status }}</span>
              </div>
            </a-col>
          </a-row>
        </a-col>
        <a-col :span="5"></a-col>
        <a-col :span="3">
          <div>
            <div style="width: 80%;border-radius: 2px;margin-top: 4px"></div>
            <span>温度</span>
            <div style="color: #dee2e6">
              <span class="number" :style="{'font-size': allHeight * 0.14 + 'px', 'line-height': allHeight * 0.14 + 'px'}">{{temp}}</span>
              <br/><span> ℃</span>
            </div>
          </div>
        </a-col>
        <a-col :span="3">
          <div>
            <div style="width: 60%;border-radius: 2px;margin-top: 4px"></div>
            <span>湿度</span>
            <div style="color: #dee2e6">
              <span class="number" :style="{'font-size': allHeight * 0.14 + 'px', 'line-height': allHeight * 0.14 + 'px'}">{{hum}}</span>
              <br/><span> %</span>
            </div>
          </div>
        </a-col>
        <a-col :span="4">
          <div>
            <div style="width: 60%;margin: 0 auto;border-radius: 2px" :style="{'border-bottom': '4px solid '+ this.pm10.color}" ></div>
            <span>PM10</span>
            <div style="color: #dee2e6">
              <span class="number" :style="{'font-size': allHeight * 0.14 + 'px', 'line-height': allHeight * 0.14 + 'px'}">{{pm10.value}}</span>
              <br/><span> ㎍/㎥</span>
            </div>
          </div>
        </a-col>
        <a-col :span="4">
          <div>
            <div style="width: 60%;margin: 0 auto;border-radius: 2px" :style="{'border-bottom': '4px solid '+ this.TVOC.color}" ></div>
            <span>TVOC</span>
            <div style="color: #dee2e6">
              <span class="number" :style="{'font-size': allHeight * 0.14 + 'px', 'line-height': allHeight * 0.14 + 'px'}">{{TVOC.value}}</span>
              <br/><span> mg/m³</span>
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
      AQILevel: ['#2ED386', '#FFDB03', '#FA9C00', '#FF0101', '#920298', '#9A0000'],
      AQIStatus: ['优', '良', '轻度', '中度', '重度', '严重'],
      temp: 33,
      hum: 99,
      AQI: {value: 500, background: '#2ED386', status: '优'},
      pm25: {value: 99.9, color: '#7E0023'},
      pm10: {value: 21, color: '#7E0023'},
      HCHO: {color: '#FF7E00',value: 0.3  , status: '中度'},
      CO2: {color: '#FF7E00',value: 9999, status: '立刻通风'},
      TVOC: {color: '#FF7E00',value: 0.3},
      optionHCHO: {},
    }
  },
  mounted() {
    const that = this
    that.reDrawHCHOChart()
  },
  methods: {
    reDrawHCHOChart() {
      this.optionHCHO = {
        series: [{

        }]
      }
    },
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
  font-weight: 6502;
  font-family: "digital-7";
}
</style>