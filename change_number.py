import sys
import os
import re


if __name__ == "__main__":
	avgs = sys.argv[1:]
	
	if len(avgs) < 1 or len(avgs) > 2 :
		print("Input font file path argument please!!")
		quit()

	read_file = avgs[0]
	write_file = avgs[1]

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