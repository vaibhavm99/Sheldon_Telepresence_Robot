// const { getDisplayDecimalPlaces } = require("@tensorflow/tfjs-node/dist/callbacks");

const socket = io('/')
const videoGrid = document.getElementById('video-grid');
var ROOM_ID = "";
const myVideo = document.createElement('video');
const myPeer = new Peer()
const peers = {}
var model = null;
var flag = 0;


setInterval(() => { runDetections(); }, 5000);

var button1 = document.getElementById('stop');
var button2 = document.getElementById('forward');
var button3 = document.getElementById('backward');
var button4 = document.getElementById('left');
var button5 = document.getElementById('right');
var button6 = document.getElementById('shutdown');

function runDetections() {
  console.log("gesture event started");
  console.log("Flag : " + flag);
    var vid = document.getElementById('firstuser');
    if (flag == 0 && vid != null) {
      flag = 1;
      console.log("hand captured");
      model.estimateHands(document.getElementById("firstuser")).then((predictions) => {
        console.log("Prediction completed with count: " + predictions.length);
        flag = 0;
        if (predictions.length > 0) { 
            $('#alertMessage').fadeIn("fast", function(){        
              $("#alertMessage").fadeOut(2000);
            });          
          console.log(predictions[0].landmarks);
          var data = JSON.stringify(predictions[0].landmarks);
          console.log(data)
          $.ajax({
            type: "POST",
            url: "/getpredictions",
            data: data,
            contentType: "application/json; charset=utf-8",
            dataType: "json",
          });
        }
      })
    }
  console.log("gesture event ended");
}

button1.addEventListener('click', function (e) {
  console.log("button clicked clockwise");
  while (flag == 1)
  {
    return new Promise(resolve => setTimeout(resolve, 500));
  }
  flag = 1;
  data1 = {
    'stop': "1",
    'forward':"0",
    'backward':"0",
    'left':"0",
    'right':"0",
    'shutdown':"0"
  };
  $.ajax({
    type: "POST",
    url: "/buttonUpdate",
    dataType: "json",
    success: async function (msg) {
      console.log("ended");
      flag = 0;
    },
    data: data1
  });
});


button2.addEventListener('click', function (e) {
  console.log("button clicked forward");
  while (flag == 1)
  {
    return new Promise(resolve => setTimeout(resolve, 500));
  }
  flag = 1;
  data1 = {
    'stop':"0",
    'forward':"1",
    'backward':"0",
    'left':"0",
    'right':"0",
    'shutdown':"0"
  };
  $.ajax({
    type: "POST",
    url: "/buttonUpdate",
    dataType: "json",
    success: async function (msg) {
      console.log("ended");
      flag = 0;
    },
    data: data1
  });
});


button3.addEventListener('click', function (e) {
  console.log("button clicked backward");
  while (flag == 1)
  {
    return new Promise(resolve => setTimeout(resolve, 500));
  }
  flag = 1;
  data1 = {
    'stop':"0",
    'forward':"0",
    'backward':"1",
    'left':"0",
    'right':"0",
    'shutdown':"0"
  };
  $.ajax({
    type: "POST",
    url: "/buttonUpdate",
    dataType: "json",
    success: async function (msg) {
      console.log("ended");
      flag = 0;
    },
    data: data1
  });
});


button4.addEventListener('click', function (e) {
  console.log("button clicked up");
  while (flag == 1)
  {
    return new Promise(resolve => setTimeout(resolve, 500));
  }
  flag = 1;
  data1 = {
    'stop':"0",
    'forward':"0",
    'backward':"0",
    'left':"1",
    'right':"0",
    'shutdown':"0"
  };
  $.ajax({
    type: "POST",
    url: "/buttonUpdate",
    dataType: "json",
    success: async function (msg) {
      console.log("ended");
      flag = 0;
    },
    data: data1
  });
});


button5.addEventListener('click', function (e) {
  console.log("button clicked down");
  while (flag == 1)
  {
    return new Promise(resolve => setTimeout(resolve, 500));
  }
  flag = 1;
  data1 = {
    'stop':"0",
    'forward':"0",
    'backward':"0",
    'left':"0",
    'right':"1",
    'shutdown':"0"
  };
  $.ajax({
    type: "POST",
    url: "/buttonUpdate",
    dataType: "json",
    success: async function (msg) {
      console.log("ended");
      flag = 0;
    },
    data: data1
  });
});


button6.addEventListener('click', function (e) {
  console.log("button clicked anticlockwise");
  while (flag == 1)
  {
    return new Promise(resolve => setTimeout(resolve, 500));
  }
  flag = 1;
  data1 = {
    'stop':"0",
    'forward':"0",
    'backward':"0",
    'left':"0",
    'right':"0",
    'shutdown':"1"
  };
  $.ajax({
    type: "POST",
    url: "/buttonUpdate",
    dataType: "json",
    success: async function (msg) {
      console.log("ended");
      flag = 0;
    },
    data: data1
  });
});

$(document).ready(async function () {
  tf.setBackend('wasm').then(() => { 
  console.log('Using TensorFlow backend: ', tf.getBackend());
    handpose.load().then((lmodel)=>{
      model = lmodel
      $.ajax({
        type: "GET",
        url: "/getroomid",
        dataType: "json",
        success: async function (msg) {
          console.log(msg);
          if (msg.length > 0) {
            ROOM_ID = msg[0].message;
            const myVideo = document.createElement('video')
            myVideo.muted = true
            myVideo.id = 'firstuser';
  
            //socket not being called here so jb naya user aaya tuh vo apne broadcast karta ni tuh isliye dikkat ho rhi but with this code it is perfect
            if(myPeer._open){
              socket.emit('join-room', ROOM_ID, 'manmeet')
            }
            // myPeer.on('open', id => {
            // })
    
            navigator.mediaDevices.getUserMedia({
              video: true,
              audio: true
            }).then(stream => {
              addVideoStream(myVideo, stream)
    
              myPeer.on('call', call => {
                call.answer(stream)
                const video = document.createElement('video')
                call.on('stream', userVideoStream => {
                  addVideoStream(video, userVideoStream)
                })
              })
    
              socket.on('user-connected', userId => {
                connectToNewUser(userId, stream)
              })
            })
          }
          else {
            alert("Something went wrong please try again !");
          }
        }
      })
    });
  });
})


socket.on('user-disconnected', userId => {
  if (peers[userId]) peers[userId].close()
})

function connectToNewUser(userId, stream) {
  const call = myPeer.call(userId, stream)
  const video = document.createElement('video')
  call.on('stream', userVideoStream => {
    addVideoStream(video, userVideoStream)
  })
  call.on('close', () => {
    video.remove()
  })

  peers[userId] = call
}

function addVideoStream(video, stream) {
  video.srcObject = stream
  video.addEventListener('loadedmetadata', () => {
    video.play()
  })
  videoGrid.append(video)
}



