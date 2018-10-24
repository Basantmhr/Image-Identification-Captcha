from tkinter import*
import time
import os ,random,sys
import re

#below is the function to change from and forget previous frame to new frame
def buttonClick():
	f1.pack_forget()
	f2.pack()

root=Tk()
root.title("Image Identification Captcha V.1 ")
root.wm_iconbitmap('icc.ico') #Test case icon
root.geometry("1920x766+0+0")

#frame1
f1=Frame(root,height='766',width='1920',bg='#FF6F00',cursor='arrow')
f1.propagate(0)
f1.pack()

#Canvas 1 for writing text associaated with frame1
canvas1=Canvas(f1,bg='grey',height=100,width='900',cursor='arrow')
canvas1.pack()
c1=canvas1.create_text(500,50,text="Image Identification Captcha V.1",font=('Times',40,'italic underline'))

# i have used label below inside which time is being shown
timeon=time.asctime(time.localtime(time.time()))
label1=Label(f1,text=timeon,bg='#EEEEEE',fg='red',font=('Arial',18,'bold'),bd=3,relief=RAISED)
label1.pack(side=TOP)
#Start button is defined below
b=Button(f1,text='Start Image Identification Captcha',width='30',relief=RAISED,bd=3,height='2',command=buttonClick)
b.place(x=670,y=450)
#Exit Button is defined below
exit=Button(f1,text='Exit',width='10',height='2',relief=RAISED,bd=3,command=quit)
exit.place(x=730,y=505)
#+++++++++++++++++++++++++++++++++++++++++++++++++++Next Frame++++++++++++++++++++++++++++++++++++++++++++++++++++++
f2=Frame(root,height='766',width='1920',bg='#EEEEEE',cursor='arrow')
f2.propagate(0)
f2.pack()
#Menu bar is defined here
menubar=Menu(root)
root.config(menu=menubar)
filemenu=Menu(root,tearoff=0)
filemenu.add_command(label='About Us')

#separating File and Exit into two submenu
menubar.add_cascade(label='File',menu=filemenu)
exitmenu=Menu(root,tearoff=0)
exitmenu.add_command(label='Exit',command=root.destroy)
menubar.add_cascade(label='Exit',menu=exitmenu)
#++++++++++++++++++++++++++++++++++++++++++++++++++++++
#Defining inside frame which is being used for placing of checkbox 
insideFrame=Frame(f2,height=604,width=604)
insideFrame.pack()
insideFrame.place(x=400,y=100)

#defining verifyframe inside which two button reset and verify is placed
verifyFrame=Frame(f2,height=60,width=604,bg='#888888')
verifyFrame.pack()
verifyFrame.place(x=400,y=710)
#defining DescLabel for displaying the task that user has to perform 
DescLabel=Label(f2,height=4,width=60,text='',bd=3,bg='#90CAF9',font=('Arial',12,'bold'))
DescLabel.pack()
DescLabel.place(x=400,y=18)

