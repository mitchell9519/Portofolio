import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
values = range(1,1001)

cubes = [x**2 for x in values]

plt.style.use('seaborn')

fig1, ax = plt.subplots()
#can custom colour with three color values 
# ax.scatter(values,cubes,c='red' ,s=10,)
ax.scatter(values,cubes,c=cubes, cmap=plt.cm.Blues ,s=10,)
#colors higher y values darker
#thickness



#axis and labels
ax.set_title("Square Numbers",fontsize=24)
ax.set_xlabel('Intial values', fontsize=14)
ax.set_ylabel('Squares of values',fontsize=14)

##range pf axis
ax.axis([0,1100,0,1100000])

#styles plot points
#plt.show()
plt.savefig('cmap')
#watch scaling !

