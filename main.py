import RPi.GPIO as GPIO
from pymongo import MongoClient
client = MongoClient("mongodb+srv://ThaparUser:Pass123@cluster0.7yqcd.mongodb.net/SheldonRobot?retryWrites=true&w=majority")
db = client.get_database('SheldonRobot')

#b3 b2 b1 b0
# Bigger letter Open, Smaller letter Close
b0 = 11
b1 = 13
b2 = 15
b3 = 19
i1 = 29
i2 = 31
i3 = 33
i4 = 35

i1_state = GPIO.LOW
i2_state = GPIO.LOW
i3_state = GPIO.LOW
i4_state = GPIO.LOW


b0_state = GPIO.HIGH
b1_state = GPIO.HIGH
b2_state = GPIO.LOW
b3_state = GPIO.HIGH

GPIO.setmode(GPIO.BOARD)

GPIO.setup(b0, GPIO.OUT)
GPIO.setup(b1, GPIO.OUT)
GPIO.setup(b2, GPIO.OUT)
GPIO.setup(b3, GPIO.OUT)
GPIO.setup(i1, GPIO.OUT)
GPIO.setup(i2, GPIO.OUT)
GPIO.setup(i3, GPIO.OUT)
GPIO.setup(i4, GPIO.OUT)


GPIO.output(b0, b0_state)
GPIO.output(b1, b1_state)
GPIO.output(b2, b2_state)
GPIO.output(b3, b3_state)
GPIO.output(i1, i1_state)
GPIO.output(i2, i2_state)
GPIO.output(i3, i3_state)
GPIO.output(i4, i4_state)

def stop1():
    i1_state = GPIO.LOW
    i2_state = GPIO.LOW
    i3_state = GPIO.LOW
    i4_state = GPIO.LOW
    GPIO.output(i1, i1_state)
    GPIO.output(i2, i2_state)
    GPIO.output(i3, i3_state)
    GPIO.output(i4, i4_state)

