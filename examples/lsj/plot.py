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
zoom = 5
ms = 58000.0
figDatas = []
for row in range(0, ySize, zoom):
    for column in range(0, xSize, zoom):
        figDatas.append(datas[row*xSize + column][3:6])

xSize, ySize, zSize = xSize/zoom, ySize/zoom, 1

import numpy as np
x, y, z = np.meshgrid(np.arange(0, xSize, 1), np.arange(0, ySize, 1), np.arange(0, zSize, 1))
u = v = w = np.zeros((ySize, xSize, zSize))

for i, data in enumerate(figDatas):
    u[i/xSize][i%xSize][0] = data[0]/ms
    v[i/xSize][i%xSize][0] = data[1]/ms
    w[i/xSize][i%xSize][0] = data[2]/ms

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.quiver3D(x, y, z, u, v, w, length=0.01, arrow_length_ratio=0.3, pivot='middle')
plt.show()
