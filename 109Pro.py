import plotly.figure_factory as ff
import pandas as pd
import statistics
df = pd.read_csv("StudentsPerformance2.csv")
S = df["reading score"].tolist()

Smean = statistics.mean(S)
SStd = statistics.stdev(S)
Smedian = statistics.median(S)
Smode = statistics.mode(S)

IStdS, IStdE = Smean-SStd, Smean+SStd
IIStdS, IIStdE = Smean-(2*SStd), Smean+(2*SStd)
IIIStdS, IIIStdE = Smean-(3*SStd), Smean+(3*SStd)

f = ff.create_distplot([S], ["reading scores"], show_hist=False)
f.show()

IStd = [result for result in S if result > IStdS and result < IStdE]
IIStd = [result for result in S if result > IIStdS and result < IIStdE]
IIIStd = [result for result in S if result > IIIStdS and result < IIIStdE]
print(Smean)
print(Smedian)
print(Smode)
print(SStd)
print("{}%".format(len(IStd)*100.0/len(S)))
print("{}%".format(len(IIStd)*100.0/len(S)))
print("{}%".format(len(IIIStd)*100.0/len(S)))