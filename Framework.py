from tkinter import*
#from Frame1 import MainF
class MainF:
	def buttonClick(self):
		root1=Tk()
		root1.title("Image")
		root1.geometry("1920x1080")
		#frame1=Frame(root1,height=1080,width=1920,bg="black")
		canvas1=Canvas(root1,height=800,width=800,bg='red')
		canvas1.create_rectangle(20,40,400,200,width=3)
		canvas1.pack()
		root1.mainloop()
root=Tk()
root.title("Image Identification Captcha V.1 ")
root.wm_iconbitmap('icc.ico') #Test case icon
root.geometry('1920x766')
c=Canvas(root,bg='grey',height=300,width='900',cursor='arrow')
c.pack()
fnt=('Times',40,'italic underline')
id=c.create_text(500,100,text="Image Identification Captcha",font=fnt)
f=Frame(root,height='500',width='1920',bg='blue',cursor='arrow')
f.propagate(0)
f.pack()
btn1=MainF()
b=Button(f,text='Start Image Identification Captcha',width='30',height='2',command=(btn1.buttonClick))
b.place(x=670,y=280)
#btn1.b.bind('<Button-1>',btn1.buttonClick)
exit=Button(f,text='Exit',width='10',height='2',command=quit)
exit.place(x=730,y=322)
root.mainloop()