import numpy as np
from params import u_0,w_0,r_0,theta_0

class RocketEnv():
    def __init__(self):
        pass

    def reset(self):
        self.state = (u_0,w_0,r_0,theta_0)
        return np.array(self.state)