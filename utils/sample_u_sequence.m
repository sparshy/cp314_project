function u = sample_u_sequence( values, theta)
%SAMPLE_U_SEQUENCE Give number of samples and a categorical pmf returns a vector
%of amples
%   values{row vector} : Associated values vector
%   theta{ 3xH matrix} : cat dist vector
[~,n] = size(theta);
u = zeros(1,n);
for i=1:n
    u(i) = sample_cat_pmf(1, theta(:,i)', values);
end
end