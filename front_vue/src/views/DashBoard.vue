<template>
  <div :style="{height:allHeight+ 'px', width: allWidth + 'px', margin: '10px 20px', position: 'absolute'}">
    <a-row>
      <a-col :span="11">
        <a-row>
          <a-col :span="12">
            <div style="float: left; border-radius: 6px; padding: 0 5px"
                 :style="{width: allWidth * 0.12 + 'px',height: allHeight * 0.12 + 'px',
                          color: AQIStyle.color, background: AQIStyle.background}">
              <span class="AQItext" style="text-align: left" :style="{'font-size': allHeight * 0.03 + 'px'}">空气质量指数</span>
              <span class="AQItext" style="text-align: right" :style="{'font-size': allHeight * 0.06 + 'px'}">{{AQI}}</span>
            </div>
          </a-col>
          <a-col :span="11">
            <div style="display: block">
              <span class="numberTitle" :style="{'--div-height': allHeight * 0.05 + 'px', '--font-height': allHeight * 0.05 + 'px'}">温度</span>
              <span class="numberTitle" :style="{'--div-height': allHeight * 0.06 + 'px', '--font-height': allHeight * 0.06 + 'px'}" style="float: right">{{temp}} ℃</span>
            </div>
            <div style="display: block">
              <span class="numberTitle" :style="{'--div-height': allHeight * 0.05 + 'px', '--font-height': allHeight * 0.05 + 'px'}">湿度</span>
              <span class="numberTitle" :style="{'--div-height': allHeight * 0.06 + 'px', '--font-height': allHeight * 0.06 + 'px'}" style="float: right">{{hum}} %</span>
            </div>
          </a-col>
        </a-row>
        <v-chart autoresize :option="optionHCHO" :style="{height: allHeight * 0.88 + 'px'}"/>
      </a-col>
      <a-col :span="13">
        <a-row>
          <a-col :span="8">
            <a-progress type="circle" :percent="pm2" :strokeColor="strokeColor" :width="allHeight * 0.22">
              <template #format="percent">
                <span style="color: red">{{ percent }}</span>
              </template>
            </a-progress>
            <span>pm2.5</span>
          </a-col>
          <a-col :span="8">
            <a-progress type="circle" :percent="pm5" :stroke-color="strokeColor" :width="allHeight * 0.22"></a-progress>
            <span style="display: block">pm5</span>
          </a-col>
          <a-col :span="8">
            <a-progress type="circle" :percent="pm10" :stroke-color="strokeColor" :width="allHeight * 0.22"></a-progress>
            <span>pm10</span>
          </a-col>
        </a-row>
        <v-chart autoresize :option="optionCO2" :style="{height: allHeight * 0.33 + 'px'}"></v-chart>
        <v-chart autoresize :option="optionHCHO" :style="{height: allHeight * 0.33 + 'px'}"></v-chart>
      </a-col>
    </a-row>
  </div>
</template>

