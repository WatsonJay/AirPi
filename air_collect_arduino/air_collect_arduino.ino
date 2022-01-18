//--------库引用---------//
#include <EEPROM.h>
#include <ESP8266WiFi.h>
#include <ESP8266WebServer.h>
#include <DNSServer.h>
#include <PubSubClient.h>
#include <Arduino.h>
#include <SimpleTimer.h>
#include <Hash.h>

//--------变量定义---------//
//--------WIFI参数--------//
//--------setup()---------//
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  WiFi.mode(WIFI_AP_STA);
  Serial.println("-------WIFI启动为AP模式-------");
}

void loop() {
  // put your main code here, to run repeatedly:

}
