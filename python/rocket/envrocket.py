import numpy as np
from params import u_0,w_0,r_0,theta_0
from dynamics import f_x
class RocketEnv():
    def __init__(self):
        pass

    def reset(self):
        self.state = (u_0,w_0,r_0,theta_0)
        return np.array(self.state)

    def step(self, control):
        t = 0 
        tau = 0.02
        states = self.state
        k1 = f_x(t, states, control)
        k2 = f_x(t + tau/2, states + tau*k1/2, control )
        k3 = f_x(t + tau/2, states + tau*k2/2, control )
        k4 = f_x(t + tau, states + k3, control)

        self.state = states + tau/6* ( k1 + 2*k2 + 2*k3 + k4)
        return self.state