from pymongo import MongoClient
client = MongoClient("mongodb+srv://ThaparUser:Pass123@cluster0.7yqcd.mongodb.net/SheldonRobot?retryWrites=true&w=majority")
db = client.get_database('SheldonRobot')
prevlandmarks = []
prevnav = []

while(True):
    records = db.robotgesture
    ls = list(records.find({'robotid':'1811'}))
    if len(ls) > 0 and ls[0] != prevlandmarks:
        
        thumbIsOpen = False
        firstFingerIsOpen = False
        secondFingerIsOpen = False
        thirdFingerIsOpen = False
        fourthFingerIsOpen = False

        prevlandmarks = ls[0]
        pseudoFixKeyPoint = ls[0]['landmarks'][2][0]
        if ls[0]['landmarks'][3][0] < pseudoFixKeyPoint and ls[0]['landmarks'][4][0] < pseudoFixKeyPoint:
            thumbIsOpen = True

        pseudoFixKeyPoint = ls[0]['landmarks'][6][1]
        if ls[0]['landmarks'][7][1] < pseudoFixKeyPoint and ls[0]['landmarks'][8][1] < pseudoFixKeyPoint:
            firstFingerIsOpen = True

        pseudoFixKeyPoint = ls[0]['landmarks'][10][1]
        if ls[0]['landmarks'][11][1] < pseudoFixKeyPoint and ls[0]['landmarks'][12][1] < pseudoFixKeyPoint:
            secondFingerIsOpen = True

        pseudoFixKeyPoint = ls[0]['landmarks'][14][1]
        if ls[0]['landmarks'][15][1] < pseudoFixKeyPoint and ls[0]['landmarks'][16][1] < pseudoFixKeyPoint:
            thirdFingerIsOpen = True

        pseudoFixKeyPoint = ls[0]['landmarks'][18][1]
        if ls[0]['landmarks'][19][1] < pseudoFixKeyPoint and ls[0]['landmarks'][20][1] < pseudoFixKeyPoint:
            fourthFingerIsOpen = True

        print('Thumb :',thumbIsOpen)
        print('First Finger :', firstFingerIsOpen)
        print('Second Finger :',secondFingerIsOpen)
        print('Third Finger :',thirdFingerIsOpen)
        print('Fourth Finger :',fourthFingerIsOpen)

    records1 = db.robotnavigation
    ls = list(records1.find({'robotid':'1811'}))

    if (len(ls[0]) > 0) and (((len(prevnav[0]) > 0) and (ls[0] != prevnav[0])) or (len(prevnav)==0)):
        prenav = ls[0]
        print('clockwise :',ls[0]['clockwise'])
        print('anticlockwise :',ls[0]['anticlockwise'])
        print('Arm up :',ls[0]['up'])
        print('Arm down:',ls[0]['down'])
        print('Robot forward :',ls[0]['forward'])
        print('Robot Backward :',ls[0]['backward'])
        