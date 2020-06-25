import numpy as np

def Energy(cState, dState, cart):
    """
    Input Current State, Desired State
    Output Force
    """
    x, x_dot, theta, theta_dot = cart.state
    costheta = np.cos(theta)
    sintheta = np.sin(theta)
    w = np.sqrt(9.81/cart.length)
    c0 = 0.9
    zeta = 1.2
    omega = w/c0
    f1 = omega**2
    f2 = zeta * 2 * omega
    u = (cart.masscart + cart.masspole * sintheta**2) * \
        (f1* (rd - x)  - f2 * x_dot) + \
        cart.masspole * 9.81 * costheta * sintheta + \
        cart.masspole * cart.lenght * theta_dot**2 * sintheta

 
def LQR():
    pass