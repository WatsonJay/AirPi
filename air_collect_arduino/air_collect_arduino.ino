//--------库引用---------//
#include <EEPROM.h>
#include <ESP8266WiFi.h>
#include <ESP8266WebServer.h>
#include <DNSServer.h>
#include <FS.h>
#include <PubSubClient.h>
#include <SimpleTimer.h>
#include <Hash.h>
#include <ArduinoJson.h>
#define LENG 16 //0x3c + 0x2 + 15 bytes equal to 17 bytes
//--------变量定义---------//
#define DEFAULT_STASSID ""
#define DEFAULT_STAPSW  ""
#define DEFAULT_MTQQIP  ""
#define DEFAULT_MTQQUSER  ""
#define DEFAULT_MTQQPASS  ""
#define MAGIC_NUMBER 0xAA
struct env_data
{
  int co2;
  int hcho;
  int tvoc;
  int pm25;
  int pm10;
  int temp;
  int hum;
};
env_data esp_data;
unsigned char buf[32];
IPAddress ApHost(192, 168, 4, 1);
const byte DNS_PORT = 53;
const char* AP_NAME = "smart_air";
struct rom_config
{
  char stassid[70];
  char stapsw[100];
  char mqttIp[50];
  char mqttUser[50];
  char mqttPass[50];
  uint8_t magic;
};
rom_config rom_wifi;
//--------WIFI参数--------//
WiFiClient espClient;
PubSubClient client(espClient);
ESP8266WebServer server(80);
DNSServer dnsServer;
String WIFI_SSID = "";
String WIFI_PASS = "";
//--------mqtt参数--------------//
const char *topic = "airPi/data";
const int mqtt_port = 1883;
const int mqtt_sended = 0;
//--------EEPROM写入与读取--------//
void loadRomConfig(){
  uint8_t *p = (uint8_t*)(&rom_wifi);
  for (int i = 0; i < sizeof(rom_wifi); i++)
  {
    *(p + i) = EEPROM.read(i);
  }
  if (rom_wifi.magic != MAGIC_NUMBER)
  {
    strcpy(rom_wifi.stassid, DEFAULT_STASSID);
    strcpy(rom_wifi.stapsw, DEFAULT_STAPSW);
    strcpy(rom_wifi.mqttIp, DEFAULT_MTQQIP);
    strcpy(rom_wifi.mqttUser, DEFAULT_MTQQUSER);
    strcpy(rom_wifi.mqttPass, DEFAULT_MTQQPASS);
    rom_wifi.magic = MAGIC_NUMBER;
    saveRomConfig();
    Serial.println("Restore config!");
  }
  Serial.println(" ");
  Serial.println("-------PRINT EEPROM CONFIG-------\n");
  Serial.print("stassid:");
  Serial.println(rom_wifi.stassid);
  Serial.print("stapsw:");
  Serial.println(rom_wifi.stapsw);
  Serial.print("mqttIp:");
  Serial.println(rom_wifi.mqttIp);
  Serial.print("mqttUser:");
  Serial.println(rom_wifi.mqttUser);
  Serial.print("mqttPass:");
  Serial.println(rom_wifi.mqttPass);
  Serial.println("--------------------------\n");
}

void saveRomConfig(){
  Serial.println("-------EEPROM save config-------\n");
  Serial.print("stassid:");
  Serial.println(rom_wifi.stassid);
  Serial.print("stapsw:");
  Serial.println(rom_wifi.stapsw);
  Serial.print("mqttIp:");
  Serial.println(rom_wifi.mqttIp);
  Serial.print("mqttUser:");
  Serial.println(rom_wifi.mqttUser);
  Serial.print("mqttPass:");
  Serial.println(rom_wifi.mqttPass);
  uint8_t *p = (uint8_t*)(&rom_wifi);
  for (int i = 0; i < sizeof(rom_wifi); i++)
  {
    EEPROM.write(i, *(p + i));
  }
  EEPROM.commit();
}
//--------WIFI(AP)初始化--------//
void initWiFiAp() {
  WiFi.mode(WIFI_AP_STA);
  Serial.println("-------WIFI启动为AP模式-------\n");
  WiFi.hostname("AIR-ESP8266");
  WiFi.softAPConfig(ApHost, ApHost, IPAddress(255, 255, 255, 0));
  if(WiFi.softAP(AP_NAME)){
    Serial.println("-------ESP8266 softAP 运行中-------\n");
    Serial.print("AP IP address: ");
    Serial.println(WiFi.softAPIP());
    dnsServer.setErrorReplyCode(DNSReplyCode::NoError);
    if(dnsServer.start(DNS_PORT, "*", ApHost)){
      Serial.println("\n-------dns server 工作中-------");
    }else{
      Serial.println("\n-------dns server 启动失败-------");
    }
  }
}
//--------wifi连接--------//
bool wifi_init() {
  Serial.print("Connected to :");
  Serial.println(rom_wifi.stassid);
  WiFi.begin(rom_wifi.stassid, rom_wifi.stapsw);
  int t = 0;
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
    t++;
    if (t > 10) {
      return false;
    }
  }
  Serial.print("\nIP address: ");
  Serial.println(WiFi.localIP());
  return true;
}

