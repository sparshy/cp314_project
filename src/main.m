params;

p = Predictor(T,H, step, [10, 0, -10]);

for i= 1:step:T
   % Calculate Loss
   
   % Theta Update
   p.calculateGradients();
   p.updateThetas();
   
   % sample u from pi_theta
   
   % sample x_t+1 from f

   % shift theta
   
end