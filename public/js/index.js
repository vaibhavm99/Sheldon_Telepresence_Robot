
const button = document.getElementById('btncroom');
button.addEventListener('click', function(e) {
    location.href="/host";
})

const button1 = document.getElementById('btnjroom');
button1.addEventListener('click', function(e) {
    var param = document.getElementById('roomid').value;
    location.href = "/client?roomId="+param;
})