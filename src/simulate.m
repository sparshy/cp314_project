m = 1;
M = 10;
g = -9.8;
L = 1;
d = 17;
u = 0;

t = [0:0.1:100];
y0 = [ 3, 0, pi/2, 0.5]';
%u = sample_u_sequence([10,0,-10], ones(3,50) * 1/3);

[t,y] = ode45(@(t,y) cartpole(y,m,M,g,L,d,u), t, y0 );
%[t,y] = f_cap(y0 , u);

for i = 1:length(t)
   draw_cartpole(y(i,:), L);
end