const express = require('express')
const app = express()
const server = require('http').Server(app)
const io = require('socket.io')(server)
const MongoClient = require("mongodb").MongoClient
const { v4: uuidV4 } = require('uuid')
app.use(express.static("public"));
var bodyParser = require("body-parser")
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));
var PORT = process.env.PORT || 8080;

var roomID;

let db;
const url = "mongodb://ThaparUser:Pass123@cluster0-shard-00-00.7yqcd.mongodb.net:27017,cluster0-shard-00-01.7yqcd.mongodb.net:27017,cluster0-shard-00-02.7yqcd.mongodb.net:27017/SheldonRobot?ssl=true&replicaSet=atlas-7et9g6-shard-0&authSource=admin&retryWrites=true&w=majority";

MongoClient.connect(url, (err, database) => {
  if (err) {
    return console.log(err);
  }
  db = database;
  server.listen((PORT), () => {
    console.log('listening on deployed server');
  });
});

app.get('/speechrecognition', (req, res) => {
  res.sendFile(__dirname + "/speech.html")
})

var Robotid;

// updating and adding the preictions of gesture
app.post('/getpredictions', (req, res) => {
  console.log(req.body);
  var thumbIsOpen = "0"
  var firstFingerIsOpen = "0"
  var secondFingerIsOpen = "0"
  var thirdFingerIsOpen = "0"
  var fourthFingerIsOpen = "0"
  var pseudoFixKeyPoint = req.body[2][0]

  if (req.body[3][0] > pseudoFixKeyPoint && req.body[4][0] > pseudoFixKeyPoint) {
    thumbIsOpen = "1"
  }
  pseudoFixKeyPoint = req.body[6][1]
  if (req.body[7][1] < pseudoFixKeyPoint && req.body[8][1] < pseudoFixKeyPoint) {
    firstFingerIsOpen = "1"
  }

  pseudoFixKeyPoint = req.body[10][1]
  if (req.body[11][1] < pseudoFixKeyPoint && req.body[12][1] < pseudoFixKeyPoint) {
    secondFingerIsOpen = "1"
  }
  pseudoFixKeyPoint = req.body[14][1]
  if (req.body[15][1] < pseudoFixKeyPoint && req.body[16][1] < pseudoFixKeyPoint) {
    thirdFingerIsOpen = "1"
  }

  pseudoFixKeyPoint = req.body[18][1]
  if (req.body[19][1] < pseudoFixKeyPoint && req.body[20][1] < pseudoFixKeyPoint) {
    fourthFingerIsOpen = "1"
  }

  var data = {
    'robotid': Robotid,
    'thumb': thumbIsOpen,
    'first': firstFingerIsOpen,
    'middle': secondFingerIsOpen,
    'ring': thirdFingerIsOpen,
    'pinky': fourthFingerIsOpen,
  }
  db.collection("robotgesture").find({ robotid: Robotid }).toArray((err, result) => {
    if (err) {
      res.send(err);
    }

    if (result.length > 0) {
      result[0].thumb = data['thumb'];
      result[0].first = data['first'];
      result[0].middle = data['middle'];
      result[0].ring = data['ring'];
      result[0].pinky = data['pinky'];

      db.collection("robotgesture").save(result[0], (err, result1) => {
        if (err) {
          return console.log(err);
        }
        res.send([
          {
            message: "Request successfully logged",
            status: true,
          },
        ]);
      });
    }
    else {
      db.collection("robotgesture").save(data, (err, result) => {
        if (err) {
          return console.log(err);
        }
        res.send([
          {
            message: "Request successfully logged",
            status: true,
          },
        ]);
      });
    }
  })
})

app.get('/', (req, res) => {
  res.sendFile(__dirname + "/login.html")
})

app.get('/homehost', (req, res) => {
  res.sendFile(__dirname + "/index.html")
})

