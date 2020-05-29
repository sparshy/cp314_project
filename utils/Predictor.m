classdef Predictor < handle
    properties
        T               % 10s
        H               % 50 steps
        step            % 0.02 sec
        theta           % 3x50 matrix
        M               % Number of control inputs
        N               % Number of states
        cState          % Current State the system starts from
        inputSize       % The number of available control inputs 3 
        values          % The values of available control [+10, 0, -10]
        gradients       % a 3 x H vector to store the gradients
    end
    methods
        % Constructor
        function obj = Predictor(T,H,step, values)
            % Constructor
            [~, inputSize] = size(values);
            obj.values = values;
            obj.T = T;
            obj.H = H;
            obj.step = step;
            obj.inputSize = inputSize;
            obj.theta = ones(obj.inputSize,H) * 1/3;
            obj.M = 1; 
            obj.N = 4; 
            obj.cState = [3,0,pi,0];
        end
        
        % Propagate the System Dynamics for H steps
        function [t,X] = propagateHSteps(obj,u)
            [t,X] = f_cap(obj.cState ,u);
        end
        
        % Calculates the Gradients
        function calculateGradients(obj)
            obj.gradients = zeros(obj.inputSize,obj.H); % 3x50
            % Calculating expected values of mean
            noIterationForSampleMean = 100;  % Number of trajectories
            for i = 1:noIterationForSampleMean
                u = sample_u_sequence(obj.values, obj.theta);
                if i%10 == 0
                    eta = normrnd(0,5,1,50);
                end
                u_with_noise = u + eta;
                loss = obj.calculateLoss(u_with_noise);
                for h=1:50
                    obj.gradients(:,h) = obj.gradients(:,h) + ( loss * ([+10,0,-10]' == u(h)) ./ obj.theta(:,h));
                end
            end
            obj.gradients = obj.gradients/noIterationForSampleMean;
        end
        
        % Calculate the Loss associated with a trajectory
        function loss = calculateLoss(obj,u)
            loss = 0;
            [t,X] = obj.propagateHSteps(u); % t, 51 x 4 matrix 
            for i=1:obj.H
                loss = loss + obj.stepCost(X(i,:));
            end
            loss = loss + obj.stepCost(X(obj.H+1,:)) ;
        end
        
        % Cost of each step
        function cost = stepCost(obj,x)
            cost = 10 * x(1)^2  + 500 * (x(3) -pi)^2 + x(2)^2 + 15 * x(4)^2 + 1000 * ( abs(x(3) -pi ) >= 0.21);
        end
        
        % Update theta values
        function updateThetas(obj)
            for h=1:50
                val = obj.theta(:,h) .* (exp(- 1e-5 * obj.gradients(:,h)) );
                obj.theta(:,h) = val/sum(val);
            end
        end
        
    end
end