import math
eps=0.001
s=0
i=1
z1=1
z=1
while math.fabs(z)>eps:
  i=i+1
  z1=i*i
  z=1/z1
  s=s+z
print('S=',s)
