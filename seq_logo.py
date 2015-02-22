from Bio.Seq import Seq
from Bio import motifs
from Tkinter import *
import threading
from time import sleep
import tkFont


# class NumberCanvas(Canvas):
# 	def __init__(self, master, number, color, textSize):
# 		Canvas.__init__(self, master)
# 		self.number = number
# 		self.color = color
# 		self.textSize = textSize
# 		self.initWidgets()
# 		self.config(width = textSize*2, height = textSize*2)

# 	def initWidgets(self):
# 		helv36 = tkFont.Font(family="TkFixedFont",size=self.textSize)
# 		self.create_text(self.textSize, self.textSize, text = str(self.number), fill = self.color, font = helv36)
# 		self.pack()


class LetterLabel(Label):
	def __init__(self, master, letter, width, height):
		Label.__init__(self, master)
		self.letter = letter
		self.width = width
		self.height = height
		self.config(text = str(self.letter))
		self.config(height = self.height, width = self.width)

# root = Tk()
# # seqs = ['ACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGT',
# # 		'ACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGT',
# # 		'ACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGT']
# # logo = LogoGUI(seqs, 20, root)
# # root.geometry('400x60')
# w = LetterLabel(root, 'A', 20, 100)
# w.pack();
# root.mainloop()





class NumLabel(Label):
	def __init__(self, master, number, textSize):
		Label.__init__(self, master)
		self.number = number
		self.textSize = textSize
		self.config(text = str(self.number))
		self.config(bg="white")
		self.bind("<Enter>", self.enter_event)
		self.bind("<Leave>", self.leave_event)
		self.bind("<Button-1>", self.click_one_event)
	def enter_event(self, event):
		self.config(bg = "green")
	def leave_event(self, event):
		self.config(bg = "white")
	def click_one_event(self, event):
		# to be implemented
		print 'click '+str(self.number)

class LogoGUI(Frame):

	def __init__(self, seqs, textSize, master = None):
		Frame.__init__(self, master)
		self.seqs = seqs
		self.textSize = textSize
		self.pack()
		# init widgets
		# canvas
		self.line_frame_cvs = Canvas(self)
		# inner frame
		self.line_frame = Frame(self.line_frame_cvs)
		# scroll bar
		self.hbar=Scrollbar(self,orient=HORIZONTAL, command = self.line_frame_cvs.xview)
		self.line_frame_cvs.configure(xscrollcommand=self.hbar.set)
		# pack
		self.hbar.pack(side=BOTTOM,fill=X)
		self.line_frame_cvs.pack(side="top", fill=BOTH, expand = True)
		# self.line_frame.pack(side="bottom")
		self.line_frame_cvs.create_window((0, 0), window = self.line_frame, anchor="nw")
		self.line_frame.bind("<Configure>", self.OnFrameConfigure)
		# create canvases 
		self.positions = []
		for i in range(1, len(seqs[0])+1):
			# create a number_canvas
			label = NumLabel(self.line_frame, number = str(i), textSize = 20)
			self.positions.append(label)
			label.pack(side="left")
		
	def OnFrameConfigure(self, event):
		self.line_frame_cvs.configure(scrollregion=self.line_frame_cvs.bbox("all"))


#test driver
root = Tk()
seqs = ['ACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGT',
		'ACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGT',
		'ACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGT']
logo = LogoGUI(seqs, 20, root)
root.geometry('400x60')
logo.mainloop()
