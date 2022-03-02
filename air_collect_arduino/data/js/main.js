var wifiInfoInterval;
var mtqqInfoInterval;

$(document).ready(function (){
    refreshWifiInfo()
    wifiInfoInterval = setInterval(function () {
        refreshWifiInfo()
    },20000)
    $("[name='wifiSetting']").submit(function (e) {
        return submitWifiSetting()
    })
    $('#wifiCollapse').on('show.bs.collapse', function () {
        refreshWifiList()
    })
});

function changeWifiCollapse(){
    $("#wifiCollapse").collapse("toggle");
}

function refreshWifiInfo(){
    $.getJSON("/wifiInfo",function (data) {
        $("#wifiSSID").empty();
        $("#ipAddr").empty();
        $("#gatewayIP").empty();
        $("#wifiSSID").append("<span>" + data.result["SSID"]+ "</span>");
        $("#ipAddr").append("<span>" + data.result["localIP"]+ "</span>");
        $("#gatewayIP").append("<span>" + data.result["gatewayIP"]+ "</span>");
    })
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

function submitWifiSetting(){
    debugger
    $('#wifiCollapse').collapse('hide')
    return false;
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
