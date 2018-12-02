import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
import json
print( os.getcwd())

#timefile = pd.read_csv("timestamp_walk.csv", header=None)
#xfile = pd.read_csv("x_walk.csv", header=None)
#yfile = pd.read_csv("y_walk.csv", header=None)
#zfile = pd.read_csv("z_walk.csv", header=None)
timefile = pd.read_csv("stair_time_walkandstairstest2.tsv.csv", header=None)
xfile = pd.read_csv("stair_x_walkandstairstest2.tsv.csv", header=None)
yfile = pd.read_csv("stair_y_walkandstairstest2.tsv.csv", header=None)
zfile = pd.read_csv("stair_z_walkandstairstest2.tsv.csv", header=None)
#lines = infile.read().split('\t')
#del lines[-1]
#print(lines)
#accvecs = []
#timevec =[]
#i=0
#for line in lines:
#    data  = json.loads(line)
##    print(data)
##    print (i)
#    timevec.append(data["accelerometer"]["timestamp"])
#    accvecs.append(data["accelerometer"]["value"][0])
    
##print(accvecs[:])

# Fixing random state for reproducibility
np.random.seed(19680801)
k=0
i=0
#for i in range(len(timefile)): 
while (699+k < len(timefile)):
	#print(len(timefile))
	#print(timefile.loc[1:2])
	timevec = timefile.loc[k:699+k]
	#print(timevec)
	accvecs = xfile.loc[k:699+k]
	#print(accvecs)
	accvecs_y = yfile.loc[k:699+k]
	#print(accvecs_y)
	accvecs_z = zfile.loc[k:699+k]	
	#print(timevec.loc[len(timevec)-1])
	elapsed = 15
	#elapsed = (timevec.loc[len(timevec)-1] - timevec.loc[0])/1000000000
	#print(timevec.loc[len(timevec)-1])
	#print(timevec.loc[0])
	#print(elapsed)
	dt = (elapsed/len(accvecs))
	#print(dt)
	t = np.arange(0.0, elapsed, dt)


	x = accvecs  # the signal
	y = accvecs_y
	z = accvecs_z

	if len(x) > len(t):
		del x[-1]
	if len(t) > len(x):
		t = t[:1]
	if len(y) > len(t): 
		del y[-1]
	if len(t) > len(y): 
		t = t[:1]
	if len(z) > len(t): 
		del z[-1]
	if len(t) > len(z): 
		t = t[:1]

	NFFT = 512  # the length of the windowing segments
	Fs = int(1.0 / dt)  # the sampling frequency
	total_coord = np.concatenate((x,y,z), axis=0)
	total_coord = pd.DataFrame(total_coord)
	total_coord1 = total_coord[0]
	fig, ax1 = plt.subplots(nrows=1)
#print(t)
#rint(x)
	t2 = np.arange(0.0, elapsed*3, dt)
	ax1.plot(t2, total_coord1)
	#ax1.plot(t, x)
	#Pxx, freqs, bins, im = ax2.specgram(total_coord1, NFFT=NFFT, Fs=Fs, noverlap=400)
	k+=699
	#np.save('stairdown8'+str(i)+".npy", Pxx)
	i+=1
# The `specgram` method returns 4 objects. They are:
# - Pxx: the periodogram
# - freqs: the frequency vector
# - bins: the centers of the time bins
# - im: the matplotlib.image.AxesImage instance representing the data in the plot
	plt.savefig('test_data2'+str(i)+'.png')
	
