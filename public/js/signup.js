var btn = document.getElementById("signup");

btn.addEventListener('click', function(e) {
    var person = {
        userid: document.getElementById('userid').value,
        password: document.getElementById('password').value,
    };
    
    $.ajax({
        type: "POST",
        url: "/adduser",
        dataType: "json",
        success: async function (msg) {
            if(msg.length>0){
                location.href="/";
            }
        }, 
        data:person
    });
});
