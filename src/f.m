function [t,X] = f(y0,u)
% y0 = Inital conditions
% u = Sequence of control
    m = 0.209;
    M = 0.711;
    g = -9.8;
    L = 0.336;
    d = 17;
    [t,X] = ode45(@(t,y) cartpole(y,m,M,g,L,d,u), 0:0.01:0.02, y0 );
end