import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import matplotlib.gridspec as gridspec
from scipy import stats
from scipy.ndimage.filters import gaussian_filter1d

from astropy.stats import bayesian_blocks
####################################

input_value = int(input("Enter the input value: "))
direction_value = int(input("Enter the direction number: "))

#####################################
colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'orange', 'purple', 'brown', 'pink', 'olive', 'lime', 'gold', 'teal', 'indigo']



plt.minorticks_on()
plt.tick_params('both', which='major', length=6, width=1, direction='in', top=True, right=True, labelbottom=True)
plt.tick_params('both', which='minor', length=4, width=1, direction='in', top=True, right=True)

for l in range(16):
	x=np.load(f"Direction{direction_value}_yearly_module{l}_block_data_{2000+input_value}.npy")
	t=np.load(f"Direction{direction_value}_yearly_module0_block_data_time_{2000+input_value}.npy")
	#print(t[-1])
	#plt.plot(t,x,color=colors[l])
	
#plt.show()



#########################################


num_window=np.load(f"Direction{direction_value}_yearly_Window_raw_{2000+input_value}.npy")
#print(num_window)
###################################################################
t=np.load(f"Direction{direction_value}_yearly_module0_block_data_time_{2000+input_value}.npy")

gap_index=[]

for i in range(len(num_window)):

	#print(num_window[i],np.round(t[i],4))
	indices=np.where(t ==num_window[i])
	#print(indices[0][0])
	
	gap_index.append(indices[0][0]+1)
	

	
gap_index=np.array(gap_index)

#print(gap_index)

t1=t

##############################


REF=[]

for j in range(len(num_window)):
		ref=np.load(f"Direction{direction_value}_yearly_ref_module_division{j}_{2000+input_value}.npy")
		REF.append(ref)


#print(REF)
#print(REF[0][0],REF[0][1],REF[0][2])



#################################

plt.minorticks_on()
plt.tick_params('both', which='major', length=6, width=1, direction='in', top=True, right=True, labelbottom=True)
plt.tick_params('both', which='minor', length=4, width=1, direction='in', top=True, right=True)

for w in range(len(gap_index)):

	t=np.load(f"Direction{direction_value}_yearly_module0_block_data_time_{2000+input_value}.npy")

	
	if w==0:
		t=t[:gap_index[w]]
	else:
	
		t=t[gap_index[w-1]:gap_index[w]]
		
	#print(t[0],t[-1])
	
	#print(REF[w][0],REF[w][1])
	ref1=np.load(f"Direction{direction_value}_yearly_module{REF[w][0]}_block_data_{2000+input_value}.npy")
	ref2=np.load(f"Direction{direction_value}_yearly_module{REF[w][1]}_block_data_{2000+input_value}.npy")
	
	
	if w==0:
		ref1=ref1[:gap_index[w]]
		ref2=ref2[:gap_index[w]]
	else:
	
		ref1=ref1[gap_index[w-1]:gap_index[w]]
		ref2=ref2[gap_index[w-1]:gap_index[w]]
	
	
	reference=(ref1+ref2)/2.0
	
	xxxx="Ref_module_div"+f"{w}"
	
	plt.plot(t,reference,label=xxxx)
	
	
	npx=f"Direction{direction_value}_avg_best_two_modules_div_{w}_{2000+input_value}"
	npt=f"Direction{direction_value}_avg_best_two_modules_time_div_{w}_{2000+input_value}"
	
	np.save(npx,reference)
	np.save(npt,t)
	
	plt.vlines(x=num_window[w],ymin=2900,ymax=3100,color='r', linestyles='dashed')
	
plt.ylabel('Muon Rate (s$^{-1}$)',size='x-large')
plt.xlabel('Time (days)',size='x-large')
plt.ylim(2900,3100)
plt.xlim(np.min(t1),np.max(t1))
plt.legend()
plt.show()


#########################################################
A=[]

for b in range(len(gap_index)-1):
	bx=np.load(f"Direction{direction_value}_YEARLY_STITCH_REFERENCE_{b}_{2000+input_value}.npy")
	
	A.append(bx)
	
print(A)

print(len(A))


