import googleexcel
import eel
import os
import sys
import click_img

eel.init('web')


@eel.expose
def e():
    print("Activate")
    os.system("python Face.py")
    print("finish activation")
@eel.expose
def reg(data,data1):
    print(data+" "+data1)
    a=googleexcel.read("cv!C1:C1")
    print(a[0][0])
    b=a[0][0]
    print(b)  
    b=int(b)+1
    print(b)
    name="cv!A"+str(b)+":A"+str(b)
    tablet="cv!B"+str(b)+":B"+str(b)
    #print(name + " ---- " + tablet)
    googleexcel.write(data,name)
    googleexcel.write(data1,tablet)
    os.mkdir("images/"+data)
    click_img.start(data)
    googleexcel.write(b,"cv!C1:C1")
   

eel.start('index.html', size=(1000, 600))
