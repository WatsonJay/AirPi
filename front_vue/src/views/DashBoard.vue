<template>
  <div :style="{height:allHeight+ 'px', width: allWidth + 'px', position: 'absolute'}">
    <div class="main" style="height: 70%">
      <a-row>
        <a-col :span="13">
          <v-chart autoresize :option="optionHCHO" :style="{width: allWidth * 0.55 + 'px',height: allHeight * 0.65 + 'px'}"/>
          <img :src="require('/src/assets/02.png')" width="400">
        </a-col>
        <a-col :span="11">

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
      AQILevel: ['#95F084', '#FFE696', '#FFAF6B', '#FF5758', '#9778FF', '#AD1775'],
      AQIStatus: ['优', '良', '轻度', '中度', '重度', '严重'],
      temp: 33,
      hum: 99,
      AQI: {value: 500, background: '#95F084', status: '优'},
      pm25: {value: 99.9, color: '#FF5758'},
      pm10: {value: 21, color: '#AD1775'},
      HCHO: {color: '#FFAF6B',value: 0.3  , status: '中度'},
      CO2: {color: '#FFAF6B',value: 9999, status: '立刻通风'},
      TVOC: {color: '#FFAF6B',value: 0.3},
      HCHO_chart: [200, -20],
      optionHCHO: {},
    }
  },
  mounted() {
    const that = this
    that.reDrawHCHOChart()
    // that.$socket.open()
  },
  beforeDestroy() {
    this.$socket.close()
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
      //this.$socket.emit('test')
    }
  },
  methods: {
    reDrawHCHOChart() {
       var  splitCount = 60, // 刻度数量
          pointerAngle = (this.HCHO_chart[0] - this.HCHO_chart[1]) * (0.5 - this.HCHO.value) / 0.5 + this.HCHO_chart[1]; // 当前指针（值）角度
      this.optionHCHO = {
        series: [{
          type: 'gauge',
          radius: '130%',
          startAngle: pointerAngle,
          endAngle: this.HCHO_chart[1],
          center: ["45%", "65%"],
          min: 0,
          max: 0.5,
          axisLine: {
            show: false
          },
          axisLabel:{
            show: false
          },
          axisTick:{
            length: 16,
            splitNumber: Math.ceil((0.5 - this.HCHO.value) / 0.5 * 7),
            lineStyle: {
              width: 3
            }
          },
          Z: 1
        }, {
          type: 'gauge',
          radius: '130%',
          startAngle: this.HCHO_chart[0],
          endAngle: pointerAngle,
          center: ["45%", "65%"],
          min: 0,
          max: 0.5,
          axisLine: {
            show: false
          },
          axisLabel:{
            show: false
          },
          axisTick:{
            length: 16,
            splitNumber: Math.ceil(this.HCHO.value / 0.5 * 7),
            lineStyle: {
              width: 3,
              color: '#fff'
            }
          },
          Z: 4,
        }, {
          type: 'gauge',
          radius: '90%',
          startAngle: this.HCHO_chart[0],
          endAngle: this.HCHO_chart[1],
          center: ["45%", "65%"],
          axisLine: {
            lineStyle: {
              width: 2,
              color: [[1, '#7f7f86']]
            }
          },
          axisLabel:{
            show: false
          },
          axisTick:{
            show: false
          },
          splitLine:{
            show: false
          },
          pointer: {
            show: false
          },
          title: {
            offsetCenter: ['-5%', '-10%'],
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
            offsetCenter: ['-55%', '60%'],
            valueAnimation: true,
            width: '60%',
            borderRadius: 8,
            formatter: function (value) {
              return '{a|'+value.toFixed(3) +'}{b|mg/m³}'
            },
            rich: {
              a: {
                fontSize: 50,
                fontWeight: 500,
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
        },]
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
  font-weight: 500;
  font-family: "digital-7";
}
</style>