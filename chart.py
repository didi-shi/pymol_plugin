from constants import *
from Tkinter import *
import random
import os
from PIL import Image
import math

class Logo(Canvas):
	def __init__(self, seqs, master = None):
		Canvas.__init__(self, master)
		self.config(height=LOGO_CANVAS_HEIGHT)
		self.config(bg='grey')
		self.seqs = seqs
		self.buildChart()

	def buildChart(self):
		# at each position, create a logobar object, append to self
		length = len(self.seqs[0])
		for i in range(0, length):
			# compute each letter's weight
			components = {}
			for seq in self.seqs:
				residue = seq[i]
				if residue not in components:
					components[residue] = 1
				else:
					components[residue] += 1
			# normalize 
			for key in components:
				components[key] /= float(len(self.seqs))
				# print components[key]
			bar = LogoBar(components, self)
			bar.pack(side = 'left')




class LogoBar(Canvas):
	def __init__(self, components, master = None):
		Canvas.__init__(self, master)
		self.components = components
		self.config(bg='white')
		self.config(bd = 0)
		self.config(width = LOGO_BAR_WIDTH, height = LOGO_BAR_HEIGHT)
		self.drawComponents()

	def drawComponents(self):
		# for each component, stretch image based on proportion
		for comp in self.components:
			# desired height
			height = math.floor(LOGO_BAR_HEIGHT * self.components[comp])
			# width
			width = LOGO_BAR_WIDTH
			# resizeImage 
			newFilePath = self.resizeImage(comp, height, width)
			rcvs = ResidueCVS(self, newFilePath, height, width)
			rcvs.pack(side = 'top')

	def resizeImage(self, residue, height, width):
		origin = Image.open(IMAGE_PATH+residue+'.png')
		origin = origin.resize((int(width), int(height)), Image.ANTIALIAS)
		filepath = self.randomFileName()
		origin.save(filepath, "png")
		return filepath

	def randomFileName(self):
		# 12-length random file name in cache
		name = []
		up_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
		digits = '0123456789'
		for i in range(0, RDM_FILE_NAME_LEN):
			l = random.choice(up_letters)
			d = random.choice(digits)
			choice = random.choice((l, d))
			name.append(choice)
		path = ''.join(name)
		return CACHE_PATH+path + '.png'




class ResidueCVS(Canvas):
    def __init__(self, master, path, height, width):
        Canvas.__init__(self, master)
        self.config(width = width, height = height, highlightthickness=0)
        self.config(bg = 'white')
        self.config(bd = 0)
        self.image = PhotoImage(file=path)
        self.create_image(0, 0, image=self.image,anchor=NW)
        self.pack(fill=BOTH, expand=1)





