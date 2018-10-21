from tkinter import*
import time
import os ,random,sys

	#from Frame1 import MainF
def buttonClick():
	f1.pack_forget()
	f2.pack()

root=Tk()
root.title("Image Identification Captcha V.1 ")
root.wm_iconbitmap('icc.ico') #Test case icon
root.geometry("1920x766+0+0")

#frame1
f1=Frame(root,height='766',width='1920',bg='blue',cursor='arrow')
f1.propagate(0)
f1.pack()

#Canvas 1 for writing text associaated with frame1
canvas1=Canvas(f1,bg='grey',height=100,width='900',cursor='arrow')
canvas1.pack()
c1=canvas1.create_text(500,50,text="Image Identification Captcha",font=('Times',40,'italic underline'))

#+++++++++++++++++++++++++++++++++++++++time++++++++++++++++++++++++++++++++++++
timeon=time.asctime(time.localtime(time.time()))
label1=Label(f1,text=timeon,bg='#EEEEEE',fg='red',font=('Arial',18,'bold'),bd=3,relief=RAISED)
label1.pack(side=TOP)

b=Button(f1,text='Start Image Identification Captcha',width='30',relief=RAISED,bd=3,height='2',command=buttonClick)
b.place(x=670,y=450)

exit=Button(f1,text='Exit',width='10',height='2',relief=RAISED,bd=3,command=quit)
exit.place(x=730,y=505)
#+++++++++++++++++++++++++++++++++++++++++++++++++++Next Frame++++++++++++++++++++++++++++++++++++++++++++++++++++++
f2=Frame(root,height='766',width='1920',bg='#EEEEEE',cursor='arrow')
f2.propagate(0)
f2.pack()
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++Menu++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
menubar=Menu(root)
root.config(menu=menubar)
filemenu=Menu(root,tearoff=0)
filemenu.add_command(label='About Us')


menubar.add_cascade(label='File',menu=filemenu)
exitmenu=Menu(root,tearoff=0)
exitmenu.add_command(label='Exit',command=root.destroy)
menubar.add_cascade(label='Exit',menu=exitmenu)
#++++++++++++++++++++++++++++++++++++++++++++++++++++++
insideFrame=Frame(f2,height=604,width=604)
insideFrame.pack()
insideFrame.place(x=400,y=100)
'''cap=Canvas(insideFrame,height=600,width=600,cursor='arrow',bg='blue')
cap1=cap.create_rectangle(0,0,198,198,outline='red',fill='green')
cap2=cap.create_rectangle(200,0,398,198,outline='red',fill='green')
cap3=cap.create_rectangle(400,0,598,198,outline='red',fill='green')
cap4=cap.create_rectangle(0,200,198,398,outline='red',fill='green')
cap5=cap.create_rectangle(200,198,398,398,outline='red',fill='green')
cap6=cap.create_rectangle(400,198,598,398,outline='red',fill='green')
cap4=cap.create_rectangle(0,400,198,598,outline='red',fill='green')
cap5=cap.create_rectangle(200,400,398,598,outline='red',fill='green')
cap6=cap.create_rectangle(400,400,598,598,outline='red',fill='green')
cap.pack()'''
#image_set
#random_image=random.choice(image_set)
verifyFrame=Frame(f2,height=60,width=604,bg='#888888')
verifyFrame.pack()
verifyFrame.place(x=400,y=710)

DescLabel=Label(f2,height=4,width=60,text="Click on the picture of traffic light",bd=3,bg='red',font=('Arial',12,'bold'))
DescLabel.pack()
DescLabel.place(x=400,y=18)
count=0
def flat():
	global count
	count=count+1
	if count%2!=0:
		img1['relief']='flat'
		print(count)
	else:
		img1['relief']='raised'
		print(count)
#photo1=PhotoImage(file="image/dmg.gif")
def click():
	pic1=random.choice(os.listdir("image/"))
	photo1=PhotoImage(file="image/"+pic1)
	pic2=random.choice(os.listdir("image/"))
	photo2=PhotoImage(file="image/"+pic2)
	pic3=random.choice(os.listdir("image/"))
	photo3=PhotoImage(file="image/"+pic3)
	pic4=random.choice(os.listdir("image/"))
	photo4=PhotoImage(file="image/"+pic4)
	pic5=random.choice(os.listdir("image/"))
	photo5=PhotoImage(file="image/"+pic5)
	pic6=random.choice(os.listdir("image/"))
	photo6=PhotoImage(file="image/"+pic6)
	pic7=random.choice(os.listdir("image/"))
	photo7=PhotoImage(file="image/"+pic7)
	pic8=random.choice(os.listdir("image/"))
	photo8=PhotoImage(file="image/"+pic8)
	pic9=random.choice(os.listdir("image/"))
	photo9=PhotoImage(file="image/"+pic9)

	print(photo1)
	img1=Button(insideFrame,image=photo1,height=200,width=200,relief=RAISED,bd=4,command=flat)
	img1.image=photo1
	img1.pack()
	img1.place(x=0,y=0)

	img2=Button(insideFrame,image=photo2,height=200,width=200,relief=RAISED,bd=4,command=flat)
	img2.image=photo2
	img2.pack()
	img2.place(x=200,y=0)

	img3=Button(insideFrame,image=photo3,height=200,width=200,relief=RAISED,bd=4,command=flat)
	img3.image=photo3
	img3.pack()
	img3.place(x=400,y=0)

	img4=Button(insideFrame,image=photo4,height=200,width=200,relief=RAISED,bd=4,command=flat)
	img4.image=photo4
	img4.pack()
	img4.place(x=0,y=200)

	img5=Button(insideFrame,image=photo5,height=200,width=200,relief=RAISED,bd=4,command=flat)
	img5.image=photo5
	img5.pack()
	img5.place(x=200,y=200)

	img6=Button(insideFrame,image=photo6,height=200,width=200,relief=RAISED,bd=4,command=flat)
	img6.image=photo6
	img6.pack()
	img6.place(x=400,y=200)

	img7=Button(insideFrame,image=photo7,height=200,width=200,relief=RAISED,bd=4,command=flat)
	img7.image=photo7
	img7.pack()
	img7.place(x=0,y=400)

	img8=Button(insideFrame,image=photo8,height=200,width=200,relief=RAISED,bd=4,command=flat)
	img8.image=photo8
	img8.pack()
	img8.place(x=200,y=400)

	img9=Button(insideFrame,image=photo9,height=200,width=200,relief=RAISED,bd=4,command=flat)
	img9.image=photo9
	img9.pack()
	img9.place(x=400,y=400)

verify=Button(verifyFrame,text='Verify',relief=RAISED,bd=3,state=DISABLED)
verify.pack()
verify.place(x=550,y=12)

Reset=Button(verifyFrame,text='Reset',relief=RAISED,bd=3,command=click)
Reset.pack()
Reset.place(x=10,y=12)
click()

root.mainloop()