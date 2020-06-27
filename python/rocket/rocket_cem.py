import gym
import numpy as np
import random
import math
from math import * 
from envrocket import RocketEnv
from cost import costAnyPointInsertion,costTrajectory
from params import tau

pi=3.14
noise=0
from dynamics import f_x

def state_trajectory(state, control):
    trajectory=[]
    states = np.array(state)    
    t = 0 
    for i in range(len(control)):
        k1 = f_x(t, states, control[i])
        k2 = f_x(t + tau/2, states + tau*k1/2, control[i] )
        k3 = f_x(t + tau/2, states + tau*k2/2, control[i] )
        k4 = f_x(t + tau, states + k3, control[i])

        newstate = states + tau/6* ( k1 + 2*k2 + 2*k3 + k4)
        trajectory.append(newstate)
    return trajectory


def cost_calc(state_trajectory):
    cost=[]
    for i in range(len(state_trajectory)):
        x, x_dot, theta, theta_dot=state_trajectory[i]

        
        deviationFromZero = theta
        if theta > np.pi:
            deviationFromZero = np.abs(2*np.pi - theta)
        threshold = 0 if deviationFromZero < .21 else 1 
        cost.append( 100*x**2  + 500*(deviationFromZero)**2 + x_dot**2 + 15*theta_dot**2 + 1000*threshold)
    return sum(cost)


def main():
    env = RocketEnv()
    control_h= 4000
    planning_h= 120
    trajectories=100
    f_samples=10
    totalreward=0
    n_elite=trajectories*0.5
    next_state=env.reset()

    mean=np.full((planning_h,2), 0) # Since we have two control variables.
    env.initializePlot()
    for time in range(control_h):
        print("Iteration ------------------", time)       
        
        #Reset Grads
        grads=np.zeros((planning_h,2)) # 2 control variables
        cumulative_cost=0
        u, w, r, theta = next_state
        scaling = 1
        gamma=1
        

        control_elite=np.zeros((trajectories, planning_h,2)) # 2 controls
        cost_elite=np.zeros(trajectories)

        for i in range(trajectories):
            control= np.array([np.random.normal(m,5) for m in mean])
            control=np.clip(scaling*control, -25, 25)
            if i%10 == 0:
                noise=np.array([np.array([np.random.normal(0,5), np.random.normal(0,5)]) for m in mean])       
            control=control+noise
            trajectory=state_trajectory(next_state,control)
            cost=costTrajectory(trajectory)
            cost_elite[i] = cost
            control_elite[i] = control

        elite_inds = cost_elite.argsort()[0:10]

        for index in elite_inds:
            grads+=control_elite[index,:]*cost_elite[index]
        grad_mean=grads/sum(cost_elite[elite_inds])

        mean=(1-gamma)*mean+gamma*grad_mean
        u= mean[0].copy()
                
        control=np.clip(scaling*u, -25, 25) # +np.random.normal(0,5)

        print("control", control)

        ## TODO Render the Simulation
        env.render()

        next_state = env.step(control)

        #shift means
        mean=np.append(mean[1:], mean[-1][np.newaxis], axis =0) 

        print("next_state",next_state, "cost", costAnyPointInsertion(next_state))
    env.close()
if __name__=="__main__": 
    main()