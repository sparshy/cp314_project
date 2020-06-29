import numpy as np
from params import u_0,w_0,r_0,theta_0, EARTH_RADIUS, mu,h,e, tau
from dynamics import f_x
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from cost import costAnyPointInsertion
class RocketEnv():
    def __init__(self):
        self.rocketTrajctoryR = []
        self.rocketTrajctoryTheta = []
        self.costs = []
        pass

    def reset(self):
        self.state = (u_0,w_0,r_0,theta_0)
        return np.array(self.state)

    def step(self, control):
        t = 0 
        states = self.state
        k1 = f_x(t, states, control)
        k2 = f_x(t + tau/2, states + tau*k1/2, control )
        k3 = f_x(t + tau/2, states + tau*k2/2, control )
        k4 = f_x(t + tau, states + k3, control)

        self.state = states + tau/6* ( k1 + 2*k2 + 2*k3 + k4)
        self.rocketTrajctoryR.append(self.state[2])
        self.rocketTrajctoryTheta.append(self.state[3])
        self.costs.append(costAnyPointInsertion(self.state))
        return self.state
    
    def initializePlot(self):
        """Plot the trajectory of the spacecraft along with the
        orbit and the earth in polar coordinates

        Args:
            x (np.array): The r values
            y (np.array): Corresponding theta values
        """
        self.theta = []
        self.trajectory = []
        self.earth = []
        for t in np.arange(0,2*np.pi,0.01):
            self.theta.append(t)
            self.trajectory.append(h**2/(mu * (1 + e * np.cos(t))) )
            self.earth.append(EARTH_RADIUS)
        fig, self.ax = plt.subplots(1, 1, subplot_kw=dict(polar=True))
        # Plots the Orbit
        self.ax.plot(self.theta, self.trajectory,'r')
        # Plots the Earth
        self.ax.plot(self.theta, self.earth,'b')
        if True:
            self.ax.set_xlim(0, np.pi/2)
            self.ax.set_ylim(0,10e6)
        self.ax.set_title("Polar plot for the trajectory")
    def render(self):
        plt.plot(self.rocketTrajctoryTheta, self.rocketTrajctoryR,'g')
        plt.draw()
        plt.pause(0.0001)

    def close(self):
        fig2, ax1 = plt.subplots()
        ax1.plot(self.costs)
        plt.show()
        np.savez('launcher',
         r=self.rocketTrajctoryR, theta=self.rocketTrajctoryTheta, theta1=self.theta, 
            earth = self.earth , orbit = self.trajectory, costs = self.costs)