//--------web服务器初始化--------//
void initWebServer(){ //配置web服务器
  server.on("/", HTTP_GET, handleIndex);
  server.on("/wifiInfo", HTTP_GET, handleSendWifiInfo);
  server.on("/wifiList", HTTP_GET, handleSendWifiList);
  server.on("/wifiSetting", HTTP_POST, handleSetWifi);
  server.on("/mqttInfo", HTTP_GET, handleSendMqttInfo);
  server.on("/mqttSetting", HTTP_POST, handleSetMqtt);
  server.onNotFound(handleNotFound);
  server.begin();
  Serial.println("-------web server 工作中-------");
}

//首页
void handleIndex() {
  Serial.print("加载主页");
  File file = SPIFFS.open("/index.html", "r");
  size_t sent = server.streamFile(file, "text/html");
  file.close();
}

//回填wifi info
void handleSendWifiInfo() {
  int nNetwork = WiFi.scanNetworks();
  DynamicJsonDocument res(1024);
  res["code"] = 200;
  if(WiFi.status() == WL_CONNECTED){
	res["result"]["SSID"] = WiFi.SSID();
	res["result"]["localIP"] = WiFi.localIP();
	res["result"]["gatewayIP"] = WiFi.gatewayIP();
  }else{
	res["result"]["SSID"] = "";
	res["result"]["localIP"] = "";
	res["result"]["gatewayIP"] = "";
  }
  String WifiInfo = "";
  serializeJson(res, WifiInfo);
  res.clear();
  server.send(200, "application/json", WifiInfo);
}

//回填wifi list
void handleSendWifiList() {
  int nNetwork = WiFi.scanNetworks();
  DynamicJsonDocument res(2048);
  res["code"] = 200;
  for (int i = 0; i < nNetwork; i++) {
    res["result"][i]["SSID"] = WiFi.SSID(i);
    res["result"][i]["RSSI"] = 2 * (WiFi.RSSI(i)+100);
  }
  String WifiList = "";
  serializeJson(res, WifiList);
  res.clear();
  server.send(200, "application/json", WifiList);
}

//提交wifi设置
void handleSetWifi() {
  DynamicJsonDocument res(500);
  DynamicJsonDocument req(500);
  String JsonString = server.arg("plain");
  deserializeJson(req, JsonString);
  JsonObject root = req.as<JsonObject>();
  const String wifiName = root["wifiName"];
  const String wifiPassword = root["wifiPass"];
  wifiName.toCharArray(rom_wifi.stassid, wifiName.length() + 1);
  wifiPassword.toCharArray(rom_wifi.stapsw, wifiPassword.length() + 1);
  req.clear();
  res["code"] = 200;
  String result = "";
  if (wifi_init()) {
	  res["result"] = "success";
  }else{
	  res["result"] = "false";
	  res["data"] = "wifi连接失败";
  }
  serializeJson(res, result);
  res.clear();
  server.send(200, "application/json", result);
  saveRomConfig();
}

//回填mqtt info
void handleSendMqttInfo() {
  DynamicJsonDocument res(1024);
  res["code"] = 200;
  if(WiFi.status() == WL_CONNECTED){
  res["result"]["mqttIp"] = rom_wifi.mqttIp;
  res["result"]["isSended"] = mqtt_sended;
  }else{
  res["result"]["mqttIp"] = "";
  res["result"]["isSended"] = "";
  }
  String mqttInfo = "";
  serializeJson(res, mqttInfo);
  res.clear();
  server.send(200, "application/json", mqttInfo);
}

//提交mqtt设置
void handleSetMqtt() {
  DynamicJsonDocument res(500);
  DynamicJsonDocument req(500);
  String JsonString = server.arg("plain");
  deserializeJson(req, JsonString);
  JsonObject root = req.as<JsonObject>();
  const String mqttIp = root["mqttIP"];
  const String mqttUser = root["mqttUser"];
  const String mqttPass = root["mqttPass"];
  mqttIp.toCharArray(rom_wifi.mqttIp, mqttIp.length() + 1);
  mqttUser.toCharArray(rom_wifi.mqttUser, mqttUser.length() + 1);
  mqttPass.toCharArray(rom_wifi.mqttPass, mqttPass.length() + 1);
  req.clear();
  res["code"] = 200;
  String result = "";
  if (wifi_init()) {
    res["result"] = "success";
  }else{
    res["result"] = "false";
    res["data"] = "mtqq设置失败";
  }
  serializeJson(res, result);
  res.clear();
  server.send(200, "application/json", result);
  saveRomConfig();
}

