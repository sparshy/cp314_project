params;

p = Predictor(T,H, step, [100, 0, -100]);

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
   p.theta = [ p.theta(:,2:end), [1/3,1/3,1/3]'];
   
   % Do simulation
   draw_cartpole(p.cState,0.336);
   fprintf('time: %f seconds ; control %f N\n', i, control );
end