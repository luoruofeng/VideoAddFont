import sys
import os
import re


def change_font_number(read_file,write_file):
	i = 1
	with open(read_file, "r") as rf:
		with open(write_file, "w+") as wf:
			lines = rf.readlines()
			for l in lines:
				r = re.match('^[1-9]\d*$',l)
				if r:
					if i != int(r.string):
						l = str(i)+"\n"
					i+=1
				wf.write(l)		