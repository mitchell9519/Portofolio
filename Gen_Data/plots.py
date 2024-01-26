import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
values = [1,2,3,4,5,6,7,8,9,10]
squares = [1,4,9,16,25,36,49,64,81,100]
cubes = [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]

plt.style.use('seaborn')

fig1, ax = plt.subplots()
#thickness
ax.plot(values,squares, linewidth=3,label = 'squares')
ax.plot(values,cubes, linewidth=3,label ='cubic')


#axis and labels
ax.set_title("Square Numbers",fontsize=24)
ax.set_xlabel('Intial values', fontsize=14)
ax.set_ylabel('Squares of values',fontsize=14)

#styles plot points
ax.tick_params(axis = 'both', labelsize =14)
plt.legend()
plt.show()


