loopNum = 50000;
X_mSumToCur = zeros(loopNum, 1);
X_mAvgAtCur = zeros(loopNum, 1);
mInd = 1:loopNum;
preSum = 0;
for loop = 1:loopNum
   count = 0;
   curSample = randsample(1322, 1103);
   for ind = 1:1103
       if(curSample(ind)<769)
           count = count + 1;
       end
   end
   if(abs(count/1103-768/1322)>= 0.0168266)
       curVal = 1;
   else
       curVal = 0;
   end
   X_mSumToCur(loop) = preSum + curVal;
   X_mAvgAtCur(loop) = X_mSumToCur(loop)/loop;
   preSum = X_mSumToCur(loop);
end
stdOneMom = std(X_mAvgAtCur)^2;
avgOneMom = mean(X_mAvgAtCur);
plot(mInd, X_mAvgAtCur);
title('M=50000')
xlabel('m')
ylabel('estimation')