<template>
  <div :style="{height:allHeight+ 'px', width: allWidth + 'px', position: 'absolute'}">
    <div class="main" style="height: 70%">
      <a-row>
        <a-col :span="11">
          <v-chart autoresize :option="optionHCHO" :style="{width: allWidth * 0.45 + 'px',height: allHeight * 0.65 + 'px'}"/>
          <img :src="require('/src/assets/02.png')" width="400">
        </a-col>
        <a-col :span="13">
          <v-chart autoresize :option="optionCO2" :style="{width: allWidth * 0.5 + 'px',height: allHeight * 0.325 + 'px'}"/>
          <v-chart autoresize :option="optionPM25" :style="{width: allWidth * 0.5 + 'px',height: allHeight * 0.325 + 'px'}"/>
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
              <div style="width: 50px;height: 26px;margin: 5px auto;border-radius: 2px" :style="{'background': this.AQI.color}" >
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
      AQI: {value: 500, color: '#95F084', status: '优'},
      pm25: {value: 0.25, color: '#FF5758', status: '中度'},
      pm10: {value: 0.34, color: '#AD1775'},
      HCHO: {color: '#FFAF6B',value: 0.3, status: '中度'},
      CO2: {color: '#FFAF6B',value: 2200, status: '立刻通风'},
      TVOC: {color: '#FFAF6B',value: 0.3},
      HCHO_chart: [200, -20],
      CO2_small_chart: {
        range: [280, -10],
        center: ["20%", "52%"],
        maxValue: 3200,
        unit: 'PPM',
        tipWidth: 70,
        title: '二氧化碳',
        titleWidth: 100,
        titleOffset:['350%','-15%'],
        valueWidth: 90
      },
      PM25_small_chart: {
        range: [280, -10],
        center: ["35%", "52%"],
        maxValue: 0.35,
        unit: 'mg/m³',
        tipWidth: 50,
        title: 'PM2.5',
        titleWidth: 70,
        titleOffset:['300%','-15%'],
        valueWidth: 70
      },
      optionHCHO: {},
      optionCO2: {},
      optionPM25: {},
    }
  },
  mounted() {
    const that = this
    that.drawHCHOChart()
    that.optionCO2 = that.drawSmallChart(this.CO2, this.CO2_small_chart)
    that.optionPM25 = that.drawSmallChart(this.pm25, this.PM25_small_chart)
    // that.$socket.open()
  },
  beforeDestroy() {
    this.$socket.close()
    this.optionHCHO = {}
    this.optionCO2 = {}
    this.optionPM25 = {}
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
      //数据初始化
    },
    connect() {
      console.log('socket connected')
      //this.$socket.emit('test')
    }
  },
  methods: {
    //HCHO图表处理
    drawHCHOChart() {
       var  splitCount = 7, // 刻度数量
           max = 0.5, //比例最大值
           pointerAngle = (this.HCHO_chart[0] - this.HCHO_chart[1]) * (0.5 - this.HCHO.value) / 0.5 + this.HCHO_chart[1], // 当前指针（值）角度
           tickColor = { //图形渐变颜色方法，四个数字分别代表，右，下，左，上，offset表示0%到100%
             type: 'linear',
             x: 1,
             y: 1,
             x2: 0, //从左到右 0-1
             y2: 0,
             colorStops: [{
               offset: 0,
               color: '#CD48AE' // 0% 处的颜色
             }, {
               offset: 1,
               color: '#2CABFC' // 100% 处的颜色
             }],
             globalCoord: false // 缺省为 false
           };
      this.optionHCHO = {
        series: [{
          type: 'gauge',
          radius: '130%',
          startAngle: pointerAngle,
          endAngle: this.HCHO_chart[1],
          center: ["50%", "65%"],
          axisLine: {
            show: false
          },
          axisLabel:{
            show: false
          },
          splitNumber: 9,
          axisTick:{
            length: 16,
            splitNumber: Math.ceil((max - this.HCHO.value) / max * splitCount),
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
          center: ["50%", "65%"],
          max: 1,
          axisLine: {
            show: false
          },
          axisLabel:{
            show: false
          },
          splitNumber: 9,
          splitLine:{
            show: false,
          },
          pointer: {
            icon: 'rect',
            offsetCenter: [0, '-77%'],
            width: 3,
            length: 22,
            itemStyle: {
              color: tickColor
            }
          },
          axisTick:{
            length: 16,
            splitNumber: Math.ceil(this.HCHO.value / max * splitCount),
            lineStyle: {
              width: 3,
              color: tickColor
            }
          },
          data: [{
            value: 1
          }],
          Z: 4,
        }, {
          type: 'gauge',
          radius: '90%',
          startAngle: this.HCHO_chart[0],
          endAngle: this.HCHO_chart[1],
          center: ["50%", "65%"],
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
            offsetCenter: ['-5%', '-12%'],
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
            offsetCenter: ['-52.5%', '55%'],
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
    //小图表处理
    drawSmallChart(type, setting) {
      var chartOption = {};
      var splitCount = 5, // 刻度数量
          pointerAngle = (setting.range[0] - setting.range[1]) * (setting.maxValue - type.value) / setting.maxValue + setting.range[1], // 当前指针（值）角度
          tickColor = { //图形渐变颜色方法，四个数字分别代表，右，下，左，上，offset表示0%到100%
            type: 'linear',
            x: 1,
            y: 1,
            x2: 0, //从左到右 0-1
            y2: 0,
            colorStops: [{
              offset: 0,
              color: '#CD48AE' // 0% 处的颜色
            }, {
              offset: 1,
              color: '#2CABFC' // 100% 处的颜色
            }],
            globalCoord: false // 缺省为 false
          };
      chartOption = {
        series: [{
          type: 'gauge',
          radius: '130%',
          startAngle: pointerAngle,
          endAngle: setting.range[1],
          center: setting.center,
          axisLine: {
            show: false
          },
          axisLabel:{
            show: false
          },
          splitLine:{
            show: false,
          },
          splitNumber: 9,
          axisTick:{
            length: 10,
            splitNumber: Math.ceil((setting.maxValue - type.value) / setting.maxValue * splitCount),
            lineStyle: {
              width: 3
            }
          },
          Z: 1
        }, {
          type: 'gauge',
          radius: '130%',
          startAngle: setting.range[0],
          endAngle: pointerAngle,
          center: setting.center,
          axisLine: {
            show: false
          },
          axisLabel:{
            show: false
          },
          splitNumber: 9,
          splitLine:{
            show: false,
          },
          pointer: {
            show: false
          },
          axisTick:{
            length: 10,
            splitNumber: Math.ceil(type.value / setting.maxValue * splitCount),
            lineStyle: {
              width: 3,
              color: tickColor
            }
          },
          Z: 4,
        }, {
          type: 'gauge',
          radius: '70%',
          startAngle: setting.range[0],
          endAngle: setting.range[1],
          center: setting.center,
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
            offsetCenter: setting.titleOffset,
            color: '#e9ecef',
            rich: {
              c: {
                height: 20,
                fontSize: 16,
                fontFamily: 'pingfang',
                width: setting.tipWidth,
                borderRadius: 4,
                color: '#fff',
                backgroundColor: type.color,
                align: 'center'
              },
              t: {
                fontSize: 23,
                fontFamily: 'pingfang',
                width: setting.titleWidth,
                color: '#fff',
                align: 'center'
              }
            },
            fontSize: document.body.clientHeight * 0.08,
          },
          detail: {
            offsetCenter: ['120%', '95%'],
            valueAnimation: true,
            width: '60%',
            borderRadius: 8,
            formatter: function (value) {
              return '{a|'+ value +'}{b|' + setting.unit + '}'
            },
            rich: {
              a: {
                fontSize: 40,
                fontWeight: 500,
                fontFamily: 'digital-7',
                width: setting.valueWidth,
                lineHeight: 40,
                color: '#e9ecef',
                align: 'left'
              },
              b: {
                lineHeight: 30,
                fontSize: 15,
                fontFamily: 'pingfang',
                color: '#fff',
                align: 'left'
              }
            }
          },
          data: [{
            value: type.value,
            name: '{t|' +setting.title + '}{c|' + type.status+ '}'
          }]
        },]
      }
      return chartOption;
    },
    //PM25/AQI颜色匹配
    selectPM25Color(value){
      switch (true){
        case value <= 35:
          this.pm25.color = this.AQI.color = this.AQILevel[0];
          this.pm25.status = this.AQI.status = this.AQIStatus[0];
          this.AQI.value = Math.round(50/35*value);
          break;
        case value <= 75:
          this.pm25.color = this.AQI.color = this.AQILevel[1];
          this.pm25.status = this.AQI.status = this.AQIStatus[1];
          this.AQI.value = Math.round((100 - 51)/(75 - 35)*(value - 35) + 51);
          break;
        case value <= 115:
          this.pm25.color = this.AQI.color = this.AQILevel[2];
          this.pm25.status = this.AQI.status = this.AQIStatus[2];
          this.AQI.value = Math.round((150 - 101)/(115 - 75)*(value - 75) + 101);
          break;
        case value <= 150:
          this.pm25.color = this.AQI.color = this.AQILevel[3];
          this.pm25.status = this.AQI.status = this.AQIStatus[3];
          this.AQI.value = Math.round((200 - 151)/(150 - 115)*(value - 115) + 151);
          break;
        case value <= 250:
          this.pm25.color = this.AQI.color = this.AQILevel[4];
          this.pm25.status = this.AQI.status = this.AQIStatus[4];
          this.AQI.value = Math.round((300 - 201)/(250 - 150)*(value - 150) + 201);
          break;
        default:
          this.pm25.color = this.AQI.color = this.AQILevel[5];
          this.pm25.status = this.AQI.status = this.AQIStatus[5];
          this.AQI.value = Math.round((500 - 301)/(500 - 250)*(value - 250) + 301);
          break;
      }
    },
    //PM10颜色匹配
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
    //HCHO颜色匹配
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
          this.HCHO.status = this.statusLevel[3];
          break;
        case value < 400:
          this.HCHO.color = this.AQILevel[4];
          this.HCHO.status = this.statusLevel[4];
          break;
        default:
          this.HCHO.color = this.AQILevel[5];
          this.HCHO.status = this.statusLevel[5];
          break;
      }
    },
    //TVOC颜色匹配
    selectTVOCColor(value){
      switch (true) {
        case value < 300:
          this.TVOC.color = this.AQILevel[0];
          break;
        case value < 600:
          this.TVOC.color = this.AQILevel[1];
          break;
        case value < 1200:
          this.TVOC.color = this.AQILevel[2];
          break;
        case value < 1800:
          this.TVOC.color = this.AQILevel[3];
          break;
        case value < 2400:
          this.TVOC.color = this.AQILevel[4];
          break;
        default:
          this.TVOC.color = this.AQILevel[5];
          break;
      }
    },
    //CO2颜色匹配
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
