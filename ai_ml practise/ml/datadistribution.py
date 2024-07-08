import numpy as np
import matplotlib.pyplot as plt
#loc= mean or high lvl, scale(standard deviation) = flat, ground, size= how much values... if(2,3) then 2d array with 3 values
data_distribution = np.random.normal(loc=30,scale=50,size=100)
plt.hist(data_distribution,bins=30,edgecolor='black',density=True)
plt.title('Histogram-data_distribution')
plt.xlabel('Values')
plt.ylabel('Frequesncy')
plt.show()

#for bell curve
mean=50
std_dev=10
sample_size=1000
normal_data=np.random.normal(loc=mean,scale=std_dev,size=sample_size)
plt.hist(normal_data,bins=30,edgecolor='orange',density=True)
plt.title('Normal')
plt.xlabel('value')
plt.ylabel('probability density')
plt.show()

#multiple independent vaiables and oone dependent variables
