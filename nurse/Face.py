import cv2
import numpy as np
import pickle
import sys
import googleexcel
def reco():
	face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
	conf_min=45
	conf_max=85
	recognizer = cv2.face.LBPHFaceRecognizer_create()
	recognizer.read("trainner.yml")
	labels={}
	with open("labels.pickle",'rb') as f:
		og_labels=pickle.load(f)
		labels={v:k for k,v in og_labels.items()}
	cap = cv2.VideoCapture(0)	

	while True:
		ret, frame = cap.read()
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		faces = face_cascade.detectMultiScale(gray, 1.1, 4)
		for (x, y, w, h) in faces:
			cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2) #(frame,x,y,(end_cord_x,end_cord_y),color,stroke)

			#print(x,y,w,h)
			roi_gray=gray[y:y+h, x:x+w]
			roi_color = frame[y:y+h, x:x+w] #(cord1-height , cord2-width)
			id_,conf=recognizer.predict(roi_gray )
			if conf>=conf_min and conf<=conf_max:
				print(id_)
				print(labels[id_])
				font=cv2.FONT_HERSHEY_SIMPLEX
				name=labels[id_]
				color=(255,255,255)
				stroke=2
				cv2.putText(frame,name,(x,y),font,1,color,stroke,cv2.LINE_AA)
				temp=conf-conf_min
				cp=100-int((temp/conf_min)*100)
				if cp>55:
					print(name)
					print(googleexcel.find(name))
					sys.exit()
				cv2.putText(frame,str(cp)+"%",(x,y-30),font,1,color,stroke,cv2.LINE_AA)

			img_item="kau4.png"
			cv2.imwrite(img_item,roi_color)
			#eyes=eye_cascade.detectMultiscale(roi_gray)
			#for (ex,ey,ew,eh) in eyes:
			#	cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (255, 0, 0), 1)

			
			
			#print(ret)
		cv2.imshow('nursebot',frame)
		if cv2.waitKey(1) ==ord('q'): 
			break
	cap.release()
reco()
