from ReadSP500 import Market_return as RM
from READTBill import Risk_free_return as Rf
from ComputingSimpleReturnAndVariance import Returns as R

import statsmodels.api as sm
import numpy as np
Return1=np.array(list(R["NFLX"].values()))
Return2=np.array(list(R["NVTS"].values()))
ReturnM=np.array(list(RM.values()))

Excess_return_1=np.array(Return1-Rf)
Excess_return_2=np.array(Return2-Rf)
Excess_Market_Return=np.array(ReturnM-Rf)

X = sm.add_constant(Excess_Market_Return)
# print(Excess_Market_Return)
y1 = Excess_return_1
y2 = Excess_return_2

model = sm.OLS(y1, X).fit()
# print(model.params)
alpha = model.params[0]
beta = model.params[1]
residuals = model.resid 
# print(Excess_return_1[0])
# print(alpha+beta*Excess_Market_Return[0]+residuals[0])


model2 = sm.OLS(y2, X).fit()
# print(model2.params)
alpha2 = model2.params[0]
beta2 = model2.params[1]
residuals2 = model2.resid 
# print(Excess_return_2[0])
# print(alpha2+beta2*Excess_Market_Return[0]+residuals2[0])
# print(model2.summary())

Treyner_index_1=(np.mean(Return1)-Rf)/beta
Treyner_index_2=(np.mean(Return2)-Rf)/beta2
# print(Treyner_index_1,Treyner_index_2)
# print(np.mean(Excess_Market_Return))
variance1=np.var(Return1)
variance2=np.var(Return2)
print(variance1,variance2)
Sharpe1=(np.mean(Return1)-Rf)/variance1
Sharpe2=(np.mean(Return2)-Rf)/variance2
print(Sharpe1,Sharpe2)
