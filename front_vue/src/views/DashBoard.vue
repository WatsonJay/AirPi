<template>
  <div :style="{height:allHeight+ 'px', width: allWidth + 'px', margin: '10px 20px', position: 'absolute'}">
    <a-row>
      <a-col :span="11">
        <v-chart autoresize :option="optionHCHO" :style="{height: allHeight * 0.77 + 'px'}" style="border-radius: 6px; margin-top: 8px"/>
        <a-row :gutter="10">
          <a-col :span="8">
            <div style="float: left; border-radius: 6px; padding: 0 5px; box-shadow: 3px 2px 6px #343a40;"
                 :style="{width: allWidth * 0.15 + 'px',height: allHeight * 0.18 + 'px',
                          color: AQIStyle.color, background: AQIStyle.background}">
              <span style="text-align: left" :style="{'font-size': allHeight * 0.035 + 'px'}">空气质量指数</span>
              <span class="number" style="text-align: right;display: block" :style="{'font-size': allHeight * 0.1 + 'px', 'line-height': allHeight * 0.08 + 'px'}">{{AQI}}</span>
            </div>
          </a-col>
          <a-col :span="4">

          </a-col>
          <a-col :span="6" >
            <div style="background: hsla(0,0%,100%,.2); border-radius: 6px">
<!--              <span class="numberTitle" :style="{'font-size': allHeight * 0.035 + 'px'}">温度</span>-->
              <div style="background: #868e96; border-radius: 5px 5px 0 0 ;color: white">
                <span>温度</span>
              </div>
              <div>
                <span class="number" :style="{'font-size': allHeight * 0.12 + 'px', 'line-height': allHeight * 0.13 + 'px'}">{{temp}}</span>
                <span style="color: #c5f6fa"> ℃</span>
              </div>
            </div>
          </a-col>
          <a-col :span="6">
            <div style="background: hsla(0,0%,100%,.2); border-radius: 6px">
