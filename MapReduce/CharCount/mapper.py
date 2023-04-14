import sys

for line in sys.stdin:
	line = line.strip()
	chars = line.replace(" ", "")
	
	for char in chars:
		print "%s\t%s" % (char, 1)