#creating a option list which have name of task string and random function will be used later to select one from it
option=['Traffic Light','House','Store','Dog','Car','Bus','Cat']
#defining str1 to avoid runtime conflict
str1=""
#defining boolean variable and integer variable for associating with checkbox
v1,v2,v3,v4,v5,v6,v7,v8,v9=True,True,True,True,True,True,True,True,True
x1=x2=x3=x4=x5=x6=x7=x8=x9=0
#defining Click() function for all major operation
def click():
	#random option will be choose
	randomval=random.choice(option)
	str1="Click on the picture of "+randomval #giving user a task 
	DescLabel['text']=str1 #inserting str1 into text attribute of descLabel
	#below image is being choosen randomnly 
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

	#below IntVar variable are being defined in order to store value of checkbox status,that is either 1 or 0 (1 is if image is clicked or else 0)
	var1=IntVar()
	var2=IntVar()
	var3=IntVar()
	var4=IntVar()
	var5=IntVar()
	var6=IntVar()
	var7=IntVar()
	var8=IntVar()
	var9=IntVar()

	#below defining storevalue function which extract checkbox status value using get() function and store them in variable x1 to x9 for 9 images
	def storevalue():
		print('in')
		#definig global variable in order to change value at later stage of execution
		global x1,x2,x3,x4,x5,x6,x7,x8,x9
		global v1,v2,v3,v4,v5,v6,v7,v8,v9
		t1=t2=t3=t4=t5=t6=t7=t8=t9=0

		#using Regex method and compile a regex expression and storing it in variable strc which can be used in re.match() arguments.
		strc=re.compile(r"("+randomval+".....)")

		#below var1 to var9 variable taking there checkbutton associated status using get() and storing them into x1 to x9 repectively
		x1=var1.get()
		#for image 1 and checkbutton 1
		if x1==1:	#x1==1 that means that the first checkbutton is selected  
			if re.match(strc,pic1): #Regex expression is being match ,that is task given and image value is being match to check result
				v1=True				#if Regex is match and result true is passed
			else:
				v1=False			#if regex doesnot match then false is return
				print(v1)
		if x1!=1:
			v1=True					#this is to make sure that even after regex is matched (meaning task and image associated are matched) but user does not click it then false is return 
			if re.match(strc,pic1):
				v1=False				

		#for image 2 and checkbutton 2
		x2=var2.get()
		if x2==1:
			if re.match(strc,pic2):
				v2=True
			else:
				v2=False
				print(v2)
		if x2!=1:
			v2=True
			if re.match(strc,pic2):
				v2=False

		#for image 3 and checkbutton 3
		x3=var3.get()
		if x3==1:
			if re.match(strc,pic3):
				v3=True
			else:
				v3=False
				print(v3)
		if x3!=1:
			v3=True
			if re.match(strc,pic3):
				v1=False

		#for image 4 and checkbutton 4
		x4=var4.get()
		if x4==1:
			if re.match(strc,pic4):
				v4=True
			else:
				v4=False
				print(v4)
		if x4!=1:
			v4=True
			if re.match(strc,pic4):
				v4=False

		#for image 5 and checkbutton 5
		x5=var5.get()
		if x5==1:
			if re.match(strc,pic5):
				v5=True
			else:
				v5=False
				print(v5)
		if x5!=1:
			v5=True
			if re.match(strc,pic5):
				v5=False


		#for image 6 and checkbutton 6
		x6=var6.get()
		if x6==1:
			if re.match(strc,pic6):
				v6=True
			else:
				v6=False
				print(v6)
		if x6!=1:
			v6=True
			if re.match(strc,pic6):
				v6=False


		#for image 7 and checkbutton 7
		x7=var7.get()
		if x7==1:
			if re.match(strc,pic7):
				v7=True
			else:
				v7=False
				print(v7)
		if x7!=1:
			v7=True
			if re.match(strc,pic7):
				v7=False


		#for image 8 and checkbutton 8
		x8=var8.get()
		if x8==1:
			if re.match(strc,pic8):
				v8=True
			else:
				v8=False
				print(v8)
		if x8!=1:
			v8=True
			if re.match(strc,pic8):
				v8=False


		#for image 9 and checkbutton 9
		x9=var9.get()
		if x9==1:
			if re.match(strc,pic9):
				v9=True
			else:
				v9=False
				print(v9)
		if x9!=1:
			v9=True
			if re.match(strc,pic9):
				v9=False

	#Below veifyfun() is defined to check that given images those are checked are matching with task or not
	def verifyfun():
		#For Debugging 
		print(v1,v2,v3,v4,v5,v6,v7,v8,v9)
		print(x1,x2,x3,x4,x5,x6,x7,x8,x9)

		#if all the images that are checked and task are matching then success
		if (v1==True and v2==True and v3==True and v4==True and v5==True and v6==True and v7==True and v8==True and v9==True) and ( x1==1 or x2==1 or  x3==1 or x4==1 or  x5==1 or x6==1 or  x7==1 or x8==1 or x9==1):
			doneframe=Frame(root,height=766,width=1920,bg='#FFF9C4')
			doneframe.propagate(0)
			f2.pack_forget()
			doneframe.pack()
			verlabel=Label(doneframe,height=3,width=50,text="Verification Successfull",fg='black',font=('Adobe Fangsong Std R',20,'italic'))
			verlabel.pack()
			verlabel.place(x=400,y=400)

		else:
			print('Error')#if checked images and task doesnot match then not sucess and even in task given and images checked are matched (nextline)
			errorframe=Frame(root,height=766,width=1920,bg='#FFF9C4')#but there are some images which user doesdnot click but are matched with  task then varify is not success
			errorframe.propagate(0)
			f2.pack_forget()
			errorframe.pack()
			errlabel=Label(errorframe,height=3,width=50,text="Verification Unsuccessfull",fg='black',font=('Adobe Fangsong Std R',20,'italic'))
			errlabel.pack()
			errlabel.place(x=400,y=400)	
	#checkbutton are defined below
	img1=Checkbutton(insideFrame,image=photo1,variable=var1,height=200,width=200,relief=RAISED,bd=4,fg='red',command=storevalue)
	img1.image=photo1
	img1.pack()
	img1.place(x=0,y=0)

	img2=Checkbutton(insideFrame,image=photo2,variable=var2,height=200,width=200,relief=RAISED,bd=4,command=storevalue)
	img2.image=photo2
	img2.pack()
	img2.place(x=200,y=0)

	img3=Checkbutton(insideFrame,image=photo3,variable=var3,height=200,width=200,relief=RAISED,bd=4,command=storevalue)
	img3.image=photo3
	img3.pack()
	img3.place(x=400,y=0)

	img4=Checkbutton(insideFrame,image=photo4,variable=var4,height=200,width=200,relief=RAISED,bd=4,command=storevalue)
	img4.image=photo4
	img4.pack()
	img4.place(x=0,y=200)

	img5=Checkbutton(insideFrame,image=photo5,variable=var5,height=200,width=200,relief=RAISED,bd=4,command=storevalue)
	img5.image=photo5
	img5.pack()
	img5.place(x=200,y=200)

	img6=Checkbutton(insideFrame,image=photo6,variable=var6,height=200,width=200,relief=RAISED,bd=4,command=storevalue)
	img6.image=photo6
	img6.pack()
	img6.place(x=400,y=200)

	img7=Checkbutton(insideFrame,image=photo7,variable=var7,height=200,width=200,relief=RAISED,bd=4,command=storevalue)
	img7.image=photo7
	img7.pack()
	img7.place(x=0,y=400)

	img8=Checkbutton(insideFrame,image=photo8,variable=var8,height=200,width=200,relief=RAISED,bd=4,command=storevalue)
	img8.image=photo8
	img8.pack()
	img8.place(x=200,y=400)

	img9=Checkbutton(insideFrame,image=photo9,variable=var9,height=200,width=200,relief=RAISED,bd=4,command=storevalue)
	img9.image=photo9
	img9.pack()
	img9.place(x=400,y=400)

	#verify button is defined below
	verify=Button(verifyFrame,text='Verify',relief=RAISED,bd=3,command=verifyfun)
	verify.pack()
	verify.place(x=550,y=12)
#reset button is defined below
Reset=Button(verifyFrame,text='Reset',relief=RAISED,bd=3,command=click)
Reset.pack()
Reset.place(x=10,y=12)
#calling click() for displaying of images and checkbutton and major operation
click()

root.mainloop()