import cv2 
import face_train
vid = cv2.VideoCapture(0) 

def start(name):
	face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

	a=0
	while(True): 
		s,img = vid.read() 
		gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
		faces = face_cascade.detectMultiScale(gray, 1.3, 5)
		for (x,y,w,h) in faces:
		    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
		    roi_gray = gray[y:y+h, x:x+w]
		    roi_color = img[y:y+h, x:x+w]
		    cv2.imwrite("images/"+name+"/"+str(a)+".png",roi_gray)
		    a=a+1
		cv2.imshow('frame', img) 
		if cv2.waitKey(100)==97 or a>30:
			break
	face_train.train()
	vid.release() 
	cv2.destroyAllWindows() 