app.get('/homeclient', (req, res) => {
  res.sendFile(__dirname + "/homeclient.html")
})

app.get('/getroomID', (req, res) => {
  res.send([{ message: roomID, status: true, },]);
})

app.get('/host', (req, res) => {
  res.redirect(`/host/${uuidV4()}`)
});

app.get('/client', (req, res) => {
  res.sendFile(__dirname + "/client.html")
})

app.get('/host/:room', (req, res) => {
  roomID = req.params.room;
  res.sendFile(__dirname + "/host.html")
})

app.get('/signupuser', (req, res) => {
  res.sendFile(__dirname + "/signup.html")
})

app.get('/accessSetting', (req, res) => {
  res.sendFile(__dirname + "/AccessSetting.html")
})

io.on('connection', socket => {
  socket.on('join-room', (roomId, userId) => {
    socket.join(roomId)
    socket.broadcast.to(roomId).emit('user-connected', userId)
    socket.on('disconnect', () => {
      socket.broadcast.to(roomId).emit('user-disconnected', userId)
    })
  });
  socket.on('user-streamming', (arg) => {
    console.log(arg);
  });
});

app.post('/login', (req, res) => {
  var password1 = req.body.password;
  var robotid1 = req.body.robotid;

  db.collection("RobotDetails").find({ robotid: robotid1, password: password1 }).toArray((err, result) => {
    if (err) {
      res.send(err);
    }
    if (result.length > 0) {
      db.collection("Users").find({ userid: req.body.userid, password: req.body.userpass }).toArray((err, result1) => {
        if (err) {
          res.send(err);
        }
        if (result1.length > 0) {
          db.collection("AccessDetails").find({ userid: req.body.userid, robotid: req.body.robotid }).toArray((err, result2) => {
            if (err) {
              res.send(err);
            }
            if (result2.length > 0) {
              result2[0]['status'] = true;
              Robotid = robotid1;
              res.send(result2);
            }
            else {
              res.send([{
                'message': "User has no access to the robot",
                'status': false
              }]);
            }
          });
        }
        else {
          res.send([{
            'message': "Password or User ID is incorrect",
            'status': false
          }]);
        }
      });
    }
    else {
      res.send([{
        'message': "Password or Robot ID is incorrect",
        'status': false
      }]);
    }
  });
});


app.post('/buttonUpdate', (req, res) => {
  console.log(req.body);
  db.collection("robotnavigation").find({ robotid: Robotid }).toArray((err, result) => {
    if (err) {
      res.send(err);
    }
    if (result.length > 0) {

      result[0].stop = req.body.stop;
      result[0].forward = req.body.forward;
      result[0].backward = req.body.backward;
      result[0].left = req.body.left;
      result[0].right = req.body.right;
      result[0].shutdown = req.body.shutdown;

      db.collection("robotnavigation").save(result[0], (err, result1) => {
        if (err) {
          return console.log(err);
        }
        res.send([
          {
            message: "Request successfully logged",
            status: true,
          },
        ]);
      });
    }
    else {
      req.body['robotid'] = Robotid;
      db.collection("robotnavigation").save(req.body, (err, result) => {
        if (err) {
          return console.log(err);
        }
        res.send([
          {
            message: "Request successfully logged",
            status: true,
          },
        ]);
      });
    }
  })
})

app.post("/adduser", (req, res) => {
  db.collection("Users").save(req.body, (err, result) => {
    if (err) {
      return console.log(err);
    }
    console.log("click added to db");
    res.send([
      {
        message: "Request successfully logged",
        status: true,
      },
    ]);
  });
});


app.post("/grantaccess", (req, res) => {
  req.body['robotid']=Robotid;
  db.collection("AccessDetails").save(req.body, (err, result) => {
    if (err) {
      return console.log(err);
    }
    console.log("click added to db");
    res.send([
      {
        message: "Request successfully logged",
        status: true,
      },
    ]);
  });
});
