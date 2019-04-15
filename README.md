# Introduction
This repository provides the code for our simulation of EMG recordings following TMS. 

The details of how TMS generates responses measured with EMG are not completely understood. We developed a biophysically detailed computational model to study the potential mechanisms underlying the generation of EMG signals following TMS. Our model successfully reproduces several characteristics of the experimental data and should be considered as a viable tool for explaining and analyzing EMG signals following TMS. For more details see our published article: "[Simulation of electromyographic recordings following transcranial magnetic stimulation](https://doi.org/10.1152/jn.00626.2017)".

# Dependencies
python 2.7.13 

numpy 1.12.1 

mpi4py 2.0.0

openmpi gnu 2.1.0-gcc4.8.5 

neuron 7.3

gnu 6.3.0

# How to run?
The input to main.py is the membrane potential of 150 cortical layer 5 neurons collected close to the spinal motoneurons in a text format. The Run.sub file is used to run the code on a high performance computing (HPC) Clusters. The outputs are EMG signals and monotoeuron spike times.
