import sys
import os

if __name__ == "__main__":
	avgs = sys.argv[1:]
	
	if len(avgs) < 1 or len(avgs) > 2 :
		print("Input font file path argument please!!")
		quit()

	read_file = avgs[0]
	write_file = avgs[1]
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
