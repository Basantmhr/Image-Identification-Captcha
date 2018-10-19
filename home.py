from tkinter import*
import time
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



root.mainloop()