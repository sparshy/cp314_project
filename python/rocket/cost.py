import dynamics
from params import mu, h,e 
import numpy as np
def costTrajectory(trajectory):
    cost = 0
    for i in range(len(trajectory)):
        cost += costAnyPointInsertion(trajectory[i])
    return cost 

def costAnyPointInsertion(state):
    u = state[0]
    w = state[1]
    r = state[2]
    theta = state[3]
    return np.abs(r - h**2/(mu * (1 + e * np.cos(theta)))) + \
            np.abs(u - mu * ( 1 + e * np.cos(theta))/ h ) + \
            np.abs(w - mu * e * np.sin(theta)/ h )

def costFixedPointInsertion(control):
    cost = 0 
    for i in range(len(control)):
        cost += 1