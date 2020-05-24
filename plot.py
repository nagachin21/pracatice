import matplotlib.pyplot as plt 
import numpy as np 

n = np.arange(-5, 6, 1)
x = []
y = []
theta = 0

for i in n:
    for j in n:
        x.append(i)
        y.append(j)

x2 = [-4,-4,-4,-4,-4,-4,-4,-4,-4,-3,-2,-1, 1, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 5]
y2 = [-4,-3,-2,-1, 0, 1, 2, 3, 4,-4,-4,-4, 4, 4,-4,-3,-2,-1, 0, 1, 2, 3, 4, 4, 4]

#線形変換前
plt.subplot(1,4,1)
plt.plot(x,y,marker='.',linestyle='None')
plt.plot(x2,y2,marker='o',linestyle='None')

plt.xlim(-7,7)
plt.ylim(-7,7)
plt.grid()

theta = 2 * np.pi / 3
A = [[np.cos(theta),-np.sin(theta)],[np.sin(theta),np.cos(theta)]]

for i in range(len(x)):
    tmp = np.dot(A,[x[i], y[i]])
    x[i] = tmp[0]
    y[i] = tmp[1]

for i in range(len(x2)):
    tmp = np.dot(A, [x2[i], y2[i]])
    x2[i] = tmp[0]
    y2[i] = tmp[1]
    
#線形変換後1
plt.subplot(1,4,2)
plt.plot(x,y,marker='.',linestyle='None')
plt.plot(x2,y2,marker='o',linestyle='None')

plt.xlim(-7,7)
plt.ylim(-7,7)
plt.grid()

for i in range(len(x)):
    tmp = np.dot(A,[x[i], y[i]])
    x[i] = tmp[0]
    y[i] = tmp[1]

for i in range(len(x2)):
    tmp = np.dot(A, [x2[i], y2[i]])
    x2[i] = tmp[0]
    y2[i] = tmp[1]
    
#線形変換後2
plt.subplot(1,4,3)
plt.plot(x,y,marker='.',linestyle='None')
plt.plot(x2,y2,marker='o',linestyle='None')

plt.xlim(-7,7)
plt.ylim(-7,7)
plt.grid()


for i in range(len(x)):
    tmp = np.dot(A,[x[i], y[i]])
    x[i] = tmp[0]
    y[i] = tmp[1]

for i in range(len(x2)):
    tmp = np.dot(A, [x2[i], y2[i]])
    x2[i] = tmp[0]
    y2[i] = tmp[1]
    
#線形変換後3
plt.subplot(1,4,4)
plt.plot(x,y,marker='.',linestyle='None')
plt.plot(x2,y2,marker='o',linestyle='None')

plt.xlim(-7,7)
plt.ylim(-7,7)
plt.grid()


plt.show()