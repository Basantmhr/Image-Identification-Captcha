from tkinter import*
class MainF:
	def buttonClick(self):
		
		frame1=Frame(root,height=1080,width=1920,bg="black")
		canvas1=Canvas(frame1)
		canvas1.create_rectangle(20,40,400,200,width=3)
root=Tk()
root.mainloop()