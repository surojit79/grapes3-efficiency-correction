import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import matplotlib.gridspec as gridspec
from scipy import stats
from scipy.ndimage.filters import gaussian_filter1d
###########################################################


input_value = int(input("Enter the input value: "))
direction_value = int(input("Enter the direction number: "))
############################################################



#########################################################
num_window=np.load(f"Direction{direction_value}_yearly_Window_raw_{2000+input_value}.npy")
t=np.load(f"Direction{direction_value}_yearly_module0_block_data_time_{2000+input_value}.npy")	



print(num_window)






gap_index=[]

for i in range(len(num_window)):

	#print(num_window[i],np.round(t[i],4))
	indices=np.where(t ==num_window[i])
	#print(indices[0][0])
	
	gap_index.append(indices[0][0]+1)
	

	
gap_index=np.array(gap_index)

#print(gap_index)
####################################################
############################################################

for w in range(len(num_window)):

	A=np.load(f"Direction{direction_value}_yearly_ref_module_division{w}_{2000+input_value}.npy")

	print(A[0])


	t=np.load(f"Direction{direction_value}_yearly_module0_block_data_time_{2000+input_value}.npy")	
		
	if w==0:
		t=t[:gap_index[w]]
	else:
	
		t=t[gap_index[w-1]:gap_index[w]]
		
	#print(t[0],t[-1])
		
	print(A[0],A[1])
	
	
	label=f"{A[0]}_"+f"{A[1]}"
		
	ref1=np.load(f"Direction{direction_value}_yearly_module{A[0]}_block_data_{2000+input_value}.npy")
	ref2=np.load(f"Direction{direction_value}_yearly_module{A[1]}_block_data_{2000+input_value}.npy")
	x=(ref1+ref2)/2.0
	
	
	if w==0:
		x=x[:gap_index[w]]
	else:
	
		x=x[gap_index[w-1]:gap_index[w]]
	
	#plt.plot(t,x,label=label)
	#plt.legend()
	#plt.show()
	
	
	F=[]
	G=[]
	X_mm=[]
	index=[]
	
	for k in range(16):
	
		z=np.load(f"Direction{direction_value}_yearly_module{k}_block_data_{2000+input_value}.npy")
		
		if w==0:
			z=z[:gap_index[w]]
		else:
	
			z=z[gap_index[w-1]:gap_index[w]]
			
			
		res=stats.pearsonr(x,z)
		X_mm.append(res[0])
		index.append(k)
		F.append(res[0])
		G.append(k)
		
		
	X_mm=np.array(X_mm)
	index=np.array(index)
	
		
	F=np.array(F)
	G=np.array(G)
	
	print(F)
	print(G)
	
	npr=f"Direction{direction_value}_yearly_num_div_value{w}_{2000+input_value}"
	nps=f"Direction{direction_value}_yearly_num_div_number{w}_{2000+input_value}"
	np.save(npr,F)
	np.save(nps,G)
	


	
		
		
	
	
	
	
	
	
	
	
