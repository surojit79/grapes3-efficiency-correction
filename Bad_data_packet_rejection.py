import ROOT
import numpy as np
import matplotlib.pyplot as plt
import time as tt

##########################################
direction_169=np.load('/home/surojit/Desktop/Muangle_data/Convert_root_to_raw_data/Direction_coordinate/direction_169.npy')
direction_0=np.load('/home/surojit/Desktop/Muangle_data/Convert_root_to_raw_data/Direction_coordinate/direction_0.npy')
direction_1=np.load('/home/surojit/Desktop/Muangle_data/Convert_root_to_raw_data/Direction_coordinate/direction_1.npy')
direction_2=np.load('/home/surojit/Desktop/Muangle_data/Convert_root_to_raw_data/Direction_coordinate/direction_2.npy')
direction_3=np.load('/home/surojit/Desktop/Muangle_data/Convert_root_to_raw_data/Direction_coordinate/direction_3.npy')
direction_4=np.load('/home/surojit/Desktop/Muangle_data/Convert_root_to_raw_data/Direction_coordinate/direction_4.npy')
direction_5=np.load('/home/surojit/Desktop/Muangle_data/Convert_root_to_raw_data/Direction_coordinate/direction_5.npy')
direction_6=np.load('/home/surojit/Desktop/Muangle_data/Convert_root_to_raw_data/Direction_coordinate/direction_6.npy')
direction_7=np.load('/home/surojit/Desktop/Muangle_data/Convert_root_to_raw_data/Direction_coordinate/direction_7.npy')
direction_8=np.load('/home/surojit/Desktop/Muangle_data/Convert_root_to_raw_data/Direction_coordinate/direction_8.npy')


#################################


num_year=int(input("Enter the year:"))
start_time = tt.time()

