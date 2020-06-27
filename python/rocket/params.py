import math
import numpy as np
EARTH_RADIUS=6.3781e6
EARTH_MASS=5.972e24
GRAVITATIONAL_CONSTANT=6.67408e-11
r_max=EARTH_RADIUS+ 36000e3
r_min= EARTH_RADIUS + 180e3
g=9.81 
# u is the tangential velocity v_perp
# w is the radial velocity
u_0 = 8095
w_0 = 6000 
r_0 = 6528953
theta_0 = 0.5
tau = 0.1
a = (r_max + r_min)/2
e = (r_max - r_min)/(r_max + r_min)
mu = GRAVITATIONAL_CONSTANT * EARTH_MASS
h = math.sqrt(r_min * mu * (1 + e ))

def position(theta):
    return (h**2/ mu) * (1/ ( 1 + e * np.cos(theta)))

def v_perp(theta):
    return (mu/h) * (1 + e* np.cos(theta))

def v_radial(theta):
    return (mu/h ) * e* np.sin(theta)