<script>
export default {
  name: "Dashboard",
  data () {
    return {
      allHeight: document.body.clientHeight - 20,
      allWidth: document.body.clientWidth - 40,
      temp: 0,
      hum: 0,
      AQI: 0,
      pm2: 21,
      pm5: 100,
      pm10: 55,
      strokeColor: "{'0%': '#73d13d','50%': '#87d068', '100%': '#ff4d4f'}",
      AQIStyle: {color: 'white', background: 'green'},
      optionHCHO: {},
      optionCO2: {},
      optionPM2: {},
      optionPM5: {},
      optionPM10: {},
      optionTVOC: {},
    }
  },
  mounted() {
    const that = this
    this.reDrawHCHOChart()
    this.reDrawCO2()
    window.onresize = () => {
      that.allHeight = document.body.clientHeight - 20
      that.allWidth = document.body.clientWidth - 40
      that.reDrawHCHOChart()
      that.reDrawCO2()
    }
  },
  methods: {
    reDrawHCHOChart() {
      this.optionHCHO = {
        series: [{
          type: 'gauge',
          startAngle: 200,
          endAngle: -20,
          radius: '78%',
          min: 0,
          max: 0.5,
          center: ["50%", "55%"],
          splitNumber: 20,
          axisLine: {
            roundCap: true,
            lineStyle: {
              width: document.body.clientHeight * 0.02,
              color: [
                [0.1, '#73d13d'],
                [0.2, '#69c0ff'],
                [0.4, '#ffec3d'],
                [0.6, '#ff7a45'],
                [1, '#ff4d4f']
              ]
            }
          },
          pointer: {
            itemStyle: {
              color: 'auto'
            }
          },
          axisTick: {
            length: document.body.clientHeight * 0.02,
            lineStyle: {
              color: 'auto',
              width: document.body.clientHeight * 0.003,
            }
          },
          splitLine: {
            length: document.body.clientHeight * 0.04,
            lineStyle: {
              color: 'auto',
              width: document.body.clientHeight * 0.008,
            }
          },
          axisLabel: {
            color: '#ffffff',
            fontSize: document.body.clientHeight * 0.04,
            distance: - document.body.clientHeight * 0.145,
            formatter: function (value) {
              if (value === 0.025) {
                return '优';
              }
              else if (value === 0.075) {
                return '良';
              }
              else if (value === 0.125) {
                return '轻度';
              }
              else if (value === 0.25) {
                return '中度';
              }
              else if (value === 0.4) {
                return '重度';
              }
            }
          },
          title: {
            offsetCenter: [0, '90%'],
            color: '#bfbfbf',
            fontSize: document.body.clientHeight * 0.08,
          },
          detail: {
            fontSize: document.body.clientHeight * 0.06,
            offsetCenter: [0, '50%'],
            valueAnimation: true,
            formatter: function (value) {
              return value.toFixed(3) + 'mg/m³';
            },
            color: 'auto'
          },
          data: [{
            value: 0.20,
            name: '甲醛(HCHO)'
          }]
        }],
      }
    },
    reDrawCO2() {
      this.optionCO2 = {
        series: [{
          type: 'gauge',
          center: ["30%", "70%"],
          radius: '130%',
          startAngle: 200,
          endAngle: -20,
          min: 400,
          max: 2000,
          splitNumber: 8,
          axisLine: {
            lineStyle: {
              width: 10,
              color: [
                [0.25, '#73d13d'],
                [0.5, '#ffec3d'],
                [1, '#fd666d']
              ]
            }
          },
          pointer: {
            itemStyle: {
              color: 'auto'
            }
          },
          axisTick: {
            distance: -10,
            length: 5,
            lineStyle: {
              color: '#fff',
              width: 1
            }
          },
          splitLine: {
            distance: -8,
            length: 12,
            lineStyle: {
              color: '#fff',
              width: 2
            }
          },
          axisLabel: {
            fontSize: 0
          },
          detail: {
            valueAnimation: true,
            fontSize: 20,
            offsetCenter: ['210%', '-50%'],
            formatter: '{value} PPM',
            color: 'auto'
          },
          title: {
            offsetCenter: ['220%', 0],
            color: '#bfbfbf',
            fontSize: document.body.clientHeight * 0.05,
          },
          data: [{
            value: 800,
            name: '二氧化碳(CO2)'
          }]
        }]
      }
    }
  }
}
</script>

<style scoped>
.number {
  color: rgb(236,237,233);
  font-size: var(--div-height);
  /*font-family: "digital-7";*/
}
.numberTitle {
  color: rgb(236,237,233);
  font-size: var(--font-height);
  line-height: var(--div-height);
}
.AQItext {
  display: block;
}
.ant-carousel >>> .slick-slide {
  text-align: center;
  height: var(--div-height);
  line-height: var(--div-height);
  overflow: hidden;
}

.ant-carousel >>> .custom-slick-arrow {
  width: var(--icon-height);
  height: var(--icon-height);
  font-size: var(--icon-height);
  color: #fff;
  background-color: rgba(31, 45, 61, 0.11);
  opacity: 0.3;
}
.ant-carousel >>> .custom-slick-arrow:before {
  display: none;
}
.ant-carousel >>> .custom-slick-arrow:hover {
  opacity: 0.5;
}
</style>