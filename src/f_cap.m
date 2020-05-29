function [t,X] = f_cap(y0,u)
% y0 = Inital conditions
% u = Sequence of control
    m = 0.209;
    M = 0.411;
    g = -9.8;
    L = 0.336;  % meters
    d = 17;
    [t,X] = ode45(@(t,y) cartpole(y,m,M,g,L,d,u( floor(49*t + 1) )), 0:0.02:1, y0 );
end