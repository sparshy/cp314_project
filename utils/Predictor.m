classdef Predictor < handle
    properties
        T
        H
        step
        theta
        M               % Number of control inputs
        N               % Number of states
        cState          % Current State the system starts from
        inputSize       % The number of available control inputs
        values          % The values of available control
        gradients       % a inputSize x H vector to store the gradients
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
            obj.cState = [0,0,0,0];
        end
        
        % Propagate the System Dynamics for H steps
        function [t,X] = propagateHSteps(obj,u)
            [t,X] = f_cap(obj.cState ,u);
        end
        
        % Calculates the Gradients
        function calculateGradients(obj)
            obj.gradients = zeros(obj.inputSize,obj.H);
            % Calculating expected values of mean
            noIterationForSampleMean = 10;
            for i = 1:noIterationForSampleMean
                u = sample_u_sequence(obj.values, obj.theta);
                loss = obj.calculateLoss(u);
                for h=1:50
                    obj.gradients(:,h) = obj.gradients(:,h) + ( loss * ([+10,0,-10]' == u(h)) ./ obj.theta(:,h));
                end
            end
            obj.gradients = obj.gradients/noIterationForSampleMean;
        end
        
        % Calculate the Loss associated with a trajectory
        function loss = calculateLoss(obj,u)
            loss = 0;
            [t,X] = obj.propagateHSteps(u);
            for i=1:obj.H
                loss = loss + obj.stepCost(X(i,:));
            end
            loss = loss + obj.stepCost(X(obj.H+1,:)) ;
        end
        
        % Cost of each step
        function cost = stepCost(obj,x)
            cost = 10 * x(1)^2  + 500 * (x(3) - pi)^2 + x(2)^2 + 15 * x(4)^2 + 1000 * ( (x(3) - pi) >= 0.21);
        end
        
        % Update theta values
        function updateThetas(obj)
            for h=1:50
                val = obj.theta(:,h) .* (exp(- 0.001 * obj.gradients(:,h)) );
                obj.theta(:,h) = val/sum(val);
            end
        end
        
    end
end