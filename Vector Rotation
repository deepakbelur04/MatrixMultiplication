####Vector Rotaion Implementation
import numpy as np
import matplotlib.pyplot as plt

print ("Lets create a 3 dimensional vector on X Y Z axis")

x = int(input("Please input value for x co-ordinate"))

y = int(input("Please input value for y co-ordinate"))

z = int(input("Please input value for z co-ordinate"))

vectorAssign = np.array([x, y, z])

#print("vector formed " + str(vectorAssign))

print(np.reshape(vectorAssign,(3,1)))

#assignIdentity = np.identity(3,int)

#print(assignIdentity)

def x_rotation(vector,theta):
    """Rotates 3-D vector around x-axis"""
    R = np.array([[1,0,0],[0,np.cos(theta),-np.sin(theta)],[0, np.sin(theta), np.cos(theta)]])
    print("x_rotation R"+str(R))
    return np.dot(R,vector)

def y_rotation(vector,theta):
    """Rotates 3-D vector around y-axis"""
    R = np.array([[np.cos(theta),0,-np.sin(theta)],[0,1,0],[np.sin(theta), 0, np.cos(theta)]])
    print("y_rotation R"+str(R))
    return np.dot(R,vector)

def z_rotation(vector,theta):
    """Rotates 3-D vector around z-axis"""
    R = np.array([[np.cos(theta), -np.sin(theta),0],[np.sin(theta), np.cos(theta),0],[0,0,1]])
    print("z_rotation R"+str(R))
    return np.dot(R,vector)

# if x == 0 :
#     kuch toh likho
# else if y == 0:

fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot(np.linspace(0,vectorAssign[0]),np.linspace(0,vectorAssign[1]),np.linspace(0,vectorAssign[2]))

v1 = y_rotation(vectorAssign,45)
print("v1 XZ Plane" + str(v1))

v2 = z_rotation(v1,45)
print("v2 XY Plane" + str(v2))

v3 = z_rotation(v2,45)
print("v3 XY Plane" + str(v3))

v4 = x_rotation(v3,45)
print("v4 YZ Plane" + str(v4))


ax.plot(np.linspace(0,v1[0]),np.linspace(0,v1[1]),np.linspace(0,v1[2]))
ax.plot(np.linspace(0,v2[0]),np.linspace(0,v2[1]),np.linspace(0,v2[2]))
ax.plot(np.linspace(0,v3[0]),np.linspace(0,v3[1]),np.linspace(0,v3[2]))
ax.plot(np.linspace(0,v4[0]),np.linspace(0,v4[1]),np.linspace(0,v4[2]))


plt.show()