# Introduction
This repository provides the code for our simulation of electromyographic recordings following transcranial magnetic stimulation. 

the details of how TMS generates responses measured with EMG are not completely understood. We developed a\ biophysically detailed computational model to study the potential mechanisms underlying the generation of EMG signals following TMS. "EMG signals are modeled as the sum of motor unit action potentials. EMG recordings from the first dorsal interosseous muscle were performed in four subjects and compared with simulated EMG signals. Our model successfully reproduces several characteristics of the experimental data. The simulated EMG signals match experimental EMG recordings in shape and size, and change with stimulus intensity and contraction level as in experimental recordings. They exhibit cortical silent periods that are close to the biological values and reveal an interesting dependence on inhibitory synaptic transmission properties. Our model predicts several characteristics of the firing patterns of neurons along the entire pathway from cortical layer 2/3 cells down to spinal motoneurons and should be considered as a viable tool for explaining and analyzing EMG signals following TMS." For more details see our published article: "[Simulation of electromyographic recordings following transcranial magnetic stimulation](https://doi.org/10.1152/jn.00626.2017)".

# Dependencies
python 2.7.13 

numpy 1.12.1 

mpi4py 2.0.0

openmpi gnu 2.1.0-gcc4.8.5 

neuron 7.3

gnu 6.3.0

# How to run?
The input to main.py is the membrane potential of 150 cortical layer 5 neurons collected close to the spinal motoneurons in a text format. The Run.sub file is used to run the code on a high performance computing (HPC) Clusters. The outputs are EMG signals and monotoeuron spike times.
