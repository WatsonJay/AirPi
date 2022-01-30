function clearDom() {
    $("#mtqqServer").empty();
}

function setMtqqServer() {
    $("#mtqqServer").append("<span>192.152.1.2</span>");
    alert("Text: " + $("#mtqqServer").text());
}
