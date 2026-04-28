import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import matplotlib.gridspec as gridspec
from scipy import stats
from scipy.ndimage.filters import gaussian_filter1d
from scipy.signal import savgol_filter
from astropy.stats import bayesian_blocks
####################################

input_value = int(input("Enter the input value: "))
direction_value = int(input("Enter the direction number: "))
#####################################
colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'orange', 'purple', 'brown', 'pink', 'olive', 'lime', 'gold', 'teal', 'indigo']



data=np.load(f"Direction{direction_value}_b1_muon_data_"+f"{2000+input_value}.npy")
time=np.load(f"Direction{direction_value}_b1_muon_data_time_"+f"{2000+input_value}.npy")
plt.plot(time,data,color='blueviolet',label='Reference')




#############################################

#################################################

t=time

plt.minorticks_on()
plt.tick_params('both', which='major',labelsize=12, length=6, width=1, direction='in', top=True, right=True, labelbottom=True)
plt.tick_params('both', which='minor', labelsize=12,length=4, width=1, direction='in', top=True, right=True)


##############################################

GM=data


#plt.plot(t,GM,color=colors[14])

#print(l)



for j in range(16):

	
		CC=[]
		y=np.load(f"Direction{direction_value}_yearly_module"+f"{j}_block_data_"+f"{2000+input_value}.npy")				
		x=t
		good_data=GM
		bad_data=y
		
		ratio = good_data / bad_data
		
		#plt.plot(x,good_data)
		#plt.plot(x,bad_data)
		#plt.show()
		
		res_g=stats.pearsonr(good_data,bad_data)
		#CC.append(res_g[0])
		
		ax=f"Module {j}"
		
		# Define Savitzky-Golay filter parameters
		window_length = 81  # Window length for smoothing (adjust as needed)
		
		#for n in [1,2,3,4,5,6,7,8,9,10]: 
		
		#	window_length = int(n*80+1)
			
		print(window_length)
		polyorder = 2 # Polynomial order for fitting (4 for 4th-order)

		# Apply the Savitzky-Golay filter to the ratio
		corrected_ratio = savgol_filter(ratio, window_length, polyorder)

		# Correct the bad data by multiplying it with the corrected ratio
		corrected_bad_data = bad_data * corrected_ratio
		
		# Plot the original bad data, corrected data, and the ratio
		#plt.figure(figsize=(12, 6))
		#plt.subplot(1, 2, 1)
		#plt.plot(x, good_data, label='Good Data', color='g')
		#plt.plot(x, bad_data, label='Bad Data', color='y')
		plt.plot(x, corrected_bad_data, label=ax, color=colors[j])
		
		"""
		plt.xlabel('X-axis')
		plt.ylabel('Y-axis')
		plt.legend()
		plt.title('Original Bad Data vs. Corrected Bad Data')
		plt.grid(True)
		
		plt.subplot(1, 2, 2)
		plt.plot(x, ratio, label='Ratio (Good/Bad)', color='green')
		plt.plot(x, corrected_ratio, label='Savitzky-Golay Corrected Ratio', color='purple')
		plt.xlabel('X-axis')
		plt.ylabel('Ratio')
		plt.legend()
		plt.title('Ratio and Savitzky-Golay Corrected Ratio')
		plt.grid(True)
		"""
		#plt.tight_layout()
		#plt.show()
		
		res=stats.pearsonr(good_data,bad_data)
		res1=stats.pearsonr(good_data,corrected_bad_data)
		print(res[0],res1[0])
		
		np.save(f"Direction{direction_value}_svg_eff_corrected_data{j}_{2000+input_value}",corrected_bad_data)
		np.save(f"Direction{direction_value}_svg_eff_corrected_time_data{j}_{2000+input_value}",x)

			
		
			

plt.ylabel('Muon rate (s$^{-1}$)',size='xx-large')
plt.xlabel('Time (days)',size='xx-large')
plt.xlim(np.min(t),np.max(t))
legend1=plt.legend(loc='upper left', bbox_to_anchor=(1, 1),fontsize=11)
for line in legend1.get_lines():
    line.set_linewidth(4)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.tight_layout()
plt.show()
	
	
	
	