##############################################
# Define a function to convert "hhmmss" to fractional day
def hhmmss_to_fractional_day(hhmmss):
    return (hhmmss // 10000) / 24 + ((hhmmss % 10000) // 100) / 1440 + (hhmmss % 100) / 86400

if num_year%4==0:
	monthDays = np.array([31, 29, 31, 30, 31, 30, 31, 31, 30,31,30,31])
else:
	monthDays = np.array([31, 28, 31, 30, 31, 30, 31, 31, 30,31,30,31])
#################################################
Raw_data=[]

for L in range(num_year,num_year+1,1):
	for M in range(10,12,1):
		for N in range(monthDays[M]):
		
			try:
				# Open the ROOT file
				
				filename=f"/home/surojit/Desktop/New_data_analysis/Raw_data/{2000+num_year}/ma{2000+L}{(M+1):02d}{(N+1):02d}.root"
				print(f"ma{2000+L}{(M+1):02d}{(N+1):02d}.root")
				
				
				
				file = ROOT.TFile.Open(filename)


				for l in range(4):

					num_tree="muangle"+f"{l}b"

					tree= file.Get(num_tree)
					

					if not isinstance(tree, ROOT.TTree):
						print(f"Error: Could not retrieve tree {num_tree}")
						continue  # or handle the error in an appropriate way


					
					nEntries = tree.GetEntries()
					
					# Fetch branches and leaves outside the loop
					branch_EDate = tree.GetBranch('EventHeader').GetLeaf('EDate')
					branch_ETime1 = tree.GetBranch('EventHeader').GetLeaf('ETime1')
					branch_Module = tree.GetBranch('EventHeader').GetLeaf('Module')
					branch_MaRate = tree.GetBranch('MaRate').GetLeaf('AngleRate')

					date, time, module,data,data_169,data_0,data_1,data_2,data_3,data_4,data_5,data_6,data_7,data_8 = [], [], [], [],[],[], [], [], [],[],[], [], [], []
					######################################################

					for i in range(nEntries):
						tree.GetEntry(i)
						
						EDate = int(branch_EDate.GetValue())
						ETime1 = int(branch_ETime1.GetValue())
						Module = int(branch_Module.GetValue())
				    
						date.append(EDate)
						time.append(ETime1)
						module.append(Module)	
						data.append(np.sum([int(branch_MaRate.GetValue(int(j))) for j in range(225)])/10.0)
						data_169.append(np.sum([int(branch_MaRate.GetValue(int(j))) for j in direction_169])/10.0)
						data_0.append(np.sum([int(branch_MaRate.GetValue(int(j))) for j in direction_0])/10.0)
						data_1.append(np.sum([int(branch_MaRate.GetValue(int(j))) for j in direction_1])/10.0)		
						data_2.append(np.sum([int(branch_MaRate.GetValue(int(j))) for j in direction_2])/10.0)
						data_3.append(np.sum([int(branch_MaRate.GetValue(int(j))) for j in direction_3])/10.0)
						data_4.append(np.sum([int(branch_MaRate.GetValue(int(j))) for j in direction_4])/10.0)
						data_5.append(np.sum([int(branch_MaRate.GetValue(int(j))) for j in direction_5])/10.0)		
						data_6.append(np.sum([int(branch_MaRate.GetValue(int(j))) for j in direction_6])/10.0)
						data_7.append(np.sum([int(branch_MaRate.GetValue(int(j))) for j in direction_7])/10.0)
						data_8.append(np.sum([int(branch_MaRate.GetValue(int(j))) for j in direction_8])/10.0)
						
					#######################################

					# Use NumPy for array operations
					date, time, module, data,data_169,data_0,data_1, data_2,data_3,data_4,data_5,data_6,data_7,data_8 =(
				 	np.array(date), np.array(time), np.array(module),
				 	np.array(data), np.array(data_169), np.array(data_0),
				 	np.array(data_1), np.array(data_2), np.array(data_3), 
				 	np.array(data_4), np.array(data_5), np.array(data_6),
				 	np.array(data_7),np.array(data_8))



					###########################################


					num_value = len(time) // 4
					#print(num_value)
					
					FINAL_T = [time[m * 4] for m in range(num_value)]
					y_updated = [hhmmss_to_fractional_day(tn) for tn in FINAL_T]
					
					#print(FINAL_T[0],FINAL_T[5],FINAL_T[-1])
					#print(y_updated[0],y_updated[5],y_updated[-1])
					
					# Create a dictionary for quick lookup of data based on time and module
					data_dict,data_dict_169,data_dict_0,data_dict_1,data_dict_2,data_dict_3,data_dict_4,data_dict_5,data_dict_6,data_dict_7,data_dict_8 = {},{},{},{},{},{},{},{},{},{},{}
					
					for k in range(len(time)):
						key = (time[k], module[k])
						if key not in data_dict:
							data_dict[key],data_dict_169[key],data_dict_0[key],data_dict_1[key],data_dict_2[key],data_dict_3[key],data_dict_4[key],data_dict_5[key],data_dict_6[key],data_dict_7[key],data_dict_8[key]= [],[],[],[],[],[],[],[],[],[],[]
							
						data_dict[key].append(data[k])
						data_dict_169[key].append(data_169[k])
						data_dict_0[key].append(data_0[k])
						data_dict_1[key].append(data_1[k])
						data_dict_2[key].append(data_2[k])
						data_dict_3[key].append(data_3[k])
						data_dict_4[key].append(data_4[k])
						data_dict_5[key].append(data_5[k])
						data_dict_6[key].append(data_6[k])
						data_dict_7[key].append(data_7[k])
						data_dict_8[key].append(data_8[k])
						

					for n in range(4):
					
						FD = [data_dict.get((time[m * 4], n), []) for m in range(num_value)]
						FD=  [inner_list if inner_list else [0.0] for inner_list in FD]
						
						
						FD1=[]
						for k1 in range (len(FD)):
							FD1.append(FD[k1][0])
						
						FD=np.array(FD1)					
						
						
						#print(len(y_updated),len(FD))
						plt.plot(y_updated,FD,'b')
						plt.ylabel('Muon Rate',size='x-large')
						plt.xlabel('Time (days)',size='x-large')
						#plt.show()
						
					
						FD1=[]
						for n1 in range(len(FD)):
							if np.mean(FD)-3*np.std(FD)<FD[n1]<np.mean(FD)+3*np.std(FD):
								FD1.append(FD[n1])
								
							else:
								FD1.append(0.0)
								#print(n1,FD[n1])
								
						FD=FD1
						
						
						np.save(f"/home/surojit/Desktop/New_data_analysis/Raw_data_10_sec/Direction225_Raw_data_10s_module{4*l+n}_{2000+L}{(M+1):02d}{(N+1):02d}.npy",FD)
						np.save(f"/home/surojit/Desktop/New_data_analysis/Raw_data_10_sec/Direction225_Raw_time_data_10s_module{4*l+n}_{2000+L}{(M+1):02d}{(N+1):02d}.npy",y_updated)
				file.Close()
				
			except Exception as e:
				print(f"Missing file ma{2000+L}{(M+1):02d}{(N+1):02d}.root: {e}")
				continue
					

	
#print(len(ALL_direction_data))		
#plt.plot(ALL_direction_data)
#plt.ylim(3000,3100)
#plt.show()

##############################################
# Record the end time
end_time = tt.time()

# Calculate the elapsed time
runtime = end_time - start_time

print(f"Runtime: {runtime} seconds")

#np.save("ALL_direction_data",ALL_direction_data)