String getContentType(String filename) { //判断请求类型
  if (server.hasArg("download")) return "application/octet-stream";
  else if (filename.endsWith(".htm")) return "text/html";
  else if (filename.endsWith(".html")) return "text/html";
  else if (filename.endsWith(".css")) return "text/css";
  else if (filename.endsWith(".js")) return "application/javascript";
  else if (filename.endsWith(".png")) return "image/png";
  else if (filename.endsWith(".gif")) return "image/gif";
  else if (filename.endsWith(".jpg")) return "image/jpeg";
  else if (filename.endsWith(".ico")) return "image/x-icon";
  else if (filename.endsWith(".xml")) return "text/xml";
  else if (filename.endsWith(".pdf")) return "application/x-pdf";
  else if (filename.endsWith(".zip")) return "application/x-zip";
  else if (filename.endsWith(".gz")) return "application/x-gzip";
  else return "text/plain";
}

void handleNotFound() { //无对应请求
  String path = server.uri();
  Serial.print("load url:");
  Serial.println(path);
  String contentType = getContentType(path);

  if (SPIFFS.exists(path)) {
    File file = SPIFFS.open(path, "r");
    size_t sent = server.streamFile(file, contentType);
    file.close();
    return;
  } else {
    if(WiFi.status() == WL_CONNECTED){
      String message = "File Not Found\n\n";
      message += "URI: ";
      message += server.uri();
      message += "\nMethod: ";
      message += ( server.method() == HTTP_GET ) ? "GET" : "POST";
      message += "\nArguments: ";
      message += server.args();
      message += "\n";
      for ( uint8_t i = 0; i < server.args(); i++ ) {
        message += " " + server.argName ( i ) + ": " + server.arg ( i ) + "\n";
      }
      server.send ( 404, "text/plain", message );
    }else{
      File file = SPIFFS.open("/index.html", "r");
      size_t sent = server.streamFile(file, "text/html");
      file.close();
    }
  }
}
//--------setup()---------//
void setup() {
  Serial.begin(9600);
  EEPROM.begin(1024);
  if(SPIFFS.begin()){ // 启动SPIFFS
    Serial.println("-------SPIFFS 已启动-------");
  } else {
    Serial.println("-------SPIFFS 启动失败-------");
  }
  initWiFiAp();
  Serial.println("-------WIFI 初始化完成-------");
  initWebServer();
  Serial.println("-------webServer 初始化完成-------");
  loadRomConfig();
  Serial.println("-------EEPROM 读取完成-------");
  if (WiFi.status() != WL_CONNECTED){
    wifi_init();
  }
}

void loop() {
  if (WiFi.status() == WL_CONNECTED){
     if(rom_wifi.mqttIp != ""){
        client.setServer(rom_wifi.mqttIp, mqtt_port);
        if(!client.connected()){
          String client_id = "esp8266-client-";
          client_id += String(WiFi.macAddress());
          Serial.printf("The client %s connects to the public mqtt broker\n", client_id.c_str());
          if (client.connect(client_id.c_str(), rom_wifi.mqttUser, rom_wifi.mqttPass)) {
             Serial.println("Public emqx mqtt broker connected");
          }
        }
     }
     if(Serial.find(0x3c)){
        Serial.readBytes(buf,LENG);
        if(buf[0] == 0x2){
          Serial.println("get data");
          if(checkValue(buf,LENG)){
            Serial.println("check right");
            esp_data.co2 = ((buf[1]<<8) + buf[2]);
            esp_data.hcho = ((buf[3]<<8) + buf[4]);
            esp_data.tvoc = ((buf[5]<<8) + buf[6]);
            esp_data.pm25 = ((buf[7]<<8) + buf[8]);
            esp_data.pm10 = ((buf[9]<<8) + buf[10]);
            esp_data.temp = (String(buf[11]) + '.' + String(buf[12])).toFloat();
            esp_data.hum = (String(buf[13]) + '.' + String(buf[14])).toFloat();
            Serial.println((String)"co2:" + esp_data.co2 +",hcho:"+esp_data.hcho+",tvoc:"+esp_data.tvoc+",pm25:"+esp_data.pm25+",pm10:"+esp_data.pm10+",temp:"+esp_data.temp+",hum:"+esp_data.hum);
            if(client.connected()){
                client.publish(topic, ((String)esp_data.co2+","+esp_data.hcho+","+esp_data.tvoc+","+esp_data.pm25+","+esp_data.pm10+","+esp_data.temp+","+esp_data.hum).c_str());
            }
          }else{
            Serial.println("check error");
          }
        }
     }
  }
  server.handleClient();
}

char checkValue(unsigned char *thebuf, char leng)
{  
  char receiveflag=0;
  int receiveSum=0;
 
  for(int i=0; i<(leng-1); i++){
    receiveSum=receiveSum+thebuf[i];
  }
  receiveSum=receiveSum + 0x3c;
 
  if(receiveSum % 256 == thebuf[leng-1])  //check the serial data 
  {
    receiveSum = 0;
    receiveflag = 1;
  }
  return receiveflag;
}

//data 3c0201a6000c00170019001f1f024407ac3c0201a6000c0018001a00201f02443c02019d000c001a0018001d1f024404a03c02019d000c001b0018001d1f024404a13c02019d000c001c0018001d1f024405a33c02019e000c001d0018001d1f024404a43c02019f000c001e0018001d1f024404a6
