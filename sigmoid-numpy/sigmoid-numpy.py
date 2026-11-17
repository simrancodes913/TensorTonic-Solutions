import numpy as np

def sigmoid(x: list | float) -> np.ndarray | float: 
    x=np.asarray(x,dtype=float)
    x=1/(1+np.exp(-1*x))
    if(x.ndim==0):
        return float(x)
    else:
        return x
    pass