while True:
    records = db.robotgesture
    ls = list(records.find({'robotid':'1811'}))
    if len(ls) > 0 :
        if  ls[0]['first'] == "1": #Index
            val = 1
            stop1()
            b0_state = GPIO.HIGH
            b1_state = GPIO.LOW
            b2_state = GPIO.LOW
            b3_state = GPIO.LOW
            GPIO.output(b0, b0_state)
            GPIO.output(b1, b1_state)
            GPIO.output(b2, b2_state)
            GPIO.output(b3, b3_state)  
        elif ls[0]['first'] == "0": #Index Close
            val = 2
            stop1()
            b0_state = GPIO.LOW
            b1_state = GPIO.HIGH
            b2_state = GPIO.LOW
            b3_state = GPIO.LOW
            GPIO.output(b0, b0_state)
            GPIO.output(b1, b1_state)
            GPIO.output(b2, b2_state)
            GPIO.output(b3, b3_state)     
            
        if ls[0]['middle'] == "1": #middle
            val = 3
            stop1()
            b0_state = GPIO.HIGH
            b1_state = GPIO.HIGH
            b2_state = GPIO.LOW
            b3_state = GPIO.LOW
            GPIO.output(b0, b0_state)
            GPIO.output(b1, b1_state)
            GPIO.output(b2, b2_state)
            GPIO.output(b3, b3_state)        
        elif ls[0]['middle'] == "0":
            val = 4
            stop1()  
            b0_state = GPIO.LOW
            b1_state = GPIO.LOW
            b2_state = GPIO.HIGH
            b3_state = GPIO.LOW
            GPIO.output(b0, b0_state)
            GPIO.output(b1, b1_state)
            GPIO.output(b2, b2_state)
            GPIO.output(b3, b3_state)      
            
        if ls[0]['ring'] == "1": #Ring
            val = 5
            stop1()    
            b0_state = GPIO.HIGH
            b1_state = GPIO.LOW
            b2_state = GPIO.HIGH
            b3_state = GPIO.LOW
            GPIO.output(b0, b0_state)
            GPIO.output(b1, b1_state)
            GPIO.output(b2, b2_state)
            GPIO.output(b3, b3_state)     
        elif ls[0]['ring'] == "0":
            val = 6
            stop1()
            b0_state = GPIO.LOW
            b1_state = GPIO.HIGH
            b2_state = GPIO.HIGH
            b3_state = GPIO.LOW
            GPIO.output(b0, b0_state)
            GPIO.output(b1, b1_state)
            GPIO.output(b2, b2_state)
            GPIO.output(b3, b3_state)
            
        if ls[0]['pinky'] == "1": #Pinky
            val = 7
            stop1()
            b0_state = GPIO.HIGH
            b1_state = GPIO.HIGH
            b2_state = GPIO.HIGH
            b3_state = GPIO.LOW
            GPIO.output(b0, b0_state)
            GPIO.output(b1, b1_state)
            GPIO.output(b2, b2_state)
            GPIO.output(b3, b3_state)          
        elif ls[0]['pinky'] == "0":
            val = 8
            stop1()
            b0_state = GPIO.LOW
            b1_state = GPIO.LOW
            b2_state = GPIO.LOW
            b3_state = GPIO.HIGH
            GPIO.output(b0, b0_state)
            GPIO.output(b1, b1_state)
            GPIO.output(b2, b2_state)
            GPIO.output(b3, b3_state)        
            
        if ls[0]['thumb'] == "1": #Thumb
            val = 9
            stop1()
            b0_state = GPIO.HIGH
            b1_state = GPIO.LOW
            b2_state = GPIO.LOW
            b3_state = GPIO.HIGH
            GPIO.output(b0, b0_state)
            GPIO.output(b1, b1_state)
            GPIO.output(b2, b2_state)
            GPIO.output(b3, b3_state)
        elif ls[0]['thumb'] == "0":
            val = 10
            stop1()
            b0_state = GPIO.LOW
            b1_state = GPIO.HIGH
            b2_state = GPIO.LOW
            b3_state = GPIO.HIGH
            GPIO.output(b0, b0_state)
            GPIO.output(b1, b1_state)
            GPIO.output(b2, b2_state)
            GPIO.output(b3, b3_state)       
    
    records1 = db.robotnavigation
    ls = list(records1.find({'robotid':'1811'}))
    
    if len(ls) > 0 :
        if ls[0]['forward'] == "1": #forward      
            i1_state = GPIO.LOW
            i2_state = GPIO.HIGH
            i3_state = GPIO.LOW
            i4_state = GPIO.HIGH
            GPIO.output(i1, i1_state)
            GPIO.output(i2, i2_state)
            GPIO.output(i3, i3_state)
            GPIO.output(i4, i4_state)
        elif ls[0]['backward'] == "1": #backward
            i1_state = GPIO.HIGH
            i2_state = GPIO.LOW
            i3_state = GPIO.HIGH
            i4_state = GPIO.LOW
            GPIO.output(i1, i1_state)
            GPIO.output(i2, i2_state)
            GPIO.output(i3, i3_state)
            GPIO.output(i4, i4_state)
        elif ls[0]['right'] == "1": #right
            i1_state = GPIO.LOW
            i2_state = GPIO.HIGH
            i3_state = GPIO.HIGH
            i4_state = GPIO.LOW
            GPIO.output(i1, i1_state)
            GPIO.output(i2, i2_state)
            GPIO.output(i3, i3_state)
            GPIO.output(i4, i4_state)
        elif ls[0]['left'] == "1": #left
            i1_state = GPIO.HIGH
            i2_state = GPIO.LOW
            i3_state = GPIO.LOW
            i4_state = GPIO.HIGH
            GPIO.output(i1, i1_state)
            GPIO.output(i2, i2_state)
            GPIO.output(i3, i3_state)
            GPIO.output(i4, i4_state)
        elif ls[0]['shutdown'] == "1": #program close (robot working off)
            records.delete_one({"robotid":"1811"})
            records1.delete_one({"robotid":"1811"}) 
            break
        elif ls[0]['stop'] == "1": #stop
            stop1()
    else:
        b0_state = GPIO.LOW
        b1_state = GPIO.LOW
        b2_state = GPIO.LOW
        b3_state = GPIO.LOW
        i1_state = GPIO.LOW
        i2_state = GPIO.LOW
        i3_state = GPIO.LOW
        i4_state = GPIO.LOW
        GPIO.output(b0, b0_state)
        GPIO.output(b1, b1_state)
        GPIO.output(b2, b2_state)
        GPIO.output(b3, b3_state)
        GPIO.output(i1, i1_state)
        GPIO.output(i2, i2_state)
        GPIO.output(i3, i3_state)
        GPIO.output(i4, i4_state)
GPIO.cleanup()