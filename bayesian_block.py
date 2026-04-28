import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import matplotlib.gridspec as gridspec
from scipy import stats
from scipy.ndimage.filters import gaussian_filter1d

from astropy.stats import bayesian_blocks
#####################################

input_value = int(input("Enter the input value: "))
direction_value = int(input("Enter the direction number: "))

t1=np.load(f"Direction{direction_value}_uninterrupted_data_time_{2000+input_value}.npy")

#####################################
colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'orange', 'purple', 'brown', 'pink', 'olive', 'lime', 'gold', 'teal', 'indigo']



plt.minorticks_on()
plt.tick_params('both', which='major', length=6, width=1, direction='in', top=True, right=True, labelbottom=True)
plt.tick_params('both', which='minor', length=4, width=1, direction='in', top=True, right=True)
######################################




num_leap_year=[]

if input_value %4==0:
	num_leap_year.append(1)
else:
	num_leap_year.append(0)
	
num_leap_year=	num_leap_year[0]

num_year=1

####################################

num_block=[]


time=[]

for l in range(16):

	#num_block=[]
	y=[]
	for m in range(input_value,input_value+1,1):
		x=np.load(f"Direction{direction_value}_uninterrupted_data_mod{l}_{2000+m}.npy")
		#time=np.load("/home/surojit/Desktop/EFF_CORRECTION/Data_2017_2022/2019/mod0_data_time_2019.npy")
		for n in range(len(x)):
			y.append(x[n])
	
	data=y
	
	
	
	
	#print(len(data))
	
	#plt.plot(time, data)
	# Define the desired number of data points after downsampling
	desired_num_points = 2920*num_year+8*num_leap_year

	# Calculate the downsampling factor
	downsampling_factor = len(data) // desired_num_points

	# Perform downsampling by averaging
	downsampled_data = []
	
	for i in range(0, len(data), downsampling_factor):
		average_value = np.mean(data[i:i+downsampling_factor])
		downsampled_data.append(average_value)

	# Generate downsampled time indices
	#downsampled_time = np.arange(0, len(downsampled_data) * downsampling_factor, downsampling_factor)
	
	
	
	#downsampled_time =(365*num_year+num_leap_year)*(downsampled_time /downsampled_time [-1])
	
	downsampled_time =np.arange(0,(365*num_year+num_leap_year),0.125)


	
	
	npxlabel=f"Direction{direction_value}_yearly_module{l}_block_data_{2000+input_value}"	
	np.save(npxlabel,downsampled_data)
	
	nptlabel=f"Direction{direction_value}_yearly_module{l}_block_data_time_{2000+input_value}"	
	np.save(nptlabel,downsampled_time)
	
	#plt.show()
	
	t=downsampled_time
	
	time.append(t)
	
	r1=np.array(downsampled_data,dtype=int)



	bins=bayesian_blocks(t,r1,fitness='events',p0=0.01)
	len(bins)
	
	print(l,len(bins))
	
	x=r1
	t_bb=[]
	x_bb=[]

	bins=np.array(bins)
	mean=[]
	for i in range(len(bins)-1):
		a=[]
		for j in range(len(t)):
			if bins[i]<=t[j]<=bins[i+1]:
				a.append(x[j])
		a=np.array(a)
    		#print(a)
		mean.append(a.mean())

	mean=np.array(mean)
	

	for i in range(len(bins)-1):
    		for j in range(len(t)):
        		if bins[i]<=t[j]<=bins[i+1]:
            			t_bb.append(t[j])
            			x_bb.append(mean[i])
	t_bb=np.array(t_bb) 
	x_bb=np.array(x_bb)
	


	m=x
	n=x_bb
	tn=t_bb


	plt.plot(t,x,color=colors[l])
	plt.plot(t_bb,x_bb,'k',lw=3)
	
	for edge in bins:
    		plt.axvline(edge, linestyle='dotted', alpha=1.0)


	nplabel=f"Direction{direction_value}_yearly_module_block_{2000+input_value}_{l}"
	print(nplabel)
	np.save(nplabel,bins)
	
	print(bins)
	
	plt.xlim(np.min(downsampled_time),np.max(downsampled_time))

plt.xlabel('Time (days)',size='x-large')
plt.ylabel('Muon Rate (s$^{-1}$)',size='x-large')
plt.show()

	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	


