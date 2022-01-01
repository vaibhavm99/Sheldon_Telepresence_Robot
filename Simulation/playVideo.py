import cv2
import numpy as np
import os
import tkinter as tk
    
files = ['indexFingerOpening.mov', 'indexFingerClosing.mov', 'middleFingerOpening.mov', 'middleFingerClosing.mov',   'ringFingerOpening.mov',  'ringFingerClosing.mov', 'pinkyFingerOpening.mov', 'pinkyFingerClosing.mov']

def playVideo(finger):
	cap = cv2.VideoCapture(files[finger])
	if(cap.isOpened()== False):
		print("Error opening video file")
	while(cap.isOpened()):
		ret, frame = cap.read()
		if ret == True:
			cv2.imshow('Simulation Video', frame)
			if cv2.waitKey(25) & 0xFF == ord('q'):
				break
		else:
			break
	cap.release()
	cv2.destroyAllWindows()

    

root = tk.Tk()
root.title("Sheldon Simulation")
root.geometry('500x300')    

frame = tk.Frame(root)
tk.Label(root, text="Sheldon - Control Panel", fg = "black", font = "Times 30 bold").pack()
frame.pack()

#QUIT
quitButton = tk.Button(root, text="QUIT", fg="red", command=quit)
quitButton.place(x=215, y=250)
# button.pack(side=tk.BOTTOM)



#Index Finger
indexOpen = tk.Button(root, fg='black', text="Open Index Finger", command=lambda:playVideo(0))
indexOpen.place(x=100, y=50)
indexClose = tk.Button(root, fg='black', text="Close Index Finger", command=lambda:playVideo(1))
indexClose.place(x=250, y=50)




#Middle Finger
middleOpen = tk.Button(root, fg='black', text="Open Middle Finger", command=lambda:playVideo(2))
middleOpen.place(x=90, y=100)
middleClose = tk.Button(root, fg='black', text="Close Middle Finger", command=lambda:playVideo(3))
middleClose.place(x=250, y=100)


#Ring Finger
ringOpen = tk.Button(root, fg='black', text="Open Ring Finger", command=lambda:playVideo(4))
ringOpen.place(x=100, y=150)
ringClose = tk.Button(root, fg='black', text="Close Ring Finger", command=lambda:playVideo(5))
ringClose.place(x=250, y=150)

#Pinky Finger
pinkyOpen = tk.Button(root, fg='black', text="Open Pinky Finger", command=lambda:playVideo(6))
pinkyOpen.place(x=100, y=200)
pinkyClose = tk.Button(root, fg='black', text="Close Pinky Finger", command=lambda:playVideo(7))
pinkyClose.place(x=250, y=200)


root.mainloop()

