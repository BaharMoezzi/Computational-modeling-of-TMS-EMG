#########################################################################
##                                                                     ##
## Simulation of EMG recordings following TMS                          ##
##                                                                     ##
## Moezzi, B., Schaworonkow, N., Plogmacher, L., Goldsworthy, M. R.,   ##
## Hordacre, B., McDonnell, M. D., Iannella, N., Ridding, M. C., and   ## 
## Triesch, J. (2018) “Simulation of electromyographic recordings      ## 
## following transcranial magnetic stimulation,” Journal of            ##
## Neurophysiology, In Press.                                          ##
##                                                                     ##
#########################################################################

import os, sys
from neuron import h, hclass, gui
import numpy as np                      # for numerics and array handling
from Parameters import *                # simulation parameters
import random as rd

np.random.seed()                        # initiate random generator
	
h.load_file("nrngui.hoc")               # initialize neuron

h.dt = 0.025                            # [ms] simulation time step

### L5 data
f = open('MembraneV.txt','r') 

### Preparing the data file for analysis
L5Membrane_Ini = []
for line in f:
	L5Membrane_Ini.append(line.split())

f.close()

L5Membrane = []
for Ini in xrange(len(L5Membrane_Ini)):
    Ink = 0
    L5Membrane_sec = []
    ### Change for faster results 
    for Inj in xrange(14000,18500):     # (1,len(L5Membrane_Ini[1]))                    
        Ink = Ink + 1
        L5Membrane_sec.append(L5Membrane_Ini[Ini][Inj])
    L5Membrane.append(L5Membrane_sec)

### Finding the time of spiking at the distal part of L5 cells
MyTime = len(L5Membrane[1])
for mR in xrange(mainRepi,mainRepf):
  TSpike = []
  for j in xrange(len(L5Membrane)):
  	timeSpike = np.zeros(int(round(0.1*MyTime)))
        index = 0
        spikes = np.zeros(MyTime-1)
        for i in xrange(1,MyTime-1):
		if float(L5Membrane[j][i]) > float(L5_th) and L5Membrane[j][i-1]  < L5Membrane[j][i] and L5Membrane[j][i] > L5Membrane[j][i+1]:
			print L5Membrane[j][i]
			spikes[i] = 1
 			timeSpike[index] = i*h.dt
			index = index + 1
	TSpike.append(timeSpike) 

  MEP = []
  Rep = len(TSpike) 
 
  ### Computing motoneuron threshold values
  Vth = []
  for i in xrange(MT):
	Vth.append(U1+float((UM-U1)*i)/float(MT)) 

  ### Randomly choosing 30 out of 120 motoneurons  
  MN_index = np.random.permutation(MT)
  MN_Index = MN_index[:M]
  MN_Index.sort()     

  Vm = []
  MNTime = []
  L5TSpike_eachMN = []
  HR = []
 
  
  MNTimeall= []    
  HR = [] 

  for forank in xrange(0,M): 

     ### Randomly choosing 70 out of 150 L5 cells
     spike_index = np.random.permutation(Rep)
     spike_Index = spike_index[:N]
     myL5TSpike = []
     for myi in xrange(0,N):
	myL5TSpike.append(TSpike[spike_Index[myi]])
     L5TSpike_eachMN.append(myL5TSpike)

     ### Computing synaptic current to motoneurons
     syn_curr = []
     Main_spikeTime = []
     Main_spikeTrain = []
     for i in xrange(N):
	cur = np.zeros(MyTime-2)
	My_spikeTrain = np.zeros(MyTime-2)
	main_st = []
        for j in xrange(len(TSpike[spike_Index[i]])):
		if TSpike[spike_Index[i]][j] != 0:
			main_st.append(TSpike[spike_Index[i]][j])
                Main_spikeTime.append(main_st)
	for t in xrange(1,MyTime-2):
 		for j in xrange(len(Main_spikeTime[i])):
			if t*h.dt < Main_spikeTime[i][j]+float(h.dt)/float(2) and t*h.dt > Main_spikeTime[i][j]-float(h.dt)/float(2):
 				My_spikeTrain[t] = 1
				cur[t] = float(1)/float(h.dt)
 	Main_spikeTrain.append(My_spikeTrain)
	syn_curr.append(float(K[i]) * cur)
     Ie = np.sum(syn_curr,0)/float(M) 

     ### Motoneuron
     V = np.zeros(MyTime-2)
     mnT = 0
     mymnT = []

     MNTimeall.append([])  
     HR.append([])
     myindex = 0
     ### Integrate and Fire model of motoneurons
     for i in xrange(1,MyTime-2):
	Total = 0
        for s in xrange(0,i-mnT):
            Total = Total + h.dt*np.exp(-float(h.dt*s)/float(taum))*Ie[i-s]
        V[i] = -nu0*np.exp(-float(h.dt*(i-mnT))/float(RRP)) + ((float(Rm)/float(taum))*(1-np.exp(-float(h.dt*(i-mnT))/float(REC)))*Total)
	if V[i] >= Vth[MN_Index[forank]]:
                mnT = i + 1
                MNTime.append(mnT)
 
     MNTimeall[forank].append(MNTime)  

     ### Hermite-Rodriguez functions:
     allhr = [np.zeros(MyTime-2)]
     for j in xrange(len(MNTime)): 
       hr = np.zeros(MyTime-2) 
       for t in xrange(1,MyTime-2): 
           hr[t] = A[MN_Index[forank]]*(-t*h.dt+MNTime[j]*h.dt+TD[forank])*np.exp(-pow((-t*h.dt+MNTime[j]*h.dt+TD[forank])/lam,2))/lam	       	
       allhr.append(hr)

     sumallhr = np.sum(allhr,0)

     HR[forank].append(sumallhr)
  
  ### Computation of EMG trace as a summation of Hermite-Rodriguez functions
  EMGSignal = np.sum(HR,0)

  ### Saving data 
  sF = '_Data_'
  sN = str(mR)
        
  s = 'Results/'
  s += 'MN'
  s += sF
  s += sN
  s += '.txt'
  np.savetxt(s, MNTimeall, fmt="%s")

  s = 'Results/'
  s += 'EMG'
  s += sF
  s += sN
  s += '.txt'
  np.savetxt(s, EMGSignal, fmt="%s")
