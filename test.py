from util import *

parser = PDBParser('test.txt')
seq = parser.getSequence()
for s in seq:
		print s+' ',

print '\n'
