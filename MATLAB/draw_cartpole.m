function draw_cartpole(y,L)
x = y(1);
theta = y(3);
% Width and Height of the Cart
W = 1;
H = 0.4;
% Mass parameters
r = 0.4;

%DRAW_CARTPOLE
plot([0 10], [0 0 ], 'k', 'LineWidth',2);
hold on
% Create the cart
rectangle('Position',[ x-W/2 0.4 W H]);
% Create the wheels
rectangle('Position',[x-W/2 0 0.4 0.4], 'Curvature', [1 1]);
rectangle('Position',[x+W/2-0.4 0 0.4 0.4], 'Curvature', [1 1]);
% Create the mass
rectangle('Position',[x+L*sin(theta)-r/2 0.6-L*cos(theta)-r/2 r r],'Curvature',[1 1]);
% Create the rod joining cart and mass
plot([x x+L*sin(theta)],[0.6 0.6-L*cos(theta)],'r','LineWidth',1);

axis([0 10 -5 5]);
hold off
drawnow
end

