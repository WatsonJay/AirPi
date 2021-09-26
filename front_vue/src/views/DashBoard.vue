<template>
  <div :style="{height:allHeight+ 'px', width: allWidth + 'px', margin: '10px 10px', position: 'absolute'}">
    <a-row>
      <a-col :span="5">
        <div class="PmDiv" :style="{height: allHeight * 0.2 + 'px','margin-top': '15px'}">
          <div style="background: #868e96; border-radius: 5px 5px 0 0 ;color: white">
            <span>PM2.5</span>
          </div>
          <div style="color: #c5f6fa">
            <span class="number" :style="{'font-size': allHeight * 0.11 + 'px', 'line-height': allHeight * 0.11 + 'px'}">{{pmValue.pm2}}</span>
            <span> ㎍/㎥</span>
          </div>
          <div style="width: 80%;margin: 0 auto;border-radius: 2px" :style="{'border-bottom': '4px solid '+ this.pmColor.pm2}" ></div>
        </div>
<!--        <div class="PmDiv" :style="{height: allHeight * 0.2 + 'px','margin-top': '20px'}">-->
<!--          <div style="background: #868e96; border-radius: 5px 5px 0 0 ;color: white">-->
<!--            <span>PM5</span>-->
<!--          </div>-->
<!--          <div style="color: #c5f6fa">-->
<!--            <span class="number" :style="{'font-size': allHeight * 0.11 + 'px', 'line-height': allHeight * 0.11 + 'px'}">{{pmValue.pm5}}</span>-->
<!--            <span> ㎍/㎥</span>-->
<!--          </div>-->
<!--          <div style="width: 80%;margin: 0 auto;border-radius: 2px" :style="{'border-bottom': '4px solid '+ this.pmColor.pm5}" ></div>-->
<!--        </div>-->
        <div class="PmDiv" :style="{height: allHeight * 0.2 + 'px','margin-top': '20px'}">
          <div style="background: #868e96; border-radius: 5px 5px 0 0 ;color: white">
            <span>PM10</span>
          </div>
          <div style="color: #c5f6fa">
            <span class="number" :style="{'font-size': allHeight * 0.11 + 'px', 'line-height': allHeight * 0.11 + 'px'}">{{pmValue.pm10}}</span>
            <span> ㎍/㎥</span>
          </div>
          <div style="width: 80%;margin: 0 auto;border-radius: 2px" :style="{'border-bottom': '4px solid '+ this.pmColor.pm10}" ></div>
        </div>
        <div style="border-radius: 6px; padding: 0 5px; box-shadow: 3px 2px 6px #343a40; margin-top: 20px"
             :style="{color: AQI.color, background: AQI.background, 'margin-top': allHeight * 0.2 + 40 + 'px'}">
          <span style="text-align: left" :style="{'font-size': allHeight * 0.035 + 'px'}">空气质量指数</span>
          <span class="number" style="text-align: right;display: block" :style="{'font-size': allHeight * 0.11 + 'px', 'line-height': allHeight * 0.11 + 'px'}">{{AQI.value}}</span>
        </div>
      </a-col>
      <a-col :span="10">
        <v-chart autoresize :option="optionCO2" :style="{height: allHeight * 0.5 + 'px'}"></v-chart>
        <v-chart autoresize :option="optionTVOC" :style="{height: allHeight * 0.5 + 'px'}"></v-chart>
      </a-col>
      <a-col :span="9">
        <v-chart autoresize :option="optionHCHO" :style="{height: allHeight * 0.82 + 'px'}"/>
        <a-row :gutter="20">
          <a-col :span="12" >
            <div style="background: hsla(0,0%,100%,.2); border-radius: 6px;box-shadow: 3px 2px 6px #343a40;">
              <!--              <span class="numberTitle" :style="{'font-size': allHeight * 0.035 + 'px'}">温度</span>-->
              <div style="background: #868e96; border-radius: 5px 5px 0 0 ;color: white;">
                <span>温度</span>
              </div>
              <div>
                <span class="number" :style="{'font-size': allHeight * 0.11 + 'px', 'line-height': allHeight * 0.11 + 'px'}">{{temp}}</span>
                <span style="color: #c5f6fa"> ℃</span>
              </div>
            </div>
          </a-col>
          <a-col :span="12">
            <div style="background: hsla(0,0%,100%,.2); border-radius: 6px;box-shadow: 3px 2px 6px #343a40;">
              <!--              <span class="numberTitle" :style="{'font-size': allHeight * 0.035 + 'px'}">湿度</span>-->
              <div style="background: #868e96; border-radius: 5px 5px 0 0 ;color: white">
                <span>湿度</span>
              </div>
              <div>
                <span class="number" :style="{'font-size': allHeight * 0.11 + 'px', 'line-height': allHeight * 0.11 + 'px'}">{{hum}}</span>
                <span style="color: #c5f6fa"> %</span>
              </div>
            </div>
          </a-col>
        </a-row>
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
      allWidth: document.body.clientWidth - 20,
      temp: 33,
      hum: 99,
      pm2: 21,
      pm5: 100,
      pm10: 55,
      AQI: {color: 'white', background: '#FF7E00', value: 0},
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
      HCHO: {color: '#FF7E00', status: '中度'},
      optionCO2: {},
      CO2: {color: '#FF0000', status: '严重'},
      optionTVOC: {},
      TVOC: {color: '#00E400', status: '优'},
    }
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
          radius: '90%',
          min: 0,
          max: 0.5,
          center: ["50%", "55%"],
          splitNumber: 20,
          axisLine: {
            roundCap: true,
            lineStyle: {
              width: document.body.clientHeight * 0.03,
              color: [
                [1, {
                  type: 'linear',
                  x: 0,
                  y: 1,
                  x2: 1, //从左到右 0-1
                  y2: 0,
                  colorStops: [{
                    offset: 0,
                    color: this.AQILevel[0] // 0% 处的颜色
                  }, {
                    offset: 0.2,
                    color: this.AQILevel[1] // 100% 处的颜色
                  }, {
                    offset: 0.4,
                    color: this.AQILevel[2] // 100% 处的颜色
                  }, {
                    offset: 0.6,
                    color: this.AQILevel[3] // 100% 处的颜色
                  }, {
                    offset: 1,
                    color: this.AQILevel[4] // 100% 处的颜色
                  }],
                  globalCoord: false // 缺省为 false
                }]
              ]
            }
          },
          pointer: {
            icon: 'circle',
            length: '20%',
            width: 18,
            offsetCenter: [0, '-85%'],
            itemStyle: {
              color: '#ffffff',
              borderColor: '#3498db',
              borderWidth: 1,
              shadowColor: '#3498db',
              shadowBlur: 15
            }
          },
          axisTick: {
            show:false
          },
          splitLine: {
            show:false
          },
          axisLabel: {
            show: false
          },
          title: {
            offsetCenter: [0, '-10%'],
            color: '#e9ecef',
            rich: {
              c: {
                height: 25,
                fontSize: 20,
                fontFamily: 'pingfang',
                width: 50,
                borderRadius: 4,
                color: '#fff',
                backgroundColor: this.HCHO.color,
                align: 'center'
              }
            },
            fontSize: document.body.clientHeight * 0.08,
          },
          detail: {
            offsetCenter: ['-50%', '60%'],
            valueAnimation: true,
            width: '60%',
            borderRadius: 8,
            formatter: function (value) {
              return '{a|'+value.toFixed(3) +'}{b|mg/m³}'
            },
            rich: {
              a: {
                fontSize: 50,
                fontWeight: 800,
                fontFamily: 'digital-7',
                width: 110,
                lineHeight: 50,
                color: '#e9ecef',
                align: 'left'
              },
              b: {
                lineHeight: 30,
                fontSize: 20,
                fontFamily: 'pingfang',
                color: '#fff',
                align: 'left'
              }
            }
          },
          data: [{
            value: 0.20,
            name: '甲醛\n{c|' + this.HCHO.status+ '}'
          }]
        }],
      }
    },
    reDrawCO2() {
      this.optionCO2 = {
        series: [{
          type: 'gauge',
          center: ["40%", "50%"],
          radius: '85%',
          startAngle: 280,
          endAngle: -10,
          min: 400,
          max: 2000,
          splitNumber: 8,
          itemStyle: {
            width: 10,
            color: { //图形渐变颜色方法，四个数字分别代表，右，下，左，上，offset表示0%到100%
              type: 'linear',
              x: 0,
              y: 1,
              x2: 1, //从左到右 0-1
              y2: 0,
              colorStops: [{
                offset: 0,
                color: '#CD48AE' // 0% 处的颜色
              }, {
                offset: 1,
                color: '#2CABFC' // 100% 处的颜色
              }],
              globalCoord: false // 缺省为 false
            }
          },
          progress: {
            show: true,
            roundCap: true,
            width: 10
          },
          pointer: {
            show: false,
          },
          axisTick: {
            show: false,
          },
          axisLine: {
            roundCap: true,
            lineStyle: {
              color: [[1, 'hsla(0,0%,100%,.2)']],
            }
          },
          splitLine: {
            show: false,
          },
          axisLabel: {
            show: false,
          },
          anchor: {
            show: false
          },
          title: {
            offsetCenter: [0, '10%'],
            color: '#e9ecef',
            rich: {
              c: {
                height: 20,
                fontSize: 15,
                width: 40,
                fontFamily: 'pingfang',
                borderRadius: 4,
                color: '#fff',
                backgroundColor: this.CO2.color,
                align: 'center'
              }
            },
            fontSize: 20,
          },
          detail: {
            valueAnimation: true,
            width: '60%',
            // lineHeight: 40,
            borderRadius: 8,
            offsetCenter: ['70%', '65%'],
            formatter: '{a|{value}}{b|PPM}',
            rich: {
              a: {
                fontSize: 40,
                fontWeight: 800,
                fontFamily: 'digital-7',
                shadowColor: '1px 1px 5px #3498db',
                lineHeight: 40,
                color: '#e9ecef',
                align: 'left'
              },
              b: {
                lineHeight: 24,
                fontFamily: 'pingfang',
                color: '#fff',
                align: 'left'
              }
            }
          },
          data: [
            {
              value: 1600,
              name: '二氧化碳\n{c|' + this.CO2.status+ '}'
            }
          ]
        }]
      }
    },
    reDrawTVOC() {
      this.optionTVOC = {
        series: [{
          type: 'gauge',
          center: ["40%", "50%"],
          radius: '85%',
          startAngle: 280,
          endAngle: -10,
          min: 0,
          max: 0.5,
          splitNumber: 8,
          itemStyle: {
            width: 10,
            color: { //图形渐变颜色方法，四个数字分别代表，右，下，左，上，offset表示0%到100%
              type: 'linear',
              x: 0,
              y: 1,
              x2: 1, //从左到右 0-1
              y2: 0,
              colorStops: [{
                offset: 0,
                color: '#CD48AE' // 0% 处的颜色
              }, {
                offset: 1,
                color: '#2CABFC' // 100% 处的颜色
              }],
              globalCoord: false // 缺省为 false
            }
          },
          progress: {
            show: true,
            roundCap: true,
            width: 10
          },
          pointer: {
            show: false,
          },
          axisTick: {
            show: false,
          },
          axisLine: {
            roundCap: true,
            lineStyle: {
              color: [[1, 'hsla(0,0%,100%,.2)']],
            }
          },
          splitLine: {
            show: false,
          },
          axisLabel: {
            show: false,
          },
          anchor: {
            show: false
          },
          title: {
            offsetCenter: [0, '10%'],
            color: '#e9ecef',
            rich: {
              c: {
                height: 20,
                fontSize: 15,
                width: 40,
                fontFamily: 'pingfang',
                borderRadius: 4,
                color: '#fff',
                backgroundColor: this.TVOC.color,
                align: 'center'
              }
            },
            fontSize: 20,
          },
          detail: {
            valueAnimation: true,
            width: '60%',
            // lineHeight: 40,
            borderRadius: 8,
            offsetCenter: ['70%', '65%'],
            formatter: function (value) {
              return '{a|' + value.toFixed(3) + '}{b|mg/m³}'
            },
            rich: {
              a: {
                fontSize: 40,
                fontWeight: 800,
                fontFamily: 'digital-7',
                lineHeight: 40,
                width: 75,
                color: '#e9ecef',
                align: 'left'
              },
              b: {
                lineHeight: 24,
                color: '#e9ecef',
                fontFamily: 'pingfang',
                align: 'left'
              }
            }
          },
          data: [{
            value: 0.10,
            name: '挥发气体\n{c|' + this.TVOC.status+ '}'
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
  font-weight: 800;
  text-shadow: 1px 1px 5px #3498db;
  font-family: "digital-7";
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
