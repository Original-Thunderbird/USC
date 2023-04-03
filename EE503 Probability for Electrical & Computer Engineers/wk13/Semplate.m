clear
rho = .7;
Numsamples=10000; %Change this to 1000 or more when you are done
Numss = 100;% Numss is the number of sigma-squared values considered (must be at least 2).
SSMIN = 0.01; %This is the smallest sigma-squared value
SSMAX = 20; % This is the largest sigma-squared value


MSE1 = zeros(1,Numss);
MSE3 = zeros(1, Numss);
MSE2 = zeros(1, Numss);
ExactMSE1 = zeros(1, Numss);
ssvals = zeros(1,Numss);

for ssindex=1:Numss
    ss = SSMIN + ((ssindex-1)/(Numss-1))*(SSMAX-SSMIN);
    ssvals(ssindex)=ss;
    a=4*rho/(3*ss + 4*rho^2);

    sum1=0;
    sum3=0;
    sum2=0;

    weird = 0;
    for i=1:Numsamples
       X=random('uniform', -2, 2);
       N=random('norm', 0, sqrt(ss));
       Y = rho*X + N;

       Xhat1 = a*Y;
       
       if (Xhat1 > 2)
           Xhat2 = 2;
       elseif (Xhat1 < -2)
           Xhat2 = -2;
       else
           Xhat2 = Xhat1;
       end

       topf = @(x) x.*exp(-1.*((Y-rho.*x).^2)./(2*ss));
       bottomf = @(x) exp(-1.*((Y-rho.*x).^2)./(2*ss));

       Xhat3 = integral(topf, -2,2)/integral(bottomf,-2,2);

       if ((Xhat3>1)||(Xhat3<-1))
           weird=Xhat3;
       end

       SE1 = (Xhat1-X)^2;
       SE3 = (Xhat3-X)^2;
       SE2 = (Xhat2-X)^2;

       sum1 = sum1*(i-1)/i + SE1*1.0/i;
       sum3 = sum3*(i-1)/i + SE3*1.0/i;
       sum2 = sum2*(i-1)/i + SE2*1.0/i;

    end

    MSE1(ssindex) = sum1;
    MSE3(ssindex) = sum3; 
    MSE2(ssindex) = sum2; 
    
    ExactMSE1(ssindex) = 4*(0.7*a-1)^2/3 + ss*a^2;

end

v = ones(size(ssvals));

hLines = plot(ssvals, ExactMSE1, '-m',  ssvals, MSE1, '--b', ssvals, (4/3)*v,':r', ssvals, MSE3, '-c', ssvals, MSE2, '-.g')
title('Numsamples=10000')
xlabel('ss')
ylabel('estimations')
legend(hLines, 'ExactMSE1', 'MSE1', 'Constant', 'MSE3', 'MSE2', 'Location', 'Southeast');

weird
