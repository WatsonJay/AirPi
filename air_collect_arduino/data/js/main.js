var wifiInfoInterval;
var mtqqInfoInterval;

$(document).ready(function (){
    refreshWifiInfo()
    $('#wifiCollapse').on('show.bs.collapse', function () {
        refreshWifiList()
    })
});

function changeWifiCollapse(){
    $("#wifiCollapse").collapse("toggle");
}

function refreshWifiInfo(){
    $.getJSON("/wifiInfo",function (data) {

    })
    // wifiInfoInterval = setInterval(function () {
    //     console.log("执行")
    // },4000)
}

function refreshWifiList(){
    $.getJSON("/wifiList",function (data) {
        debugger
        var list = data.result.sort(function(a, b){
            return parseInt(a["RSSI"]) < parseInt(b["RSSI"]) ? 1 : parseInt(a["RSSI"]) == parseInt(b["RSSI"]) ? 0 : -1;
        });
        $.each(list,function(index,obj){
            $("#wifiInfo").append("<option value='"+obj["SSID"]+"'>"+obj["SSID"]+"</option>");
        })
    })
}

window.onbeforeunload = function () {
    window.clearInterval(wifiInfoInterval)
}

function clearDom() {
    $("#mtqqServer").empty();
}

function setMtqqServer() {
    $("#mtqqServer").append("<span>192.152.1.2</span>");
    alert("Text: " + $("#mtqqServer").text());
}
