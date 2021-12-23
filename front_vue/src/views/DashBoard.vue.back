<template>
  <div :style="{height:allHeight+ 'px', width: allWidth + 'px', margin: '10px 10px', position: 'absolute'}">
    <a-row>
      <a-col :span="5">
        <div class="PmDiv" :style="{height: allHeight * 0.23 + 'px','margin-top': '15px'}">
          <div style="background: #868e96; border-radius: 5px 5px 0 0 ;color: white">
            <span>PM2.5</span>
          </div>
          <div style="color: #c5f6fa">
            <span class="number" :style="{'font-size': allHeight * 0.14 + 'px', 'line-height': allHeight * 0.14 + 'px'}">{{pm25.value}}</span>
            <span> ㎍/㎥</span>
          </div>
          <div style="width: 80%;margin: 0 auto;border-radius: 2px" :style="{'border-bottom': '4px solid '+ this.pm25.color}" ></div>
        </div>
        <div class="PmDiv" :style="{height: allHeight * 0.23 + 'px','margin-top': '20px'}">
          <div style="background: #868e96; border-radius: 5px 5px 0 0 ;color: white">
            <span>PM10</span>
          </div>
          <div style="color: #c5f6fa">
            <span class="number" :style="{'font-size': allHeight * 0.14 + 'px', 'line-height': allHeight * 0.14 + 'px'}">{{pm10.value}}</span>
            <span> ㎍/㎥</span>
          </div>
          <div style="width: 80%;margin: 0 auto;border-radius: 2px" :style="{'border-bottom': '4px solid '+ this.pm10.color}" ></div>
        </div>
        <div style="border-radius: 6px; padding: 0 5px; box-shadow: 3px 2px 6px #343a40; margin-top: 20px; color: #e9ecef"
             :style="{background: AQI.background, 'margin-top': allHeight * 0.2 + 23 + 'px'}">
          <span style="text-align: left" :style="{'font-size': allHeight * 0.035 + 'px'}">空气质量指数</span>
          <span class="number" style="text-align: right;display: block" :style="{'font-size': allHeight * 0.11 + 'px', 'line-height': allHeight * 0.11 + 'px'}">{{AQI.value}}</span>
        </div>
      </a-col>
      <a-col :span="10">
        <v-chart autoresize :option="optionTVOC" :style="{height: allHeight * 0.5 + 'px'}"></v-chart>
        <v-chart autoresize :option="optionCO2" :style="{height: allHeight * 0.5 + 'px'}"></v-chart>
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
  data() {
    return {
      allHeight: document.body.clientHeight - 20,
      allWidth: document.body.clientWidth - 20,
      timer: '',
      temp: 33.99,
      hum: 99.99,
      AQILevel: ['#00E400', '#FFFF00', '#FF7E00', '#FF0000', '#99004C', '#7E0023'],
      statusLevel: ['优', '良', '轻度', '中度', '重度', '严重'],
      pm25: {value: 99, color: '#7E0023'},
      pm10: {value: 21, color: '#7E0023'},
      AQI: {value: 0, background: '#FF0000'},
      HCHO: {color: '#FF7E00',value: 0.3, status: '中度'},
      CO2: {color: '#FF7E00',value: 9999, status: '立刻通风'},
      TVOC: {color: '#FF7E00',value: 0.3, status: '优'},
      optionHCHO: {},
      optionCO2: {},
      optionTVOC: {},
    }
  },
  mounted() {
    const that = this
    // this.refreshData()
    // this.timer = setInterval(this.refreshData, 62000);
    this.$socket.open()
    window.onresize = () => {
      that.allHeight = document.body.clientHeight - 20
      that.allWidth = document.body.clientWidth - 40
      that.reDrawHCHOChart()
      that.reDrawCO2()
      that.reDrawTVOC()
    }
  },
  beforeDestroy() {
    this.$socket.close()
    clearInterval(this.timer);
  },
  sockets: {
    connecting() {
      console.log('正在连接')
    },
    disconnect() {
      console.log("Socket 断开");
    },
    connect_failed() {
      console.log('连接失败')
    },
    server_response(data) {
      console.log(data)
    },
    connect() {
      console.log('socket connected')
      this.$socket.emit('test')
    }
  },
  methods: {
    refreshData(){
      this.$api.air.getDashData().then(res=> {
        // 执行某些操作
        if(res.success) {
          this.pm25.value = res.data['pm25']
          this.selectPM25Color(res.data['pm25'])
          this.pm25.value = res.data['pm10']
          this.selectPM10Color(res.data['pm10'])
          this.HCHO.value = res.data['hcho'] / 1000
          this.selectHCHOColor(res.data['hcho'])
          this.CO2.value = res.data['co2']
          this.selectCo2Color(res.data['co2'])
          this.TVOC.value = res.data['tvoc'] / 1000
          this.selectTVOCColor(res.data['tvoc'])
          this.temp = res.data['temp']
          this.hum = res.data['hum']
          this.reDrawHCHOChart()
          this.reDrawCO2()
          this.reDrawTVOC()
        }
      })
    },
    selectPM25Color(value){
      switch (true){
        case value < 35:
          this.pm25.color = this.AQI.background = this.AQILevel[0];
          this.AQI.value = Math.round(50/35*value);
          break;
        case value < 75:
          this.pm25.color = this.AQI.background = this.AQILevel[1];
          this.AQI.value = Math.round((100 - 51)/(75 - 35)*(value - 35) + 51);
          break;
        case value < 115:
          this.pm25.color = this.AQI.background = this.AQILevel[2];
          this.AQI.value = Math.round((150 - 101)/(115 - 75)*(value - 75) + 101);
          break;
        case value < 150:
          this.pm25.color = this.AQI.background = this.AQILevel[3];
          this.AQI.value = Math.round((200 - 151)/(150 - 115)*(value - 115) + 151);
          break;
        case value < 250:
          this.pm25.color = this.AQI.background = this.AQILevel[4];
          this.AQI.value = Math.round((300 - 201)/(250 - 150)*(value - 150) + 201);
          break;
        default:
          this.pm25.color = this.AQI.background = this.AQILevel[5];
          this.AQI.value = Math.round((500 - 301)/(500 - 250)*(value - 250) + 301);
          break;
      }
    },
    selectPM10Color(value){
      switch (true){
        case value < 35:
          this.pm10.color = this.AQILevel[0];break;
        case value < 75:
          this.pm10.color = this.AQILevel[1];break;
        case value < 115:
          this.pm10.color = this.AQILevel[2];break;
        case value < 150:
          this.pm10.color = this.AQILevel[3];break;
        case value < 250:
          this.pm10.color = this.AQILevel[4];break;
        default:
          this.pm10.color = this.AQILevel[5];break;
      }
    },
    selectHCHOColor(value){
      switch (true) {
        case value < 50:
          this.HCHO.color = this.AQILevel[0];
          this.HCHO.status = this.statusLevel[0];
          break;
        case value < 100:
          this.HCHO.color = this.AQILevel[1];
          this.HCHO.status = this.statusLevel[1];
          break;
        case value < 200:
          this.HCHO.color = this.AQILevel[2];
          this.HCHO.status = this.statusLevel[2];
          break;
        case value < 300:
          this.HCHO.color = this.AQILevel[3];
          this.HCHO.status = this.statusLevel[2];
          break;
        case value < 400:
          this.HCHO.color = this.AQILevel[4];
          this.HCHO.status = this.statusLevel[2];
          break;
        default:
          this.HCHO.color = this.AQILevel[5];
          this.HCHO.status = this.statusLevel[2];
          break;
      }
    },
    selectTVOCColor(value){
      switch (true) {
        case value < 300:
          this.TVOC.color = this.AQILevel[0];
          this.TVOC.status = this.statusLevel[0];
          break;
        case value < 600:
          this.TVOC.color = this.AQILevel[1];
          this.TVOC.status = this.statusLevel[1];
          break;
        case value < 1200:
          this.TVOC.color = this.AQILevel[2];
          this.TVOC.status = this.statusLevel[2];
          break;
        case value < 1800:
          this.TVOC.color = this.AQILevel[3];
          this.TVOC.status = this.statusLevel[2];
          break;
        case value < 2400:
          this.TVOC.color = this.AQILevel[4];
          this.TVOC.status = this.statusLevel[2];
          break;
        default:
          this.TVOC.color = this.AQILevel[5];
          this.TVOC.status = this.statusLevel[2];
          break;
      }
    },
    selectCo2Color(value){
      switch (true) {
        case value < 400:
          this.CO2.color = this.AQILevel[0];
          this.CO2.status = '清新';
          break;
        case value < 800:
          this.CO2.color = this.AQILevel[1];
          this.CO2.status = '稍闷';
          break;
        case value < 1200:
          this.CO2.color = this.AQILevel[2];
          this.CO2.status = '需通风';
          break;
        default:
          this.CO2.color = this.AQILevel[3];
          this.CO2.status = '立刻通风';
          break;
      }
    },
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
            value: this.HCHO.value,
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
                width: 65,
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
              value: this.CO2.value,
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
            offsetCenter: ['65%', '65%'],
            formatter: function (value) {
              return '{a|' + (value).toFixed(3) + '}{b|mg/m³}'
            },
            rich: {
              a: {
                fontSize: 40,
                fontWeight: 800,
                fontFamily: 'digital-7',
                lineHeight: 40,
                width: 90,
                color: '#e9ecef',
                align: 'left'
              },
              b: {
                lineHeight: 24,
                color: '#e9ecef',
                left:30,
                fontFamily: 'pingfang',
                align: 'left'
              }
            }
          },
          data: [{
            value: this.TVOC.value,
            name: '挥发气体\n{c|' + this.TVOC.status+ '}'
          }]
        }]
      }
    }
  },
}
</script>

<style scoped>
.PmDiv {
  border-radius: 5px;
  box-shadow: 3px 2px 6px #343a40;
  background: hsla(0,0%,100%,.2);
}
.number {
  color: #e9ecef;
  font-weight: 800;
  text-shadow: 1px 1px 5px #adb5bd;
  font-family: "digital-7";
}
</style>
