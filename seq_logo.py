from Tkinter import *
import tkFont
from chart import *
from constants import *
from pymol.wizard import Wizard
from pymol import cmd
import threading

class LetterLabel(Label):
	def __init__(self, master, letter, width, height):
		Label.__init__(self, master)
		self.letter = letter
		self.width = width
		self.height = height
		self.config(text = str(self.letter))
		self.config(height = self.height, width = self.width)
		self.config(bg = 'blue')



class ResidueLabel(Label):
	def __init__(self, master, residue, position, textSize):
		Label.__init__(self, master)
		self.position = position
		self.residue = residue
		self.textSize = textSize
		self.config(width = LOGO_BAR_WIDTH)
		# inner_cvs = Canvas(self)
		# inner_cvs.create_text(20, 30, anchor=W, font="Purisa",
  		#      text=self.residue)
		# inner_cvs.pack(side='top')
		self.config(text = str(self.residue))
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
		print 'click '+self.residue+' at position '+str(self.position)

class LogoGUI(Frame):

	def __init__(self, query, seqs, textSize, master = None):
		Frame.__init__(self, master)
		self.seqs = seqs
		self.query = query
		self.textSize = textSize
		self.pack()
		# init widgets

		# headline
		head = Label(self, text = 'sequence logo')
		head.pack(side = 'top')

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

		# create logo canvas
		self.logo_cvs = Logo(self.seqs, self.line_frame)
		self.logo_cvs.pack(side='top', fill = X)

		# create canvases 
		self.positions = []
		for i in range(0, len(query)):
			# create a number_canvas
			label_frame = Frame(self.line_frame, width = LOGO_BAR_WIDTH, height = 20, bd = 1)
			label = ResidueLabel(label_frame, residue = query[i], position = i, textSize = 20)
			self.positions.append(label)
			label_frame.pack(side = 'left')
			label_frame.pack_propagate(0)
			label.pack(fill = X, side='left')
		
	def OnFrameConfigure(self, event):
		self.line_frame_cvs.configure(scrollregion=self.line_frame_cvs.bbox("all"))

# draw letter on canvas

class LogoThread(threading.Thread):
	def __init__(self, search_id, thecmd):
		threading.Thread.__init__(self)
		self.search_id = search_id
		self.cmd = thecmd


	def run(self):
		print 'about to render Tk application'
		root = Tk()
		query = 'ACTGCAGTCATGCATGCAGTCGATCGATCGATCGATCGAT'
		seqs = ['ACAGCAGTCATGCATGCGTCGATCGATCGATCGATCGATA',
			'CAGGCTGTCAGACAGACAGTCGATCGATCGATCGATCGAT',
			'ACTGCGCACAAGCATGCAGTCGATCGATCGATCGATCGAT']
		# seqs = []
		# path = 'cache/'+str(search_id)
		# with open(path, 'r') as f:
		# 	for line in f:
		# 		seqs.append(line.strip())
		# # placeholder for query
		# query = ''.join(['A']*len(seqs[0]))
		# print 'seqs: '
		# print seqs
		# print 'query: '
		# print query
		logo = LogoGUI(query, seqs, 20, root)
		size = str(LOGO_GUI_WIDTH)+'x'+str(LOGO_GUI_HEIGHT)
		root.geometry(size)
		logo.mainloop()


def start_seq_logo_thread(cmd, search_id):
	thread = LogoThread(search_id, cmd)
	thread.start()
	thread.join()
	# thread_func(search_id, cmd)


# start_seq_logo_thread(1, 'cmd')



#test driver
# root = Tk()
# query = 'ACTGCAGTCATGCATGCAGTCGATCGATCGATCGATCGAT'
# seqs = ['ACAGCAGTCATGCATGCGTCGATCGATCGATCGATCGATA',
# 		'CAGGCTGTCAGACAGACAGTCGATCGATCGATCGATCGAT',
# 		'ACTGCGCACAAGCATGCAGTCGATCGATCGATCGATCGAT']
# logo = LogoGUI(query, seqs, 20, root)
# size = str(LOGO_GUI_WIDTH)+'x'+str(LOGO_GUI_HEIGHT)
# root.geometry(size)
# logo.mainloop()
