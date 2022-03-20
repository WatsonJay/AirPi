var wifiInfoInterval;
var mtqqInfoInterval;

$(document).ready(function (){
    refreshWifiInfo()
    wifiInfoInterval = setInterval(function () {
        refreshWifiInfo()
    },20000)
    mtqqInfoInterval = setInterval(function () {
        refreshMqttInfo()
    },20000)
    $("[name='wifiSetting']").submit(function (e) {
        return submitWifiSetting()
    })
    $("[name='mqttSetting']").submit(function (e) {
        return submitMqttSetting()
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

function refreshMqttInfo(){
    $.getJSON("/mqttInfo",function (data) {
        $("#mtqqServer").empty();
        $("#mtqqSended").empty();
        $("#mtqqServer").append("<span>" + data.result["mqttIp"]+ "</span>");
        $("#mtqqSended").append("<span>" + data.result["isSended"]==1?"成功":"失败"+ "</span>");
    })
}

function refreshWifiList(){
    $.getJSON("/wifiList",function (data) {
        debugger
        var list = data.result.sort(function(a, b){
            return parseInt(a["RSSI"]) < parseInt(b["RSSI"]) ? 1 : parseInt(a["RSSI"]) == parseInt(b["RSSI"]) ? 0 : -1;
        });
        $.each(list,function(index,obj){
            $("#wifiName").append("<option value='"+obj["SSID"]+"'>"+obj["SSID"]+"</option>");
        })
    })
}

function submitWifiSetting(){
    debugger
    var $form = $("[name='wifiSetting']");
    var data = getFormData($form);
    $.ajax({
        type: "post",
        url: "wifiSetting",
        dataType: "json",
        contentType: "application/json;charset=utf-8",
        data: JSON.stringify(data),
        success: function (d){
            showSuccessAlart("wifi设置成功")
            $('#wifiCollapse').collapse('hide')
        },
        error: function (d){
            showErrorAlart("wifi设置失败，请重试")
        }
    })
    return false;
}

function submitMqttSetting() {
    debugger
    var $form = $("[name='mqttSetting']");
    var data = getFormData($form);
    $.ajax({
        type: "post",
        url: "mqttSetting",
        dataType: "json",
        contentType: "application/json;charset=utf-8",
        data: JSON.stringify(data),
        success: function (d){
            showSuccessAlart("mqtt服务器设置成功")
            $('#mqttCollapse').collapse('hide')
        },
        error: function (d){
            showErrorAlart("mqtt服务器设置失败，请重试")
        }
    })
    return false;
}

window.onbeforeunload = function () {
    window.clearInterval(wifiInfoInterval)
    window.clearInterval(mtqqInfoInterval)
}

function showSuccessAlart(msg) {
    $("#wifiAlert").append("<div class='alert alert-success fade show' id='wifiSuccess' role='alert'>" + msg + "</div>"
      )
    window.setTimeout(function () {
        $('#wifiSuccess').alert('close');
    }, 3000)
}

function showErrorAlart(msg) {
    $("#wifiAlert").append("<div class='alert alert-danger fade show' id='wifiError' role='alert'>" + msg + "</div>")
    window.setTimeout(function () {
        $('#wifiError').alert('close');
    }, 3000)
}

function getFormData($form) {
    debugger
    var form_array = $form.serializeArray();
    var indexed_array = {};
    $.map(form_array, function(n, i){
        indexed_array[n['name']] = n['value'];
    });
    return indexed_array;
}

function clearDom() {
    $("#mtqqServer").empty();
}

function setMtqqServer() {
    $("#mtqqServer").append("<span>192.152.1.2</span>");
    alert("Text: " + $("#mtqqServer").text());
}
