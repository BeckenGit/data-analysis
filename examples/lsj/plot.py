#Transfer the text file to 2D List
f = open("10.odt")
allDataStr = f.readlines()
numLinesStr = allDataStr[12: -1]
nums = []
for aStr in numLinesStr:
    aNumsStr = aStr.split()
    num = []
    for aNumStr in aNumsStr:
        num.append(float(aNumStr))
    nums.append(num)

f.close()
