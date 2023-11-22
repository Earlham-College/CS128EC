def AppendTwoFiles():
# input Files
    fstF = open("first.dat","r")
    scdF = open("second.dat","r")
# output file
    frthF = open("fourth.dat","w")
# List
    lsToAppend = []
    for line in fstF:
        if "AACCTTNN" in line:
            lsToAppend.append(line)
        else:
            pass

    for line in scdF:
        if "AACCTTNN" in line:
            lsToAppend.append(line)
        else:
            pass

    for i in lsToAppend:
        frthF.write(i)

# Closing files
    fstF.close()
    scdF.close()
    frthF.close()
    return


def printString(whatToPrint):
    AppendTwoFiles()
    print(whatToPrint)
    return


if __name__ == "__main__":
	printString("Hi World")
	exit()
