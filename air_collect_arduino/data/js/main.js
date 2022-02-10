var wifiInfoInterval;
var mtqqInfoInterval;

$(document).ready(function (){
    $('#wifiCollapse').on('show.bs.collapse', function () {
        refreshWifiList()
    })
});

function changeWifiCollapse(){
    $("#wifiCollapse").collapse("toggle");
}

function refreshWifiInfo(){
    wifiInfoInterval = setInterval(function () {
        console.log("执行")
    },2000)
}

function refreshWifiList(){
    $.getJSON("/wifiInfo",function (data) {
        
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
