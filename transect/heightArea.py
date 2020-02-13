import pandas as pd
import seaborn as sns
from sklearn.metrics import mean_squared_error as mse
from sklearn.metrics import mean_absolute_error as mae
import matplotlib.pyplot as plt

data = pd.read_csv('transects.csv')

ids = data['LINE_ID'].unique()

# for i in ids:
#     tran = data[data['LINE_ID'] == i]
#     f, (ax1) = plt.subplots(1, 1, figsize=(15, 10))
#     sns.scatterplot('FIRST_DIST','FIRST_Z', ax=ax1 , data = tran)
#     plt.savefig('{}.png'.format(i))

ss = pd.read_csv('startStop.csv')
ls =  []
for i in ids:
    tran1 = ss[ss['OBJECTID'] == i]
    startE = int(tran1['top E bank'])
    stopE =  int(tran1['bottom E bank'])
    startD =  int(tran1['top D bank'])
    stopD =  int(tran1['bottom D bank'])
    
    tran2 = data[data['LINE_ID'] == i]
    startE = list(tran2['FIRST_Z'])[startE-1]
    stopE = list(tran2['FIRST_Z'])[stopE-1]
    startD = list(tran2['FIRST_Z'])[startD-1]
    stopD = list(tran2['FIRST_Z'])[stopD-1]

    hgtE = startE-stopE
    hgtD = stopD - startD
    
    row ={'id':i, 'hgtE':hgtE/100, 'hgtD':hgtD/100}
    ls.append(row)
    
df = pd.DataFrame(ls)
df['E hdiff'] = ss['E hdiff']
df['D hdiff'] = ss['D hdiff']

erd = pd.DataFrame()
dep = pd.DataFrame()
erd[['profile', 'aimm']] =  df[['hgtE', 'E hdiff']]
dep[['profile', 'aimm']] =  df[['hgtD', 'D hdiff']]

allDF = erd.append(dep)

print(allDF.aimm.mean())
print(mse(allDF.profile, allDF.aimm) ** 0.5)
print(mae(allDF.profile, allDF.aimm))