import numpy as np
import matplotlib.pyplot as plt
import time as tt

start_time = tt.time()
#######################################
num_year=int(input("Enter the year:"))

direction_value = int(input("Enter the direction number: "))

if num_year%4==0:
	monthDays = np.array([31, 29, 31, 30, 31, 30, 31, 31, 30,31,30,31])
else:
	monthDays = np.array([31, 28, 31, 30, 31, 30, 31, 31, 30,31,30,31])
#################################################
Raw_data=[]

for l in range(4):
	for n in range(4):

		for L in range(num_year,num_year+1,1):
			for M in range(12):
				for N in range(monthDays[M]):
					try:
						x=np.load(f"/home/surojit/Desktop/New_data_analysis/Raw_data_10_sec/Direction{direction_value}_Raw_data_10s_module{4*l+n}_{2000+L}{(M+1):02d}{(N+1):02d}.npy")
						
						t=np.load(f"/home/surojit/Desktop/New_data_analysis/Raw_data_10_sec/Direction{direction_value}_Raw_time_data_10s_module{4*l+n}_{2000+L}{(M+1):02d}{(N+1):02d}.npy")
						
						
						print(f"{direction_value}_{4*l+n}_{2000+L}{(M+1):02d}{(N+1):02d}")
						#plt.plot(t,x)
						#plt.show()
						
						
						final_time, final_data= [],[]
						
						t_new = np.linspace(0, 1 - 1 / 360, 360)
						
						#print(len(t_new))
						#print(t_new[0],t_new[1])
						t_min, t_max, delta_t = t_new[0], t_new[-1], t_new[1] - t_new[0]
						
						
						
						while t_min<=t_max:

							sums = 0.0	
							count = 0
													
							for i3 in range(len(t)):
								if t_min<=t[i3]<t_min+delta_t:
									if x[i3]>0.0:
									
										sums+=x[i3]
										count+=1
									
																						
							final_data.append(sums / count if count > 0 else np.mean(x))
							

													
							final_time.append(t_min)
							t_min += delta_t
							
						final_time, final_data= (
								np.array(final_time), np.array(final_data))
								
						#plt.plot(final_time,final_data,'r')
						#plt.show()
						
						np.save(f"/home/surojit/Desktop/New_data_analysis/Raw_data_4m/Direction{direction_value}_Raw_data_4m_module{4*l+n}_{2000+L}{(M+1):02d}{(N+1):02d}.npy",final_data)
						np.save(f"/home/surojit/Desktop/New_data_analysis/Raw_data_4m/Direction{direction_value}_Raw_time_data_4m_module{4*l+n}_{2000+L}{(M+1):02d}{(N+1):02d}.npy",final_time)
					
					except FileNotFoundError:
						print(f"File not found for {4 * l + n}_{2000 + L}{(M + 1):02d}{(N + 1):02d}. putting zero...")

						final_data = np.zeros(360)
						final_time = np.linspace(0, 1 - 1 / 360, 360)
						np.save(f"/home/surojit/Desktop/New_data_analysis/Raw_data_4m/Direction{direction_value}_Raw_data_4m_module{4*l+n}_{2000+L}{(M+1):02d}{(N+1):02d}.npy",final_data)
						np.save(f"/home/surojit/Desktop/New_data_analysis/Raw_data_4m/Direction{direction_value}_Raw_time_data_4m_module{4*l+n}_{2000+L}{(M+1):02d}{(N+1):02d}.npy",final_time)
					
						continue
						
				
					
# Record the end time
end_time = tt.time()

# Calculate the elapsed time
runtime = end_time - start_time

print(f"Runtime: {runtime} seconds")
					
					
					
					
					
