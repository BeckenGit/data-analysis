#Transfer the text file to 2D List
f = open("10.odt")
allDataStr = f.readlines()
f.close()
numLinesStr = allDataStr[12: -1]
datas = []
for aStr in numLinesStr:
    aNumsStr = aStr.split()
    nums = []
    for aNumStr in aNumsStr:
        nums.append(float(aNumStr))
    datas.append(nums)

xSize, ySize, zSize = 400, 50, 1

import numpy as np
x, y, z = np.meshgrid(np.arange(0, xSize, 1), np.arange(0, ySize, 1), np.arange(0, zSize, 1))
u = v = w = np.zeros((ySize, xSize, zSize))

for i, data in enumerate(datas):
    u[i/xSize][i%xSize][0] = data[3]
    v[i/xSize][i%xSize][0] = data[4]
    w[i/xSize][i%xSize][0] = data[5]

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.gca(projection='3d')
#ax.quiver3D(x, y, z, u, v, w)
plt.show()
