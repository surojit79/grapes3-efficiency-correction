import numpy as np
import matplotlib.pyplot as plt
import time as tt
from scipy.ndimage.filters import gaussian_filter1d

start_time = tt.time()
#######################################
num_year=int(input("Enter the year:"))
direction_value = int(input("Enter the direction number: "))

t=np.load(f"/home/surojit/Desktop/Muangle_plot/Data/Pres_TIME_MUON_S0_M0_{2000+20}.npy")

if num_year%4==0:
	monthDays = np.array([31, 29, 31, 30, 31, 30, 31, 31, 30,31,30,31])
else:
	monthDays = np.array([31, 28, 31, 30, 31, 30, 31, 31, 30,31,30,31])
#################################################

for l in range(4):
	for n in range(4):
		Raw_data=[]
		for L in range(num_year,num_year+1,1):
			for M in range(12):
				for N in range(monthDays[M]):
					x=np.load(f"/home/surojit/Desktop/New_data_analysis/Raw_data_4m/Direction{direction_value}_Raw_data_4m_module{4*l+n}_{2000+L}{(M+1):02d}{(N+1):02d}.npy")
					for i in range(len(x)):
						Raw_data.append(x[i])
						
						
		
		#
		#np.save(f"/home/surojit/Desktop/New_data_analysis/Muon_data/Raw_time_data_4m_bin/Direction225_Raw_data_4m_module{4*l+n}.npy",t)
		
		y=np.load(f"/home/surojit/Desktop/New_data_analysis/Pressure_data/Pressure_data_{2000+L}.npy")
		
		print(f"Pressure_data_{2000+L}.npy")		
		p_diff=y-np.mean(y)
		coeff=-0.00128
		R=[]
		for i in range(len(t)):
			R.append(Raw_data[i]/(1+coeff*p_diff[i]))
		R=np.array(R)
		
		#plt.plot(t,Raw_data)
		plt.plot(t,R)
		
		
		np.save(f"/home/surojit/Desktop/New_data_analysis/Muon_data/Raw_data_4m_bin/Direction{direction_value}_rejection{4*l+n}_{2000+L}.npy",R)
		#np.save(f"/home/surojit/Desktop/New_data_analysis/Muon_data/Raw_data_4m_bin/Direction225_pres_corrected_rejection{4*l+n}_{2000+L}.npy",R)
		
		np.save(f"/home/surojit/Desktop/New_data_analysis/Muon_data/Raw_data_4m_bin/rejection_time_{2000+L}.npy",t)

		
		#plt.xlim(0,10)
plt.show()
					
					
					
					
					
					
					
					
