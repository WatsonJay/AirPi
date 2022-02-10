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

//--------变量定义---------//
IPAddress ApHost(192, 168, 4, 1);
const byte DNS_PORT = 53;
const char* AP_NAME = "smart_air";
ESP8266WebServer server(80);
DNSServer dnsServer;
//--------WIFI参数--------//
WiFiClient espClient;
PubSubClient client(espClient);
//--------EEPROM写入与读取--------//

//--------WIFI(AP)初始化--------//
void initWiFiAp() {
  WiFi.mode(WIFI_AP_STA);
  Serial.println("-------WIFI启动为AP模式-------");
  WiFi.hostname("AIR-ESP8266");
  WiFi.softAPConfig(ApHost, ApHost, IPAddress(255, 255, 255, 0));
  if(WiFi.softAP(AP_NAME)){
    Serial.println("-------ESP8266 softAP 运行中-------");
    Serial.print("\nAP IP address: ");
    Serial.println(WiFi.softAPIP());
    dnsServer.setErrorReplyCode(DNSReplyCode::NoError);
    if(dnsServer.start(DNS_PORT, "*", ApHost)){
      Serial.println("-------dns server 工作中-------");
    }else{
      Serial.println("-------dns server 启动失败-------");
    }
  }
}
//--------web服务器初始化--------//
void initWebServer(){ //配置web服务器
  server.on("/", HTTP_GET, handleIndex);
  server.on("/wifiInfo", HTTP_GET, handleSendWifiInfo);
  server.on("/wifiList", HTTP_GET, handleSendWifiList);
  server.on("/wifiList", HTTP_POST, handleSetWifi);
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

void handleSetWifi() {
  DynamicJsonDocument res(500);
  String JsonString = server.arg("Body");
  deserializeJson(res, JsonString);
  JsonObject root = res.as<JsonObject>();
  const char* value = root["SSID"];
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
  // put your setup code here, to run once:
  Serial.begin(9600);
  if(SPIFFS.begin()){ // 启动SPIFFS
    Serial.println("-------SPIFFS 已启动-------");
  } else {
    Serial.println("-------SPIFFS 启动失败-------");
  }
  initWiFiAp();
  initWebServer();
}

void loop() {
  // put your main code here, to run repeatedly:
  if (WiFiMulti.run() != WL_CONNECTED){
	dnsServer.processNextRequest();
  }else{
	if (!client.connected()) {
	}
  }
  server.handleClient();
}
  