connection=[]
for a in range(len(gap_index)-1):


	G=[]
	for w in range(a,a+2,1):


		t=np.load(f"Direction{direction_value}_yearly_module0_block_data_time_{2000+input_value}.npy")
		
		
		if w==0:
			t=t[:gap_index[w]]
		else:
		
			t=t[gap_index[w-1]:gap_index[w]]
			
			
		x=np.load(f"Direction{direction_value}_avg_best_two_modules_div_{w}_{2000+input_value}.npy")
		
		x1=[]
		mean_x=np.mean(x)
		for j in range(len(x)):
			x1.append(mean_x)
		x1=np.array(x1)
		
		
		
		##############################
				
		y=np.load(f"Direction{direction_value}_yearly_module{A[a]}_block_data_{2000+input_value}.npy")
		
		if w==0:
			y=y[:gap_index[w]]
		else:

			y=y[gap_index[w-1]:gap_index[w]]
			
		y1=[]
		mean_y=np.mean(y)
		for j in range(len(y)):
			y1.append(mean_y)
		y1=np.array(y1)
		
	
		G.append(mean_x/mean_y)
		
		#print(mean_y)
		############################################
		#label_y
		
		label_y=f"Direction{direction_value}_Module_{A[a]}"	
		label_x=f"Avg_of_Module{REF[w][0],REF[w][1]}"
			
		#############################################
		"""
		plt.minorticks_on()
		plt.tick_params('both', which='major', length=6, width=1, direction='in', top=True, right=True, labelbottom=True)
		plt.tick_params('both', which='minor', length=4, width=1, direction='in', top=True, right=True)

			
		plt.plot(t,y,'b',lw=1.5,label=label_y)
		plt.plot(t,x,lw=1.5,label=label_x)
		
		plt.plot(t,x1,'k',lw=2)
		plt.plot(t,y1,'r',lw=2)
	plt.vlines(x=num_window[a],ymin=2500,ymax=3100,color='r', linestyles='dashed')
	plt.xlim(num_window[1],num_window[3])
	plt.ylabel('Muon Rate (s$^{-1}$)',size='x-large')
	plt.xlabel('Time (days)',size='x-large')
	plt.legend()
	plt.show()
	"""

	G=np.array(G)
	C=[]

	C.append(1.0)

	for m in range(len(G)-1):
		C.append(G[m*2]/G[2*m+1])
		connection.append(G[m*2]/G[2*m+1])

	print(C)

	C=np.array(C)
	
	
	##############################################
	for w in range(a,a+2,1):


		t=np.load(f"Direction{direction_value}_yearly_module0_block_data_time_{2000+input_value}.npy")
		
		
		if w==0:
			t=t[:gap_index[w]]
		else:
		
			t=t[gap_index[w-1]:gap_index[w]]
			
			
		x=np.load(f"Direction{direction_value}_avg_best_two_modules_div_{w}_{2000+input_value}.npy")
		
		x1=[]
		mean_x=np.mean(x)
		for j in range(len(x)):
			x1.append(mean_x)
		x1=np.array(x1)
		
		
		
		##############################
				
		y=np.load(f"Direction{direction_value}_yearly_module{A[a]}_block_data_{2000+input_value}.npy")
		
		if w==0:
			y=y[:gap_index[w]]
		else:

			y=y[gap_index[w-1]:gap_index[w]]
			
		y1=[]
		mean_y=np.mean(y)
		for j in range(len(y)):
			y1.append(mean_y)
		y1=np.array(y1)
		
		#print(mean_y)
		############################################
		#label_y
		
		label_y=f"Direction{direction_value}_Module_{A[a]}"	
		label_x=f"Direction{direction_value}_Avg_of_Module{REF[w][0],REF[w][1]}"
		
			
		#############################################
		"""
		plt.minorticks_on()
		plt.tick_params('both', which='major', length=6, width=1, direction='in', top=True, right=True, labelbottom=True)
		plt.tick_params('both', which='minor', length=4, width=1, direction='in', top=True, right=True)
	
		plt.plot(t,y,'b',lw=1.5,label=label_y)
		plt.plot(t,C[w-a]*x,lw=1.5,label=label_x)
		
		plt.plot(t,C[w-a]*x1,'k',lw=2)
		plt.plot(t,y1,'r',lw=2)
		
	plt.vlines(x=num_window[2],ymin=2900,ymax=3100,color='r', linestyles='dashed')
	plt.xlim(num_window[1],num_window[3])
	plt.ylabel('Muon Rate (s$^{-1}$)',size='x-large')
	plt.xlabel('Time (days)',size='x-large')
	plt.legend()
	plt.show()
	"""
np.save(f'Direction{direction_value}_YEARLY_stitch',connection)

#########################################################
#connection
connection=np.load(f'Direction{direction_value}_YEARLY_stitch.npy')
N=connection

C=[]
mul=1
C.append(1.0)
for n1 in range(len(N)):
	
	mul =mul*N[n1]
	
	C.append(mul)
	
	print(mul)
print(C)
print(len(C))
#########################################
##########################################
plt.minorticks_on()
plt.tick_params('both', which='major', length=6, width=1, direction='in', top=True, right=True, labelbottom=True)
plt.tick_params('both', which='minor', length=4, width=1, direction='in', top=True, right=True)


eff1=[]
effT=[]

for w1 in range(len(gap_index)):	
	x=np.load(f"Direction{direction_value}_avg_best_two_modules_div_{w1}_{2000+input_value}.npy")
	t=np.load(f"Direction{direction_value}_avg_best_two_modules_time_div_{w1}_{2000+input_value}.npy")
	
	for i in range(len(x)):
		eff1.append(C[w1]*x[i])
		effT.append(t[i])
	
	plt.plot(t,C[w1]*x)
	#plt.plot(t1,x1-90,'b',label='Mod_9')
	#plt.vlines(x=365,ymin=2900,ymax=3100,color='r', linestyles='dashed')
	#plt.vlines(x=365*2,ymin=2900,ymax=3100,color='r', linestyles='dashed')
	#plt.vlines(x=365*3,ymin=2900,ymax=3100,color='r', linestyles='dashed')
	#plt.vlines(x=365*4+1,ymin=2900,ymax=3100,color='r', linestyles='dashed')
	#plt.vlines(x=365*5,ymin=2900,ymax=3100,color='r', linestyles='dashed')

#plt.vlines(x=num_window[w1], ymin=np.min(x1-40), ymax=np.max(x1-40), colors='red', linestyles='dashed')
	
#plt.xlim(num_window[l]-80,num_window[l]+80)
#plt.xlim(num_window[2]-20,num_window[3]+20)
#plt.xlim(1550,1730)
plt.ylabel('Muon Rate (s$^{-1}$)',size='x-large')
plt.xlabel('Time (days)',size='x-large')
plt.ylim(2700,3100)
plt.xlim(np.min(t1),np.max(t1))
plt.legend()
plt.show()


np.save(f"Direction{direction_value}_b1_muon_data_{2000+input_value}",eff1)
np.save(f"Direction{direction_value}_b1_muon_data_time_{2000+input_value}",t1)












