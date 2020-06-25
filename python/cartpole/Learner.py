import numpy as np
class PredictorContinuous():
    def __init__(self):
        self.T = 10         # 10 sec 
        self.H = 50         # 50 steps 
        self.step = 0.02    # 0.02 seconds
        self.mean = np.zeros((1,self.H))
        self.M = 1
        self.N = 4
        self.cState = (0,0,np.pi, 0)    # Initial state
        self.gradients = np.zeros((1,50))
        self.noOfTrajectories = 100

    def propagateSystemDyanmics(self):
        pass

#       Propagate the System Dynamics for H steps
#         function [t,X] = propagateHSteps(obj,u)
#             [t,X] = f_cap(obj.cState ,u);
#         end
    def calculateGradients(self):
        scaling = 1 # Ask Soumya why this is needed
        # First Try some trajectories
        for i in range(self.noOfTrajectories):
            control= np.array([np.random.normal(m,5) for m in mean])
            control=np.clip(scaling*control, -25, 25)
            if i%10 == 0:
                noise=np.array([np.random.normal(0,5) for m in mean])
            control=control+noise
            trajectory=state_trajectory(next_state,control)
            cost=cost_calc(trajectory)
            cost_elite[i] = cost
            control_elite[i] = control
            #print("after_update:  ", grad)

        # Use only Elite Trajcectories.


#         % Calculates the Gradients
#         function calculateGradients(obj)
#             obj.gradients = zeros(1,obj.H);% 1x50
#             % Calculating expected values of mean
#             noIterationForSampleMean = 100;% Number of trajectories
#             for i = 1:noIterationForSampleMean
#                 u = normrnd(obj.mean,2);
#                 for m=1:50
#                     if u(m) > 25
#                         u(m) = 25;
#                     end
#                     if u(m) < -25
#                         u(m) = -25;
#                     end
#                 end
#                 if i%10 == 0
#                     eta = normrnd(0,5,1,50);
#                 end
#                 u_with_noise = u + eta;
#                 loss = obj.calculateLoss(u_with_noise);
#                 for h=1:50
#                     obj.gradients(h) = obj.gradients(h) + ( loss * u(h) );
#                 end
#             end
#             obj.gradients = obj.gradients/noIterationForSampleMean;
#         end
    def calculateLoss(self):
        loss = 0
        (t,X) = self.propagateSystemDyanmics(u)
        fo
        
#         % Calculate the Loss associated with a trajectory
#         function loss = calculateLoss(obj,u)
#             loss = 0;
#             [~,X] = obj.propagateHSteps(u); % t, 51 x 4 matrix 
#             for i=1:obj.H
#                 loss = loss + obj.stepCost(X(i,:));
#             end
#             loss = loss + obj.stepCost(X(obj.H+1,:));
#         end
        
#         % Cost of each step
#         function cost = stepCost(obj,x)
#             angle = x(3);
#             if angle < 0
#                 angle = -angle;
#             end
#             cost = 10 * x(1)^2  + 500 * (angle -pi)^2 + x(2)^2 + 15 * x(4)^2 + 100*cos(x(3));%+ 1000 * ( abs(x(3) -pi ) >= 0.21);
#         end
        
#         % Update theta values
#         function updateThetas(obj)
#             for h=1:50
#                 gamma = 1e-5;
#                 obj.mean(h) = (1-gamma)*obj.mean(h) + gamma*obj.gradients(h);
#                 if obj.mean(h) > 25
#                     obj.mean(h) = 25;
#                 end
#                 if obj.mean(h) < -25
#                     obj.mean(h) = -25;
#                 end
#             end
#         end
        
#     end
# end