import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.linalg import svd
import warnings

###############################

input_value = int(input("Enter the year: "))
#module_value = int(input("Enter the module number: "))
direction_value = int(input("Enter the direction number: "))




if input_value%4==0:
	num_year_number=366
	
else:
	num_year_number=365

############################
# Let's create a function to model and create data
def func(x, a, x0, sigma):
    return a*np.exp(-(x-x0)**2/(2*sigma**2))


###########
for D in range(16):
	module_value=D

	Gauss=np.load(f'/home/surojit/Desktop/New_data_analysis/Rejection/Rejected_data/Direction{direction_value}_gauss_mean_{2000+input_value}.npy')
	G_mean=Gauss[D]
	print(G_mean)

	#############################
	range_min=np.zeros(500)
	range_max=np.zeros(500)

	range_min[225]=2200
	range_max[225]=3200

	range_min[169]=2000
	range_max[169]=2900

	range_min[0]=180
	range_max[0]=300

	range_min[1]=250
	range_max[1]=350

	range_min[2]=170
	range_max[2]=250

	range_min[3]=250
	range_max[3]=400

	range_min[4]=400
	range_max[4]=600

	range_min[5]=200
	range_max[5]=400

	range_min[6]=180
	range_max[6]=300

	range_min[7]=250
	range_max[7]=400

	range_min[8]=150
	range_max[8]=300
	
	range_min[52]=Gauss[D]-0.1*Gauss[D]
	range_max[52]=Gauss[D]+0.1*Gauss[D]

	range_min[108]=Gauss[D]-0.1*Gauss[D]
	range_max[108]=Gauss[D]+0.1*Gauss[D]

	range_min[112]=Gauss[D]-0.1*Gauss[D]
	range_max[112]=Gauss[D]+0.1*Gauss[D]


	range_min[116]=Gauss[D]-0.1*Gauss[D]
	range_max[116]=Gauss[D]+0.1*Gauss[D]

	range_min[172]=Gauss[D]-0.1*Gauss[D]
	range_max[172]=Gauss[D]+0.1*Gauss[D]


	range1=range_min[direction_value]
	range2=range_max[direction_value]
	factor_a=0.8
	# q,a,b,i,j,k,l,m,n,p
	data_mean=[]
	data_std=[]


	t1=np.load(f'/home/surojit/Desktop/New_data_analysis/Muon_data/Raw_data_4m_bin/rejection_time_{2000+input_value}.npy')

	print(t1)


	solar_jump=[]

	solar_jump_position=[]

	X_UP=[]
	X_MEAN=[]

	############ input
	scale_value=np.zeros(500)
	scale1_value=np.zeros(500)

	scale_value[225]=5
	scale_value[169]=5
	scale_value[0]=1
	scale_value[1]=1
	scale_value[2]=1
	scale_value[3]=1
	scale_value[4]=1
	scale_value[5]=1
	scale_value[6]=1
	scale_value[7]=1
	scale_value[8]=1
	scale_value[52]=1
	scale_value[108]=1
	scale_value[112]=1
	scale_value[116]=1
	scale_value[172]=1
	

	scale1_value[225]=10
	scale1_value[169]=10
	scale1_value[0]=1
	scale1_value[1]=1
	scale1_value[2]=1
	scale1_value[3]=1
	scale1_value[4]=1
	scale1_value[5]=1
	scale1_value[6]=1
	scale1_value[7]=1
	scale1_value[8]=1
	scale1_value[52]=1
	scale1_value[108]=1
	scale1_value[112]=1
	scale1_value[116]=1
	scale1_value[172]=1

	scale=scale_value[direction_value]
	scale1=scale1_value[direction_value]

	X=[]
	T=[]
	Y=[]
	for q in range(0,num_year_number,2):
		if num_year_number==365:
			a=q*360
			b=(q+2)*360
			
			if q==364:
				a=q*360
				b=(q+1)*360
		else:
			a=q*360
			b=(q+2)*360
		
		
		
		#print(a,b)
		for i in range (D,D+1,1):

			label=f"/home/surojit/Desktop/New_data_analysis/Muon_data/Raw_data_4m_bin/Direction{direction_value}_rejection{i}_{2000+input_value}.npy"
		
			x_up=np.load(label)
			
			
			x_mean_count=[]
			
			for F in range(len(x_up)):
				if range2>x_up[F]>range1:
					x_mean_count.append(x_up[F])
			x_mean_count=np.array(x_mean_count)
			mean_count=np.mean(x_mean_count)
			mean_std=np.std(x_mean_count)
			#print(q,mean_count,mean_std)
			
				
		
			x_n=[]
			t_n=[]
			
			count_M=0
			
			for j in range(a,b,1):
		
				if x_up[j]==0:
					count_M=count_M+1
					x_n.append(1.0)
					
				else:
					x_n.append(x_up[j])
				
				t_n.append(t1[j])
		
			#print(t_n)
			#print(len(t_n))
			
			x_n=np.array(x_n)
			
			
			if count_M/len(t_n)>factor_a:
			
				print(q,mean_count,mean_std)
				data_mean.append(0.0)
				data_std.append(0.0)
				for M in range(len(t_n)):
				
					
					X_UP.append(0.0)
					X_MEAN.append(G_mean)
					X.append(0.0)
					Y.append(x_n[M])
					T.append(t_n[M])
					
				break
			
				
			
			
		
			#print(np.mean(x_n),np.std(x_n))
		
			
		
			#print(np.mean(x_hist),np.std(x_hist))
		
			#plt.plot(t_n,x_n)
			#plt.ylim(3000,3100)
			#plt.show()
			#plt.xlim(3000,3100)
		
		
			x_np=[]
			for k in range(len(x_n)):
				if 1.1*mean_count>x_n[k]>0.9*mean_count:
					x_np.append(x_n[k])
			x_np=np.array(x_np)
		
			#print(np.mean(x_np),np.std(x_np))
		
			x_npp=[]
			for l in range(len(x_n)):
				if np.mean(x_np)-4*np.std(x_np)<=x_n[l]<=np.mean(x_np)+4*np.std(x_np):
					x_npp.append(x_n[l])
			x_npp=np.array(x_npp)
		
		
		 
			#plt.hist(x_npp,bins=20)
			#plt.show()
			
			try:
			
				counts, bins, bars=plt.hist(x_npp,bins=20,histtype='step',color='b',density=True)
				plt.close()
				bins=(bins[:len(bins)-1]+bins[1:])/2
				counts=np.array(counts)
				bins=np.array(bins)
			
				shift = np.mean(x_npp)
				#scale=5
				
				bins=(bins-shift)/scale
					
				#plt.scatter(scale*bins+shift,counts)
			
				# Executing curve_fit on noisy data
				popt, pcov = curve_fit(func, bins, counts)
					
				Mean_new=popt+shift
				#print(popt)
				#print(np.mean(x_npp),'Fitted_mean=',(10*popt[1]+shift))
				#print('StD=',StD_next,popt[2])
					
			
			
			
				#ym = func(bins, popt[0], popt[1], popt[2])
				#plt.plot(10*bins+shift, ym, label=label,lw=3)
			
				#plt.show()
			
				gauss_a=np.linspace(np.min(bins),np.max(bins),1000)
				gauss_y=func(gauss_a,popt[0],popt[1],popt[2])
				#plt.plot(scale*gauss_a+shift,gauss_y, label=label,lw=3)
				#plt.show()
			
				gauss_mean=scale*popt[1]+shift
				gauss_std=scale*popt[2]
				
				gauss_mean=np.abs(gauss_mean)
				gauss_std=np.abs(gauss_std)
				
				data_mean.append(gauss_mean)
				data_std.append(gauss_std)
			
				print(q,i,gauss_mean,gauss_std)
				plt.close()
			except Exception as e:
				# Handle the exception (print an error message, continue, or take other actions)
				print(f"Error during fitting for q={q}, i={i}: {e}")
				
				print(q,mean_count,mean_std)
				data_mean.append(G_mean)
				data_std.append(0.0)
				for R in range(len(t_n)):
				
					
					X_UP.append(x_n[R])
					X_MEAN.append(x_n[R])
					X.append(0.0)
					Y.append(x_n[R])
					T.append(t_n[R])
					
				break
						
			x_new=[]
			t_new=[]
			for m in range(len(x_n)):
				if gauss_mean-4*gauss_std<=x_n[m]<=gauss_mean+4*gauss_std:
					x_new.append(x_n[m])
				else:
					x_new.append(0.0)
					t_new.append(m)
		
			x_new=np.array(x_new)
			t_new=np.array(t_new)
			
			for n in range(len(x_new)):
				X.append(x_new[n])
				T.append(t_n[n])
				Y.append(x_n[n])
			
			#plt.plot(t_n,x_n,'r',alpha=0.5)
			#plt.plot(t_n,x_new,'b')
			#plt.ylim(2800,3100)
			#plt.show()
			
			

			count_n=0
			Converge=[]
			for p in range(16):
		
				if p!=i:
					
					
					
					
					
					#print(p,i)
					#count_n=count_n+1
			
					npxlabel=f"/home/surojit/Desktop/New_data_analysis/Muon_data/Raw_data_4m_bin/Direction{direction_value}_rejection{p}_{2000+input_value}.npy"
		
					y_up=np.load(npxlabel)
					
					
					y_mean_count=[]
			
					for E in range(len(y_up)):
						if range2>y_up[E]>range1:
							y_mean_count.append(y_up[E])
					y_mean_count=np.array(y_mean_count)
					mean_county=np.mean(y_mean_count)
					mean_stdy=np.std(y_mean_count)
		
					#plt.plot(t1,y_up)
		
					y=[]
					t=[]
					COUNT_M=0
					for o in range(a,b,1):
		
						if y_up[o]==0:
							COUNT_M=COUNT_M+1
							y.append(1.0)
					
						else:
							y.append(y_up[o])
				
						t.append(t1[o])
				
					y=np.array(y)
					
					if COUNT_M/len(t)>factor_a:
						continue
					
					#print(p,i)
				
					count_n=count_n+1
					
					#plt.plot(t,x_n/y)
					#plt.xlim(np.min(t_n),np.max(t_n))
		
					#plt.xlabel('Time (days)',size='x-large')
					#plt.ylabel('Ratio',size='x-large')
					#plt.legend()
					#plt.savefig('plot5.pdf')			
					plt.show()
					
					
					
					h_n=mean_county*x_n/y
				
					y_n=[]
					count=0
					for A in range(len(h_n)-1):
						if h_n[A]-h_n[A+1]!=0:
							count=count+1
							y_n.append(h_n[A])
				
							
			
				
				
							
				
					y_n=np.array(y_n)
					
					
					
			
			
					y_np=[]
					for r in range(len(y_n)):
						if 1.1*mean_count>y_n[r]>0.9*mean_count:
							y_np.append(y_n[r])
					y_np=np.array(y_np)
		
					#print(np.mean(y_np),np.std(y_np))
		
					y_npp=[]
					for s in range(len(y_n)):
						if np.mean(y_np)-4*np.std(y_np)<=y_n[s]<=np.mean(y_np)+4*np.std(y_np):
							y_npp.append(y_n[s])
					y_npp=np.array(y_npp)
			
					try:
						counts1, bins1, bars1=plt.hist(y_npp,bins=20,histtype='step',color='b',density=True)
						plt.close()
						bins1=(bins1[:len(bins1)-1]+bins1[1:])/2
						counts1=np.array(counts1)
						bins1=np.array(bins1)
				
						shift1 = np.mean(y_npp)
						
						bins1=(bins1-shift1)/scale1
					
						#plt.scatter(scale1*bins1+shift1,counts1)
			
						# Executing curve_fit on noisy data
						popt1, pcov1 = curve_fit(func, bins1, counts1)
					
						Mean_new1=popt1+shift1
				
						gauss_a1=np.linspace(np.min(bins1),np.max(bins1),1000)
						gauss_y1=func(gauss_a1,popt1[0],popt1[1],popt1[2])
						#plt.plot(scale1*gauss_a1+shift1,gauss_y1, label=label,lw=3)
						#plt.show()
			
						gauss_mean1=scale1*popt1[1]+shift1
						gauss_std1=scale1*popt1[2]
				
						gauss_mean1=np.abs(gauss_mean1)
						gauss_std1=np.abs(gauss_std1)
			
						#print(gauss_mean1,gauss_std1)
				
						plt.close()
						
					except Exception as e:
						# Handle the exception (print an error message, continue, or take other actions)
						print(f"Error during fitting for q={q}, i={i}, p={p}: {e}")
						continue  # Continue with the next iteration of the loop

					y_new=[]

					t_new1=[]
					for t in range(len(x_n)):
						if gauss_mean1-4*gauss_std1<=h_n[t]<=gauss_mean1+4*gauss_std1:
							y_new.append(h_n[t])
						else:
							y_new.append(0.0)
				
							t_new1.append(t)
		
					y_new=np.array(y_new)
		
					t_new1=np.array(t_new1)
			
			
					#print(t_new,t_new1)
			
					t_new2=[]
					for u in range(len(t_new)):
				
						if t_new[u] in t_new1:
							#print(t_new[r])
							t_new2.append(t_new[u])
							Converge.append(t_new[u])
					
			
					
					#print(t_new,t_new1,t_new2)
				#print(len(t_new),len(t_new1),len(t_new2))
			
			
			t_factor=[]
			t_ultimate=[]
		
			for v in range(len(t_new)):
		
				count=0
				for w in range(len(Converge)):
				
					if t_new[v]==Converge[w]:
						count=count+1
					
				#print(t_new[v],count/count_n*100)
				factor=count/count_n
				t_factor.append(factor)
			t_factor=np.array(t_factor)
			for c in range(len(t_new)):
				if t_factor[c]>=0.7:
					t_ultimate.append(t_new[c])
				
			
				
			#print(t_ultimate)
			#print(len(t_ultimate))
			
			t_ultimate=np.array(t_ultimate)
			
		
				
				
			x_ultimate=[]
			x_meanfilled=[]
			for d in range(len(t_n)):
				if d in t_ultimate:
				
					x_ultimate.append(0.0)
					x_meanfilled.append(gauss_mean)
				else:
					if x_n[d]>1.0:
						x_ultimate.append(x_n[d])
						x_meanfilled.append(x_n[d])
					else:
						x_ultimate.append(x_n[d])
						x_meanfilled.append(gauss_mean)
			x_ultimate=np.array(x_ultimate)
			x_meanfilled=np.array(x_meanfilled)
			#plt.plot(t_n,x_ultimate)
			#plt.show()
			
		
			for e in range(len(t_n)):
				X_UP.append(x_ultimate[e])
				X_MEAN.append(x_meanfilled[e])		
			
			for G in range(len(t_new)):
				if t_new[G] not in t_ultimate:
					if x_n[t_new[G]]>1.0:
						solar_jump.append(t_new[G])
						solar_jump_position.append(q)
						
			
			
			
	X_UP=np.array(X_UP)
	X_MEAN=np.array(X_MEAN)


	#plt.plot(T,X_UP,'r',label='Rejection')
	#plt.legend()
	#plt.show()

	#plt.plot(T,X_MEAN,'b',label='Mean')
	#plt.legend()
	#plt.show()		

	solar_jump=np.array(solar_jump)
	solar_jump_position=np.array(solar_jump_position)

	print(solar_jump_position,solar_jump)
	print(len(solar_jump))		
			
	data_mean=np.array(data_mean)
	data_std=np.array(data_std)	

	print(len(X_UP))


	np.save(f'/home/surojit/Desktop/New_data_analysis/Rejection/Rejected_data/Direction{direction_value}_mod{module_value}_data_{2000+input_value}.npy',X_UP)
	np.save(f'/home/surojit/Desktop/New_data_analysis/Rejection/Rejected_data/Direction{direction_value}_mod{module_value}_data_time_{2000+input_value}.npy',t1)
	np.save(f'/home/surojit/Desktop/New_data_analysis/Rejection/Rejected_data/Direction{direction_value}_mod{module_value}_data_MEAN_{2000+input_value}.npy',X_MEAN)
	np.save(f'/home/surojit/Desktop/New_data_analysis/Rejection/Rejected_data/Direction{direction_value}_mod{module_value}_data_mean_{2000+input_value}.npy',data_mean)
	np.save(f'/home/surojit/Desktop/New_data_analysis/Rejection/Rejected_data/Direction{direction_value}_mod{module_value}_data_std_{2000+input_value}.npy',data_std)
		

	
	
		
		
