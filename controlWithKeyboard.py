import RPi.GPIO as GPIO

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

    key = input()
    if key == 'I': #Index
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
        
    elif key == 'i': #Index Close
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
          
    elif key == 'M': #middle
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
        
    elif key == 'm':
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
        
    elif key == 'R': #Ring
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
        
    elif key == 'r':
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
        
    elif key == 'P': #Pinky
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
        
    elif key == 'p':
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
        
    elif key == 'T': #Thumb
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
        
    elif key == 't':
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
        
    elif key == 'a': #open all
        val = 11
        stop1()
        b0_state = GPIO.HIGH
        b1_state = GPIO.HIGH
        b2_state = GPIO.LOW
        b3_state = GPIO.HIGH
        GPIO.output(b0, b0_state)
        GPIO.output(b1, b1_state)
        GPIO.output(b2, b2_state)
        GPIO.output(b3, b3_state)

    elif key == 'g': #grasp close all
        val = 12
        stop1()
        b0_state = GPIO.LOW
        b1_state = GPIO.LOW
        b2_state = GPIO.HIGH
        b3_state = GPIO.HIGH
        GPIO.output(b0, b0_state)
        GPIO.output(b1, b1_state)
        GPIO.output(b2, b2_state)
        GPIO.output(b3, b3_state)
        
    elif key == 'w': #forward
        
        i1_state = GPIO.LOW
        i2_state = GPIO.HIGH
        i3_state = GPIO.LOW
        i4_state = GPIO.HIGH
        GPIO.output(i1, i1_state)
        GPIO.output(i2, i2_state)
        GPIO.output(i3, i3_state)
        GPIO.output(i4, i4_state)

    elif key == 's': #backward
        i1_state = GPIO.HIGH
        i2_state = GPIO.LOW
        i3_state = GPIO.HIGH
        i4_state = GPIO.LOW
        GPIO.output(i1, i1_state)
        GPIO.output(i2, i2_state)
        GPIO.output(i3, i3_state)
        GPIO.output(i4, i4_state)

    elif key == 'e': #right
        i1_state = GPIO.LOW
        i2_state = GPIO.HIGH
        i3_state = GPIO.HIGH
        i4_state = GPIO.LOW
        GPIO.output(i1, i1_state)
        GPIO.output(i2, i2_state)
        GPIO.output(i3, i3_state)
        GPIO.output(i4, i4_state)

    elif key == 'q': #left
        i1_state = GPIO.HIGH
        i2_state = GPIO.LOW
        i3_state = GPIO.LOW
        i4_state = GPIO.HIGH
        GPIO.output(i1, i1_state)
        GPIO.output(i2, i2_state)
        GPIO.output(i3, i3_state)
        GPIO.output(i4, i4_state)

    elif key == 'f': #program close (robot working off)
        break
    elif key == 'v': #stop
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