<!--              <span class="numberTitle" :style="{'font-size': allHeight * 0.035 + 'px'}">湿度</span>-->
              <div style="background: #868e96; border-radius: 5px 5px 0 0 ;color: white">
                <span>湿度</span>
              </div>
              <div>
                <span class="number" :style="{'font-size': allHeight * 0.12 + 'px', 'line-height': allHeight * 0.13 + 'px'}">{{hum}}</span>
                <span style="color: #c5f6fa"> %</span>
              </div>
            </div>
          </a-col>
        </a-row>
      </a-col>
      <a-col :span="13">
        <v-chart autoresize :option="optionCO2" :style="{height: allHeight * 0.38 + 'px'}"></v-chart>
        <v-chart autoresize :option="optionTVOC" :style="{height: allHeight * 0.38 + 'px'}"></v-chart>
        <div style="margin: 10px">
          <a-row :gutter="10">
            <a-col :span="8">
              <div class="PmDiv" :style="{height: allHeight * 0.19 + 'px', width: allWidth * 0.14 + 'px'}">
                <div style="background: #868e96; border-radius: 5px 5px 0 0 ;color: white">
                  <span>PM2.5</span>
                </div>
                <div style="color: #c5f6fa">
                  <span class="number" :style="{'font-size': allHeight * 0.07 + 'px', 'line-height': allHeight * 0.1 + 'px'}">{{pmValue.pm2}}</span>
                  <span> ㎍/㎥</span>
                </div>
                <div style="width: 80%;margin: 0 auto;border-radius: 2px" :style="{'border-bottom': '4px solid '+ this.pmColor.pm2}" ></div>
              </div>
            </a-col>
            <a-col :span="8">
              <div class="PmDiv" :style="{height: allHeight * 0.19 + 'px', width: allWidth * 0.14 + 'px'}">
                <div style="background: #868e96; border-radius: 5px 5px 0 0 ;color: white">
                  <span>PM5</span>
                </div>
                <div style="color: #c5f6fa">
                  <span class="number" :style="{'font-size': allHeight * 0.07 + 'px', 'line-height': allHeight * 0.1 + 'px'}">{{pmValue.pm5}}</span>
                  <span> ㎍/㎥</span>
                </div>
                <div style="width: 80%;margin: 0 auto;border-radius: 2px" :style="{'border-bottom': '4px solid '+ this.pmColor.pm5}" ></div>
              </div>
            </a-col>
            <a-col :span="8">
              <div class="PmDiv" :style="{height: allHeight * 0.19 + 'px', width: allWidth * 0.14 + 'px'}">
                <div style="background: #868e96; border-radius: 5px 5px 0 0 ;color: white">
                  <span>PM10</span>
                </div>
                <div style="color: #c5f6fa">
                  <span class="number" :style="{'font-size': allHeight * 0.07 + 'px', 'line-height': allHeight * 0.1 + 'px'}">{{pmValue.pm10}}</span>
                  <span> ㎍/㎥</span>
                </div>
                <div style="width: 80%;margin: 0 auto;border-radius: 2px" :style="{'border-bottom': '4px solid '+ this.pmColor.pm10}" ></div>
              </div>
            </a-col>
          </a-row>
        </div>
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
      temp: 33,
      hum: 99,
      AQI: 0,
      pm2: 21,
      pm5: 100,
      pm10: 55,
      AQIStyle: {color: 'white', background: '#FF7E00'},
      pmColor: {
        pm2: '#7E0023',
        pm5: '#FFFF00',
        pm10: '#00E400'
      },
      pmValue: {
        pm2: 9999,
        pm5: 9999,
        pm10: 9999
      },
      AQILevel: ['#00E400', '#FFFF00', '#FF7E00', '#FF0000', '#99004C', '#7E0023'],
      optionHCHO: {},
      optionCO2: {},
      optionPM2: {},
      optionPM5: {},
      optionPM10: {},
      optionTVOC: {},
    }
  },
  computed: {
    // getPM2BackgroundString(){
    //   return 'linear-gradient(to top, '+ this.pmColor.pm2 +', #bdc3c7)'
    // },
    // getPM5BackgroundString(){
    //   return 'linear-gradient(to top, '+ this.pmColor.pm5 +', #bdc3c7)'
    // },
    // getPM10BackgroundString(){
    //   return 'linear-gradient(to top, '+ this.pmColor.pm10 +', #bdc3c7)'
    // }
  },
  mounted() {
    const that = this
    this.reDrawHCHOChart()
    this.reDrawCO2()
    this.reDrawTVOC()
    window.onresize = () => {
      that.allHeight = document.body.clientHeight - 20
      that.allWidth = document.body.clientWidth - 40
      that.reDrawHCHOChart()
      that.reDrawCO2()
      that.reDrawTVOC()
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
                [0.1, '#00E400'],
                [0.2, '#69c0ff'],
                [0.4, '#FFFF00'],
                [0.6, '#FF7E00'],
                [1, '#FF0000']
              ]
            }
          },
          pointer: {
            icon: 'path://M12.8,0.7l12,40.1H0.7L12.8,0.7z',
            length: '20%',
            width: 15,
            offsetCenter: [0, '-45%'],
            itemStyle: {
              color: 'auto'
            }
          },
          axisTick: {
            length: document.body.clientHeight * 0.02,
            splitNumber: 2,
            lineStyle: {
              color: 'auto',
              width: document.body.clientHeight * 0.002,
            }
          },
          splitLine: {
            length: document.body.clientHeight * 0.03,
            lineStyle: {
              color: 'auto',
              width: document.body.clientHeight * 0.006,
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
          radius: '100%',
          startAngle: 200,
          endAngle: -20,
          min: 400,
          max: 2000,
          splitNumber: 8,
          axisLine: {
            lineStyle: {
              width: 14,
              color: [
                [0.25, '#00E400'],
                [0.5, '#FFFF00'],
                [1, '#FF0000']
              ]
            }
          },
          pointer: {
            itemStyle: {
              color: 'auto'
            }
          },
          axisTick: {
            distance: -14,
            length: 5,
            lineStyle: {
              color: '#fff',
              width: 1
            }
          },
          splitLine: {
            distance: -14,
            length: 14,
            lineStyle: {
              color: '#fff',
              width: 2
            }
          },
          axisLabel: {
            distance: -22,
            fontSize: 10,
            color: '#e9ecef'
          },
          detail: {
            valueAnimation: true,
            fontSize: 20,
            offsetCenter: ['260%', '-30%'],
            formatter: '{value} PPM',
            color: 'auto'
          },
          title: {
            offsetCenter: ['240%', 0],
            color: '#bfbfbf',
            fontSize: document.body.clientHeight * 0.05,
          },
          data: [{
            value: 800,
            name: '二氧化碳(CO2)'
          }]
        }]
      }
    },
    reDrawTVOC() {
      this.optionTVOC = {
        series: [{
          type: 'gauge',
          center: ["70%", "70%"],
          radius: '100%',
          startAngle: 200,
          endAngle: -20,
          min: 0,
          max: 0.5,
          splitNumber: 10,
          axisLine: {
            lineStyle: {
              width: 14,
              color: [
                [0.1, '#00E400'],
                [0.2, '#69c0ff'],
                [0.4, '#FFFF00'],
                [0.6, '#FF7E00'],
                [1, '#FF0000']
              ]
            }
          },
          pointer: {
            itemStyle: {
              color: 'auto'
            }
          },
          axisTick: {
            distance: -14,
            length: 5,
            lineStyle: {
              color: '#fff',
              width: 1
            }
          },
          splitLine: {
            distance: -14,
            length: 14,
            lineStyle: {
              color: '#fff',
              width: 2
            }
          },
          axisLabel: {
            distance: -20,
            fontSize: 10,
            color: '#e9ecef'
          },
          detail: {
            valueAnimation: true,
            fontSize: 20,
            offsetCenter: ['-235%', '-35%'],
            formatter: function (value) {
              return value.toFixed(3) + 'mg/m³';
            },
            color: 'auto'
          },
          title: {
            offsetCenter: ['-240%', 0],
            color: '#bfbfbf',
            fontSize: document.body.clientHeight * 0.05,
          },
          data: [{
            value: 0.10,
            name: '挥发气体(TVOC)'
          }]
        }]
      }
    }
  }
}
</script>

<style scoped>
.number {
  color: #e9ecef;
  text-shadow: 1px 1px 5px #3498db;
  font-family: "digital-7";
}
.numberTitle {
  color: #e9ecef;
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
.PmDiv {
  border-radius: 5px;
  box-shadow: 3px 2px 6px #343a40;
  background: hsla(0,0%,100%,.2);
}
</style>
