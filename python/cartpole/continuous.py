from cartpole import CartPoleEnv
import numpy as np
cart = CartPoleEnv()
cart.reset()

for _ in range(1000):

    # Calculate the Gradients

    # Update Thetas

    # Sample u trajectory

    # Apply u[0] to the actual system
    cart.step(10) # Apply Some force

    # Update the New State in the Learner

    # Shift the Thetas
    
    # Simulate
    cart.render()

cart.close()