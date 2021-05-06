import cv2
import os
import pickle
from PIL import Image
import numpy as np
def train():

	BASE_DIR=os.path.dirname(os.path.abspath(__file__))
	image_dir=os.path.join(BASE_DIR,"images")
	face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
	#print(dir(cv2.face))
	recognizer = cv2.face.LBPHFaceRecognizer_create()
	x_train=[]
	y_labels=[]
	current_id=0
	label_ids={}
	for root,dirs,files in os.walk(image_dir):
		for file in files:
			if file.endswith("png") or file.endswith("jpg"):
				print(file)
				path=os.path.join(root,file)
				label=os.path.basename(os.path.dirname(path)).replace(" ","-").lower()  #get name of folder that image is in
				#print(label,path)
				if not label in label_ids:
					label_ids[label]=current_id
					current_id +=1
				id_=label_ids[label]
				#print(label_ids)
				pil_image=Image.open(path).convert("L") #gets image from path
				size=(550,550)
				final_image=pil_image.resize(size,Image.ANTIALIAS)
				image_array=np.array(final_image,"uint8")
				x_train.append(image_array)
				y_labels.append(id_)
	#print(y_labels)
	#print(x_train)
	with open("labels.pickle",'wb') as f:
		pickle.dump(label_ids,f)

	recognizer.train(x_train,np.array(y_labels))
	recognizer.save("trainner.yml")
					

			
