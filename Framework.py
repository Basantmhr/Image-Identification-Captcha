from tkinter import*
def buttonclick(self):
	print('You have click me.')
root=Tk()
root.title("Image Identification Captcha V.1 ")
root.wm_iconbitmap('icc.ico') #Test case icon
root.geometry('1920x766')
c=Canvas(root,bg='grey',height=300,width='900',cursor='mouse')
c.pack()
fnt=('Times',40,'italic underline')
id=c.create_text(500,100,text="Image Identification Captcha",font=fnt)
f=Frame(root,height='500',width='1920',bg='blue',cursor='arrow')
f.propagate(0)
f.pack()
b=Button(f,text='Start Image Identification Captcha',width='30',height='2',)
b.pack()
b.place(x=670,y=280)
b.bind('<Button-1>',buttonclick)
exit=Button(f,text='Exit',width='10',height='2',command=quit)
exit.pack()
exit.place(x=730,y=322)
exit.bind('<Button-1>')

root.mainloop()