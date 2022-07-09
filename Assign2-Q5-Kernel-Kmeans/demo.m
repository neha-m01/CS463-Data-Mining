clear; close all;
d = 2;
k = 2;

n = 508; % the total # of objects 
X=[copy and paste the 2D data from the excel file]; X=X’; 

init = ceil(k*rand(1,n));
[y,model,mse] = knKmeans(X,init,@knGauss);
plotClass(X,y)

idx = 1:2:n;
Xt = X(:,idx);
t = knKmeansPred(model, Xt);
plotClass(Xt,t)