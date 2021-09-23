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
    window.onresize = () => {
      that.allHeight = document.body.clientHeight - 20
      that.allWidth = document.body.clientWidth - 40
      that.reDrawTVOCChart()
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
            data: ['Line 1']
          },
          tooltip: {
            trigger: 'axis',
            axisPointer: {
              type: 'cross',
              label: {
                backgroundColor: '#6a7985'
              }
            }
          },
          yAxis: [
            {
              type: 'value',
              splitLine: {
                lineStyle: {
                  color: 'rgba(206,212,218,0.6)'
                }
              }
            }
          ],
          series: [
            {
              name: 'Line 1',
              type: 'line',
              stack: 'Total',
              smooth: true,
              // showSymbol: false,
              lineStyle: {
                opacity: 0.8,
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