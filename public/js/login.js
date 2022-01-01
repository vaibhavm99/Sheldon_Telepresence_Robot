var btn = document.getElementById("signin");

btn.addEventListener('click', function(e) {
    
    var person = {
        userid: document.getElementById('userid').value,
        userpass:document.getElementById('userpass').value,
        password: document.getElementById('password').value,
        robotid: document.getElementById('roboid').value
    };
    
    $.ajax({
        type: "POST",
        url: "/login",
        dataType: "json",
        success: async function (msg) {
            if(msg[0].status==true){
                if(msg[0].access == "view"){
                    location.href="/homeclient";
                }
                else{
                    location.href="/homehost";
                }
            }
            else if(msg[0].status == false){
                alert(msg[0].message);
            }
        }, 
        data:person
    });
});

var btn1 = document.getElementById('signup');
btn1.addEventListener('click',function(){
    location.href="/signupuser";
})