# input Files
fstF = open("first.dat","r")
scdF = open("second.dat","r")
# output file
frthF = open("fourth.dat","w")

# Lists to append
lsToAppend = []

for line in fstF:
	lsToAppend.append(line)

for line in scdF:
	lsToAppend.append(line)

for i in lsToAppend:
	frthF.write(i) 
    
# Closing files
fstF.close()
scdF.close()
frthF.close()


def printString(whatToPrint):
	print(whatToPrint)
	return


if __name__ == "__main__":
	printString("Hi World")
	exit()
