import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.colors as mcolors
import numpy as np
###################################
input_value=int(input("Enter the year: "))
direction_value = int(input("Enter the direction number: "))
############################################################
#########################################################
num_window=np.load(f"Direction{direction_value}_yearly_Window_raw_{2000+input_value}.npy")
t=np.load(f"Direction{direction_value}_yearly_module0_block_data_time_{2000+input_value}.npy")	

print(num_window)	
#################################

#print(num_window)

updated_window=[]
updated_window.append(num_window[0])
for u in range(len(num_window)-1):
	updated_window.append(num_window[u+1]-num_window[u])
	
updated_window=np.array(updated_window)

#print(updated_window,updated_window[0],updated_window[1])
num_updated_window=updated_window


###############################
stitch_reference_modules=[]
for scale in range(len(updated_window)-1):

	num_data=[]
	for w in range(len(num_window)):
		npr=f"Direction{direction_value}_yearly_num_div_value{w}_{2000+input_value}.npy"
		x=np.load(npr)
		num_data.append(x)
			
	
	num_data=np.array(num_data)
	
	
	nummm1=[]
	for u in range(scale,scale+2,1):
		nummm1.append(num_data[u])
	num_data=nummm1
	
	#print(num_data)
	
	
	num_ref=[]
	num_index=[]
	
	exclude_module=np.load(f"YEARLY_REF_module_division{scale}_{2000+input_value}.npy")
	
	print("################",exclude_module,"###############")
	for i in range(16):
		#print(num_data[0][i],num_data[1][i])
		
		if i not in exclude_module :
			num_ref.append((num_data[0][i]+num_data[1][i])/2.0)
		
			num_index.append(i)
	
	num_ref=np.array(num_ref)
	#print(num_ref)
	num_index=np.array(num_index)
	
	sorted_data = sorted(zip(num_ref, num_index))
	sorted_x, sorted_t = zip(*sorted_data)
	sorted_x=np.array(sorted_x)
	sorted_t=np.array(sorted_t)
	
	nxx=f"Direction{direction_value}_YEARLY_STITCH_REFERENCE_{scale}_{2000+input_value}"
	np.save(nxx,sorted_t[-1])
	
	#print('##############################')
	print(scale,'xxxxxx',sorted_t[-1],'xxxxxxx',sorted_x[-1])
	#print('################################')
	
	stitch_reference_modules.append(sorted_t[-1])
	
	
	
		
	A=np.zeros((16,len(num_data)))
	for i in range(16):
		for j in range(1):
		
			for k in range(len(num_data)):
				A[i][j+k]=num_data[k][i]
	data=A
	
	#print(data)

	###############################
	a=np.arange(len(data[0]))
	a1=[]

	for l in range(len(a)):
	    a1.append(f"{l+1:02d}")

	b=np.arange(len(data))+0.5
	b1=[] 
	for l in range(len(b)):
	    b1.append(f"{15-l:02d}")

	############################################

	up_win=[]
	
	for v in range(scale,scale+2,1):
		#print(v)
		up_win.append(num_updated_window[v])
	up_win=np.array(up_win)
	
	#print(updated_window)
	#print(up_win)
	
	updated_window=up_win

	M=[]
	M.append(updated_window[0]/2)
	M.append(updated_window[0]+updated_window[1]/2)
	M=np.array(M)

	N=[]
	N.append(scale)
	N.append(scale+1)
	N=np.array(N)
	
	#print(M,N)

	# Create a figure and axis
	fig, ax = plt.subplots()

	# Define the dimensions of the matrix
	rows, cols = 16, len(updated_window)

	# Define the size of each rectangle
	rect_widths =np.array(updated_window)  # Width of the first and second columns
	rect_height = 1.0

	#print(len(rect_widths))

	# Define data values for each box (ranging from 0.5 to 1.0)
	#data = [[0.7, 0.9],
	#        [0.6, 0.8],
	#        [0.8, 0.75]]

	# Create a colormap
	colormap = plt.get_cmap('jet_r')

	vmin=0.9
	vmax=1.0  # Define your custom range here


	#fig, ax = plt.subplots(figsize=(10,2), dpi=100)
	plt.minorticks_on()

	ax.tick_params('both', which='major', length=4, width=2, direction='out')
	# Loop through the rows and columns to create rectangles with colors
	for i in range(rows):
		for j in range(cols):
			x = sum(rect_widths[:j])  # Calculate the x-coordinate based on column width
			y = i * rect_height
			value = data[15-i][j]  # Get the data value for coloring
			color = colormap((value - vmin) / (vmax - vmin))  # Map the data value to a color within the custom range
			rect = patches.Rectangle((x, y), rect_widths[j], rect_height, linewidth=1, edgecolor='k', facecolor=color)
			ax.add_patch(rect)
		
		# Add text label with the data value at the center of each rectangle
	       # ax.text(x + rect_widths[j] / 2, y + rect_height / 2, f'{value:.3f}', color='black',
	       #         ha='center', va='center', fontsize=12)

	# Set axis limits
	ax.set_xlim(0, sum(rect_widths))
	ax.set_ylim(0, rows * rect_height)

	#plt.xlabel('Division',size='x-large')
	plt.xlabel('Division',size='x-large')
	plt.ylabel('Module',size='x-large')
	plt.xticks(M,N)
	plt.yticks(b, b1)
	# Set aspect ratio to equal to make the rectangles square
	#ax.set_aspect('equal')

	# Remove axis labels and ticks
	#ax.xaxis('off')

	# Create a colorbar
	sm = plt.cm.ScalarMappable(cmap=colormap, norm=plt.Normalize(vmin=vmin, vmax=vmax))
	sm.set_array([])  # An empty array is used since we're not mapping data directly
	cbar = plt.colorbar(sm, ax=ax)
	cbar.set_label('Color Bar',size='x-large')

	# Display the plot
	#plt.show()
	plt.close('all')






