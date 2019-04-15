##########################################
##                                      ##
## Parameters used in Main.py           ##
##                                      ##
##########################################

import numpy as np         # for numerics and array handling

### Loop parameters to produce multiple EMG traces
mainRepi  = 1
mainRepf  = 10

### Layer 5 Cells


L5_th     = 0               # L5 cells threshold                    
N         = 70              # N                    
							        

### Motoneuron (LIF)
K         = np.ones(N)
Rm        = 36              # Input resistance,
nu0       = 22              # Scale factor for refractory function 
RRP       = 2               # Refractory time constant
taum      = 4               # Passive membrane time constant
REC       = 100             # Recovery time constant
MT        = 120 
M         = 30           
U1        = 5            
UM        = 15            
lam       = 2               # Lambda
MNr       = 100             # A vary over MNr fold
A         = np.exp(xrange(MT)*np.log(MNr)/MT)
TD        = 10 * np.ones(MT) 
