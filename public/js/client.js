const socket = io('/')

const videoGrid = document.getElementById('video-grid');
var ROOM_ID = "";
const myVideo = document.createElement('video');
const myPeer = new Peer()
const peers = {}


$(document).ready(async function () {
    var ROOM_ID = location.search.split('roomId=')[1]
    const myVideo = document.createElement('video')
    myVideo.muted = true
    myVideo.id = 'firstuser';
    myPeer.on('open', id => {
        socket.emit('join-room', ROOM_ID, id)
    })

    navigator.mediaDevices.getUserMedia({
        video: true,
        audio: true
    }).then(stream => {
        
        addVideoStream(myVideo, stream)

        myPeer.on('call', call => {
            call.answer(stream)
            const video = document.createElement('video')
            video.id = "seconduser";
            call.on('stream', userVideoStream => {
                addVideoStream(video, userVideoStream)
            })
        })

        socket.on('user-connected', userId => {
            connectToNewUser(userId, stream)
        })
    })
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



