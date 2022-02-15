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
      xAxis: [],
      hcho: [],
      tvoc: [],
      co2: [],
      pm10: [],
      pm25: [],
      optionTVOC: {},
      optionCO2: {},
      optionPM: {}
    }
  },
  mounted() {
    const that = this
    this.refreshData()
    this.timer = setInterval(this.refreshData, 120000);
    window.onresize = () => {
      that.allHeight = document.body.clientHeight - 20
      that.allWidth = document.body.clientWidth - 40
      that.reDrawTVOCChart()
      that.reDrawCO2Chart()
      this.reDrawPMChart()
    }
  },
  destroyed() {
    window.clearInterval(this.timer);
    this.timer = null;
  },
  methods: {
    refreshData(){
      this.$api.air.getHistoryData().then(res=> {
        // 执行某些操作
        debugger
        if(res.success) {
          this.xAxis = res.data.createtime
          this.hcho = res.data.hcho
          this.tvoc = res.data.tvoc
          this.co2 = res.data.co2
          this.pm25 = res.data.pm25
          this.pm10 = res.data.pm10
          this.reDrawTVOCChart()
          this.reDrawCO2Chart()
          this.reDrawPMChart()
        }
      })
    },
    reDrawTVOCChart() {
      this.optionTVOC = {
        backgroundColor: 'rgba(206, 212, 218, 0.1)',
        xAxis: [
          {
            type: 'category',
            boundaryGap: false,
            data: this.xAxis
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
            start: 20,
            end: 100
          },
          {
            start: 20,
            end: 100
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
            data: this.hcho
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
            data: this.tvoc
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
            data: this.xAxis
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
            start: 20,
            end: 100
          },
          {
            start: 20,
            end: 100
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
            data: this.co2
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
            data: this.xAxis
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
            start: 20,
            end: 100
          },
          {
            start: 20,
            end: 100
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
            data: this.pm25
          },
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
            data: this.pm10
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
