clc;
clear;
params;
p = PredictorContinuous(T,H, step);
for i= 0:step:T
   % Calculate Loss 
   % Not doing for now, needed for plotting
   
   % Theta Update
   p.calculateGradients();
   p.updateThetas();
   
   % sample u from pi_theta
   u = p.mean;
   control = u(1);
   
   % get x_t+1 from f (actual system)
   [t,X] = f(p.cState, control);
   p.cState = X(end,:);
   p.cState
   % shift theta
   p.mean = [ p.mean(:,2:end), 10];
   
   % Do simulation
   draw_cartpole(p.cState,0.336);
   fprintf('time: %f seconds ; control %f N\n', i, control );
end