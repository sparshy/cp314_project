params;

p = Predictor(T,H, step, [10, 0, -10]);

for i= 1:step:T
   % Calculate Loss 
   % Not doing for now, needed for plotting
   
   % Theta Update
   p.calculateGradients();
   p.updateThetas();
   
   % sample u from pi_theta
   u = sample_u_sequence(p.values, p.theta);
   control = u(1);
   
   % get x_t+1 from f (actual system)
   [t,X] = f(p.cState, control);
   p.cState = X(end,:);
   
   % shift theta
   
end