import sys
import os

def change_font(read_file,write_file):
	s = " --> "
	with open(read_file, "r") as rf:
		with open(write_file, "w+") as wf:
			lines = rf.readlines()
			lines.reverse()
			resultl = []
			tempt = ""
			for l in lines:
				if s in l:
					print(l)
					tt = l[:l.index(s)]
					if tempt != "":	
						l = l[:l.index(s)+len(s)]+tempt+"\n"
					tempt = tt
					print(l)
				resultl.append(l)
			resultl.reverse()	
			wf.writelines(resultl)
