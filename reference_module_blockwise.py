import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import matplotlib.gridspec as gridspec
from scipy import stats
from scipy.ndimage.filters import gaussian_filter1d


##########################################################
# Let's create a function to model and create data
def func(x, a, x0, sigma):
    return a*np.exp(-(x-x0)**2/(2*sigma**2))

##########################################################

input_value = int(input("Enter the input value: "))
direction_value = int(input("Enter the direction number: "))
###########################################################
num_window=np.load(f"Direction{direction_value}_yearly_Window_raw_{2000+input_value}.npy")
t=np.load(f"Direction{direction_value}_yearly_module0_block_data_time_{2000+input_value}.npy")	

gap_index=[]

for i in range(len(num_window)):

	#print(num_window[i],np.round(t[i],4))
	indices=np.where(t ==num_window[i])
	#print(indices[0][0])
	
	gap_index.append(indices[0][0]+1)
	

	
gap_index=np.array(gap_index)

#print(gap_index)
#############################################################
colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'orange', 'purple', 'brown', 'pink', 'olive', 'lime', 'gold', 'teal', 'indigo']
#############################################################

const=0



F1_std=[]
for n1 in range(16):

	x_n=np.load(f"Direction{direction_value}_yearly_module{n1}_block_data_{2000+input_value}.npy")
	plt.plot(t,x_n/x_n[0],color=colors[n1],label=f'M{n1:02d}')

	# Calculate the mean and standard deviation of the data
	mean_x_n = np.mean(x_n)
	std_x_n = np.std(x_n)
	F1_std.append(std_x_n)
	
	print(n1,std_x_n)
#plt.legend()
#plt.show()

############################



for w in range(0,len(gap_index),1):

	t=np.load(f"Direction{direction_value}_yearly_module0_block_data_time_{2000+input_value}.npy")	
	
	
	if w==0:
		t=t[:gap_index[w]]
	else:
	
		t=t[gap_index[w-1]:gap_index[w]]
	
	A=[17]
		
	while(len(A)<=15):	
		X_mm=[]
		index=[]
		for i in range(16):
			if i not in A:		
				a=[]
				
				npxlabel=f"Direction{direction_value}_yearly_module{i}_block_data_{2000+input_value}.npy"
				y=np.load(npxlabel)
				
				if w==0:
					y=y[:gap_index[w]]
				else:
	
					y=y[gap_index[w-1]:gap_index[w]]
				
				#y=y[m1*w:m1*w+m1]
				y=y/np.mean(y)
				
				plt.minorticks_on()
				plt.tick_params('both', which='major', length=6, width=1, direction='in', top=True, right=True, labelbottom=True)
				plt.tick_params('both', which='minor', length=4, width=1, direction='in', top=True, right=True)

				
				ax="Module"+f"{i}"
				plt.plot(t,y,color=colors[i],lw=1.5,label=ax)

		
				count_i=0
				for j in range(16):		
					if j not in A:
						if i!=j:
							npzlabel=f"Direction{direction_value}_yearly_module{j}_block_data_{2000+input_value}.npy"
							z=np.load(npzlabel)
							
							if w==0:
								z=z[:gap_index[w]]
							else:
	
								z=z[gap_index[w-1]:gap_index[w]]
							#z=z[m1*w:m1*w+m1]
							z=z/np.mean(z)
							res = stats.pearsonr(y,z)
							#print(i,j,res[0])					
							a.append(res[0])
						
				a=np.array(a)
				#print(i,np.mean(a))
		
				X_mm.append(np.mean(a))
				index.append(i)
					
		X_mm=np.array(X_mm)
		index=np.array(index)
		
		#print(X_mm,index)
		
		sorted_data = sorted(zip(X_mm, index))
		sorted_x, sorted_t = zip(*sorted_data)
		sorted_x=np.array(sorted_x)
		sorted_t=np.array(sorted_t)
		
		
		print('##############################')
		print(sorted_t[0],sorted_x[0])
		print('################################')
		
		
		plt.xlabel('Time (days)',size='x-large')
		plt.ylabel(r'Relative Muon rate',size='x-large')
		plt.xlim(np.min(t),np.max(t))
		plt.legend(frameon=True)	
		#plt.tight_layout()	
		#plt.savefig(bx)
		#plt.show()
		A.append(sorted_t[0])
		

	B=np.array(A)
	C=np.arange(16)
	
	print(B)
	print(C)
	
	E=[]
	E.append(B[-1])
	for v in range(len(C)):
		if C[v] not in B:
			E.append(C[v])
			
	print(w,E)
	
	np.save(f"Direction{direction_value}_yearly_ref_module_division{w}_{2000+input_value}",E)

	



















