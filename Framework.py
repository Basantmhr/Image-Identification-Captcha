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
b=Button(f,text='Run',width='5',height='2')
b.pack()
b.bind('<Button-1>',buttonclick)

root.mainloop()