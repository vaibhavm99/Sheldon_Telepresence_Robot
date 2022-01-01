#include <Servo.h> 
int indexPin = 3; 
int middlePin = 5;
int ringPin = 6;
int pinkyPin = 9;
int thumbPin = 10;

int ic = 0;
int io = 180;
int mo = 90;
int mc = 0;
int ro = 90;
int rc = 150;
int po = 90;
int pc = 180;
int to = 150;
int tc = 50;

Servo thumb, index, middle, ring, pinky; 

int ci, cm, cr, cp, ct;

void setup() { 
  Serial.begin(9600);
pinMode(2, INPUT);
pinMode(4, INPUT);
pinMode(7, INPUT);
pinMode(8, INPUT);
   thumb.attach(thumbPin); 
   index.attach(indexPin);
   middle.attach(middlePin);
   ring.attach(ringPin);
   pinky.attach(pinkyPin);
   Serial.println("All Open");
   ci = io;
   cm = mo;
   cr = ro;
   cp = po;
   ct = to;
   

}


void loop(){ 

  bool b0 = digitalRead(2);
  bool b1 = digitalRead(4);
  bool b2 = digitalRead(7);
  bool b3 = digitalRead(8);
  int val = b0 + b1*2 + b2*4 + b3*8;

  if(val == 1) // Index Open
    ci = io;
    
  else if(val == 2) // Index Close
    ci = ic;  

  else if(val == 3) // Middle Open
    cm = mo;

  else if(val == 4) // Middle Close
    cm = mc;

  else if(val == 5) // Ring Open
    cr = ro;

  else if(val == 6) // Ring Close
    cr = rc;

  else if(val == 7) // Pinky Open
    cp = po;

  else if(val == 8) // Pinky Close
    cp = pc;

  else if(val == 9) // Thumb Open
    ct = to;

  else if(val == 10) // Thumb Close
    ct = tc;

  else if(val == 11) // All Open
  {
    ci = io;
    cm = mo;
    cr = ro;
    cp = po;
    ct = to;
  }

  else if(val == 12) // All Close
  {
    ci = ic;
    cm = mc;
    cr = rc;
    cp = pc;
    ct = tc; 
  }
// Execute all Positions

  index.write(ci);
  middle.write(cm);
  ring.write(cr);
  pinky.write(cp);
  thumb.write(ct);
}
  
