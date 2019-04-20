from tkinter import *

class BuckyButtons:
	def __init__(self, master):
		frame = Frame(master)
		frame.pack()

		self.printButton = Button(frame, text="print message", command=self.printMessage)  
		# self.printMessage 从自身class中创建的function，因为不是永远call，所以要另外define，不在__init__中
		self.printButton.pack(side=LEFT)

		self.quitButton = Button(frame, text="quit", command=frame.quit) # 从自身class中创建的attribute：quitButton
		self.quitButton.pack(side=LEFT)

	def printMessage(self):
		print('WOw, this acutally worked!')




root = Tk()
b = BuckyButtons(root) # this is an object, root is treated as master parameter, *args

root.mainloop()

# frame in Tk()window, button in frame, function in button