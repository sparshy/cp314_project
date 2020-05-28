function r = sample_cat_pmf(n, dist, values)
%SAMPLE_PMF Give number of samples and a categorical pmf returns a vector
%of amples
%   n{int} : Number of samples required
%   dist{row vector} : A row vector of categorical dist.
%   values{row vector} : Associated values vector
c = cumsum([0,dist(:).']);
c = c/c(end); % make sur the cumulative is 1 
[~,~,i] = histcounts(rand(1,n),c);
r = values(i); % map to v values
end