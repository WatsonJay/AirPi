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
    var $form = $("[name='wifiSetting']");
    var data = getFormData($form);
    showSuccessAlart()
    $('#wifiCollapse').collapse('hide')
    return false;
}

window.onbeforeunload = function () {
    window.clearInterval(wifiInfoInterval)
}

function showSuccessAlart() {
    $("#wifiAlert").append("<div class='alert alert-success fade show' id='wifiSuccess' role='alert'>wifi设置成功</div>"
      )
    window.setTimeout(function () {
        $('#wifiSuccess').alert('close');
    }, 5000)
}

function showErrorAlart() {
    $("#wifiAlert").append("<div class='alert alert-danger fade show' id='wifiError' role='alert'>wifi设置失败,请检查重试</div>")
    window.setTimeout(function () {
        $('#wifiError').alert('close');
    }, 5000)
}

function getFormData($form) {
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
