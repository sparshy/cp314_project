m = 1;
M = 10;
g = -9.8;
L = 1;
d = 17;
u = 0;

t = [0:0.1:100];
y0 = [ 2, 0, pi, 0.5]';

[t,y] = ode45(@(t,y) cartpole(y,m,M,g,L,d,u), t, y0 );

for i = 1:length(t)
   draw_cartpole(y(i,:), L);
end