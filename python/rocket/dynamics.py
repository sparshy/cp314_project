import numpy as np

from params import g, mu
# The state vector is [u, w, r, theta]

def f_x(t,x,u):

    u_ = x[0]
    w = x[1]
    r = x[2]
    theta = x[3]
    a_u = u[0]
    a_w = u[1]

    return np.array([
        a_u - u_ * w / r,
        a_w + u_*u_/r - mu/(r*r),
        w,
        u_/r
    ])
