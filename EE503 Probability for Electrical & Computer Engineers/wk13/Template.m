clear
rho = .7;
Numsamples=1000; %Change this to 1000 or more when you are done
Numss = 100;% Numss is the number of sigma-squared values considered (must be at least 2).
SSMIN = 0.0001; %This is the smallest sigma-squared value
SSMAX = .1; % This is the largest sigma-squared value


MSE1 = zeros(1,Numss);
MSE3 = zeros(1, Numss);
ExactMSE1 = zeros(1, Numss);
ssvals = zeros(1,Numss);

for ssindex=1:Numss
    ss = SSMIN + ((ssindex-1)/(Numss-1))*(SSMAX-SSMIN);
    ssvals(ssindex)=ss;
    a=rho/(5*(rho^2/7+ss));

    sum1=0;
    sum3=0;

    weird = 0;
    for i=1:Numsamples
       X=random('uniform', -1, 1);
       N=random('norm', 0, sqrt(ss));
       Y = rho*X^3+ N;

       Xhat1 = a*Y;


       topf = @(x) x.*exp(-1.*((Y-rho.* x.^3).^2)./(2*ss));
       bottomf = @(x) exp(-1.*((Y-rho.* x.^3).^2)./(2*ss));

       Xhat3 = integral(topf, -1,1)/integral(bottomf,-1,1);

       if ((Xhat3>1)||(Xhat3<-1))
           weird=Xhat3;
       end

       SE1 = (Xhat1-X)^2;
       SE3 = (Xhat3-X)^2;

       sum1 = sum1*(i-1)/i + SE1*1.0/i;
       sum3 = sum3*(i-1)/i + SE3*1.0/i;


    end

    MSE1(ssindex) = sum1;
    MSE3(ssindex) = sum3; 
    ExactMSE1(ssindex) = a^2*(0.07+ss)-0.28*a+1/3;

end

v = ones(size(ssvals));
hLines = plot(ssvals, ExactMSE1, '-m',  ssvals, MSE1, '--b', ssvals, (1/3)*v,'-r', ssvals, MSE3, '-.g')
title('Numsamples=1000')
xlabel('ss')
ylabel('MSE')
legend(hLines, 'ExactMSE1', 'MSE1', 'Constant', 'MSE3', 'Location', 'Southeast');

weird
