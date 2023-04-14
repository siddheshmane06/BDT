import sys

mMin = mMax = minDate = maxDate = None

for line in sys.stdin:
	line = line.strip().split(" ")
	print(line)
	date, tmax, tmin = line
	print(date)
	tmax = int(tmax)
	tmin = int(tmin)

	if(not minDate) or (not maxDate):
		mMax = tmax
		mMin = tmin
		minDate = date
		maxDate = date
	else:
		if tmax > mMax:
			mMax = tmax
			maxDate = date
		if tmin < mMin:
			mMin = tmin
			minDate = date
	
print("Minimum Temperature:", minDate, mMin)
print("Maximum Temperature:", maxDate, mMax)
