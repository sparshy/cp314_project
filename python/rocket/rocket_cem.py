import gym
import numpy as np
import random
import math
from math import * 
from envrocket import RocketEnv

masscart = 1
gravity = 9.8
length = 0.65
masspole =0.1
polemass_length =masspole *length
total_mass = masspole + masscart
force_mag = 10.0
tau = 0.02
pi=3.14
noise=0

def state_trajectory(state, control):
    trajectory=[]
    x, x_dot, theta, theta_dot = state    

    for i in range(len(control)):
        noise = np.random.normal(0,1) # Stochasticity 
        force = control[i]
        costheta = math.cos(theta)
        sintheta = math.sin(theta)

        temp = (force + polemass_length * theta_dot ** 2 * sintheta) / total_mass
        thetaacc = (gravity * sintheta - costheta * temp) / (length * (4.0 / 3.0 - masspole * costheta ** 2 / total_mass))
        xacc = temp - polemass_length * thetaacc * costheta / total_mass

        x = x + tau * x_dot
        x_dot = x_dot + tau * xacc
        theta = theta + tau * theta_dot
        theta_dot = theta_dot + tau * thetaacc
        
        # Clip thetas 
        theta = theta%(2*np.pi)
        state=(x,x_dot,theta,theta_dot) #Also theta_dot and x_dot are becoming too high
        trajectory.append(np.array(state).flatten())
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
    control_h= 500
    planning_h= 120
    trajectories=100
    f_samples=10
    totalreward=0
    n_elite=trajectories*0.5
    next_state=env.reset()

    mean=np.full((planning_h,2), 0) # Since we have two control variables.

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
                noise=np.array([np.random.normal(0,5) for m in mean])       
            control=control+noise
            trajectory=state_trajectory(next_state,control)
            cost=cost_calc(trajectory)
            cost_elite[i] = cost
            control_elite[i] = control

        elite_inds = cost_elite.argsort()[0:10]

        for index in elite_inds:
            grads+=control_elite[index,:]*cost_elite[index]
        grad_mean=grads/sum(cost_elite[elite_inds])

        mean=(1-gamma)*mean+gamma*grad_mean
        u= mean[0].copy()
                
        control=np.clip(scaling*u, -25, 25)+np.random.normal(0,5)

        print("control", control.item())

        env.render()

        next_state,reward,done,info = env.step(control.item(),0)

        #shift means
        mean=np.append(mean[1:],10)

        print("next_state",next_state)

        if done:
            pass
    print("Total reward", totalreward)
    env.close()

if __name__=="__main__": 
    main()