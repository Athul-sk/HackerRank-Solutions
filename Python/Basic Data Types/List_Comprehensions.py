#You are given three integers x,y and z representing the dimensions of a cuboid along with an integer n.
#Print a list of all possible coordinates given by (i,j,k) on a 3D grid where the sum of i+j+k is not equal to n.

x = int(input())
y = int(input())
z = int(input())
n = int(input())
list=[]
for i in range(0,x+1):
    for j in range(0,y+1):
        for k in range(0,z+1):
            if i+j+k==n:
                continue
            list.append([i,j,k])
print(list)
