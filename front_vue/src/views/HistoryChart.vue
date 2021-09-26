<template>
  <div :style="{height:allHeight+ 'px', width: allWidth + 'px', margin: '10px 10px', position: 'absolute'}">
    <v-chart name="tvoc" autoresize :option="optionTVOC" v-show="type == 'TVOC'" :style="{height: allHeight * 0.88 + 'px'}"></v-chart>
    <v-chart name="co2" autoresize :option="optionCO2" v-show="type == 'CO2'" :style="{height: allHeight * 0.88 + 'px'}"></v-chart>
    <v-chart name="pm" autoresize :option="optionPM" v-show="type == 'PM'" :style="{height: allHeight * 0.88 + 'px'}"></v-chart>
    <a-row style="margin-top: 8px">
      <a-col>
        <a-radio-group default-value="TVOC" v-model="type" button-style="solid">
          <a-radio-button value="TVOC">
            TVOC
          </a-radio-button>
          <a-radio-button value="CO2">
            CO2
          </a-radio-button>
          <a-radio-button value="PM">
            PM2.5-10
          </a-radio-button>
        </a-radio-group>
      </a-col>
    </a-row>
  </div>
</template>

<script>
export default {
  name: "historyChart",
  data () {
    return {
      allHeight: document.body.clientHeight - 20,
      allWidth: document.body.clientWidth - 20,
      type: 'TVOC',
      optionTVOC: {},
      optionCO2: {},
      optionPM: {}
    }
  },
  mounted() {
    const that = this
    this.reDrawTVOCChart()
    this.reDrawCO2Chart()
    this.reDrawPMChart()
    window.onresize = () => {
      that.allHeight = document.body.clientHeight - 20
      that.allWidth = document.body.clientWidth - 40
      that.reDrawTVOCChart()
      that.reDrawCO2Chart()
      this.reDrawPMChart()
    }
  },
  methods: {
    reDrawTVOCChart() {
      this.optionTVOC = {
        backgroundColor: 'rgba(206, 212, 218, 0.1)',
        xAxis: [
          {
            type: 'category',
            boundaryGap: false,
            data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
          }
        ],
        legend: {
          data: ['甲醛(HCHO)', '挥发气体(TVOC)'],
          textStyle: {
            color: '#FFF'
          }
        },
        grid: {
          left: '2%',
          right: '2%',
          top: '10%',
          containLabel: true
        },
        tooltip: {
          trigger: 'axis',
          axisPointer: {
            type: 'line',
            label: {
              backgroundColor: '#6a7985'
            }
          }
        },
        yAxis: [
          {
            type: 'value',
            nameLocation: "end",
            name: "mg/㎥",
            splitLine: {
              lineStyle: {
                color: 'rgba(206,212,218,0.6)'
              }
            }
          }
        ],
        dataZoom: [
          {
            type: 'inside',
            start: 0,
            end: 80
          },
          {
            start: 0,
            end: 80
          }
        ],
        series: [
          {
            name: '甲醛(HCHO)',
            type: 'line',
            smooth: true,
            lineStyle: {
              opacity: 0.8,
              width: 3,
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
            emphasis: {
              focus: 'series'
            },
            data: [140, 232, 101, 264, 90, 340, 250]
          },
          {
            name: '挥发气体(TVOC)',
            type: 'line',
            smooth: true,
            lineStyle: {
              opacity: 0.8,
              width: 3,
              color: { //图形渐变颜色方法，四个数字分别代表，右，下，左，上，offset表示0%到100%
                type: 'linear',
                x: 0,
                y: 1,
                x2: 1, //从左到右 0-1
                y2: 0,
                colorStops: [{
                  offset: 0,
                  color: '#0575E6' // 0% 处的颜色
                }, {
                  offset: 1,
                  color: '#00F260' // 100% 处的颜色
                }],
                globalCoord: false // 缺省为 false
              }
            },
            emphasis: {
              focus: 'series'
            },
            data: [220, 302, 181, 234, 210, 290, 150]
          }
        ]
      }
    },
    reDrawCO2Chart() {
      this.optionCO2 = {
        backgroundColor: 'rgba(206, 212, 218, 0.1)',
        xAxis: [
          {
            type: 'category',
            boundaryGap: false,
            data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
          }
        ],
        legend: {
          data: ['二氧化碳(CO2)'],
          textStyle: {
            color: '#FFF'
          }
        },
        grid: {
          left: '2%',
          right: '2%',
          top: '10%',
          containLabel: true
        },
        tooltip: {
          trigger: 'axis',
          axisPointer: {
            type: 'line',
            label: {
              backgroundColor: '#6a7985'
            }
          }
        },
        yAxis: [
          {
            type: 'value',
            nameLocation: "end",
            name: "ppm",
            splitLine: {
              lineStyle: {
                color: 'rgba(206,212,218,0.6)'
              }
            }
          }
        ],
        dataZoom: [
          {
            type: 'inside',
            start: 0,
            end: 80
          },
          {
            start: 0,
            end: 80
          }
        ],
        series: [
          {
            name: '二氧化碳(CO2)',
            type: 'line',
            smooth: true,
            lineStyle: {
              opacity: 0.8,
              width: 3,
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
            emphasis: {
              focus: 'series'
            },
            data: [140, 232, 101, 264, 90, 340, 250]
          }
        ]
      }
    },
    reDrawPMChart() {
      this.optionPM = {
        backgroundColor: 'rgba(206, 212, 218, 0.1)',
        xAxis: [
          {
            type: 'category',
            boundaryGap: false,
            data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
          }
        ],
        legend: {
          data: ['PM2.5', 'PM5', 'PM10'],
          textStyle: {
            color: '#FFF'
          }
        },
        grid: {
          left: '2%',
          right: '2%',
          top: '10%',
          containLabel: true
        },
        tooltip: {
          trigger: 'axis',
          axisPointer: {
            type: 'line',
            label: {
              backgroundColor: '#6a7985'
            }
          }
        },
        yAxis: [
          {
            type: 'value',
            nameLocation: "end",
            name: "㎍/㎥",
            splitLine: {
              lineStyle: {
                color: 'rgba(206,212,218,0.6)'
              }
            }
          }
        ],
        dataZoom: [
          {
            type: 'inside',
            start: 0,
            end: 80
          },
          {
            start: 0,
            end: 80
          }
        ],
        series: [
          {
            name: 'PM2.5',
            type: 'line',
            smooth: true,
            lineStyle: {
              opacity: 0.8,
              width: 3,
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
            emphasis: {
              focus: 'series'
            },
            data: [140, 232, 101, 264, 90, 340, 250]
          },
          // {
          //   name: 'PM5',
          //   type: 'line',
          //   smooth: true,
          //   lineStyle: {
          //     opacity: 0.8,
          //     width: 3,
          //     color: { //图形渐变颜色方法，四个数字分别代表，右，下，左，上，offset表示0%到100%
          //       type: 'linear',
          //       x: 0,
          //       y: 1,
          //       x2: 1, //从左到右 0-1
          //       y2: 0,
          //       colorStops: [{
          //         offset: 0,
          //         color: '#0575E6' // 0% 处的颜色
          //       }, {
          //         offset: 1,
          //         color: '#00F260' // 100% 处的颜色
          //       }],
          //       globalCoord: false // 缺省为 false
          //     }
          //   },
          //   emphasis: {
          //     focus: 'series'
          //   },
          //   data: [220, 302, 181, 234, 210, 290, 150]
          // },
          {
            name: 'PM10',
            type: 'line',
            smooth: true,
            lineStyle: {
              opacity: 0.8,
              width: 3,
              color: { //图形渐变颜色方法，四个数字分别代表，右，下，左，上，offset表示0%到100%
                type: 'linear',
                x: 0,
                y: 1,
                x2: 1, //从左到右 0-1
                y2: 0,
                // colorStops: [{
                //   offset: 0,
                //   color: '#6be585' // 0% 处的颜色
                // }, {
                //   offset: 1,
                //   color: '#dd3e54' // 100% 处的颜色
                // }],
                colorStops: [{
                  offset: 0,
                  color: '#0575E6' // 0% 处的颜色
                }, {
                  offset: 1,
                  color: '#00F260' // 100% 处的颜色
                }],
                globalCoord: false // 缺省为 false
              }
            },
            emphasis: {
              focus: 'series'
            },
            data: [320, 132, 201, 334, 190, 130, 220]
          }
        ]
      }
    }
  }
}
</script>

<style>
.ant-radio-button-wrapper {
  background: rgba(206,212,218,0.6);
}
.ant-radio-group-solid .ant-radio-button-wrapper-checked:not(.ant-radio-button-wrapper-disabled):hover {
  background: linear-gradient(to bottom, #2CABFC, #CD48AE);
  border-color: rgba(206,212,218,0.6);
}

.ant-radio-group-solid .ant-radio-button-wrapper-checked:not(.ant-radio-button-wrapper-disabled){
  background: linear-gradient(to bottom, #2CABFC, #CD48AE);
  border-color: rgba(206,212,218,0.6);
}

.ant-radio-button-wrapper-checked:not(.ant-radio-button-wrapper-disabled):hover::before{
  background: rgba(206,212,218,0.6);
}

.ant-radio-button-wrapper > span{
  background-image: linear-gradient(to bottom, #2CABFC, #CD48AE);
  -webkit-background-clip: text;
  color: transparent;
}
.ant-radio-button-wrapper-checked > span{
  color: white ;
}
</style>
