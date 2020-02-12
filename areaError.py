import arcpy
import os
import pandas as pd
from sklearn.metrics import mean_squared_error as mse
from sklearn.metrics import mean_absolute_error as mae
arcpy.env.overwriteOutput = True

os.chdir('C:\\Users\\fwillia1\\Desktop\\delineations\\oldMasks')

sites = ['1_3', '1_4', '1_5', '1_6', '2_3', '2_4', '2_5', '2_6', '3_3', '3_4',
         '3_5', '3_6', 'drake6', 'galloway4', 'graeve3',
         'griswold4', 'harris6', 'lamberson3', 'newell4',
         'niehaus3', 'schnepel6', 'schwenke5', 'stortenbecker5', 'toman5']

allDF = pd.DataFrame()
for site in sites:
    sitePol = '{}_delin.shp'.format(site)
    aimmPol = '{}_aimm.shp'.format(site)

    siteDF = pd.DataFrame(
        arcpy.da.FeatureClassToNumPyArray(sitePol, ['gridcode', 'area']))
    siteDF = siteDF.groupby('gridcode').sum().reset_index()
    siteDF['method'] = 'delineation'

    aimmDF = pd.DataFrame(
        arcpy.da.FeatureClassToNumPyArray(aimmPol, ['gridcode', 'area']))
    aimmDF = aimmDF.groupby('gridcode').sum().reset_index()
    aimmDF['method'] = 'aimm'

    bothDF = siteDF.append(aimmDF)
    bothDF['site'] = site
    allDF = allDF.append(bothDF)

allDF.to_csv('test.csv')
dif = allDF
dif = allDF.loc[allDF['gridcode'] == 1]
deposition = dif.pivot(index='site', columns='method', values='area')
deposition.to_csv('deposition.csv')

dif = allDF.loc[allDF['gridcode'] == 2]
erosion = dif.pivot(index='site', columns='method', values='area')
erosion.to_csv('erosion.csv')

merged = deposition.merge(erosion, on='site')
merged['aimm'] = merged.aimm_x - merged.aimm_y
merged['delineation'] = merged.delineation_x - merged.delineation_y
merged.to_csv('merged.csv')

print(deposition.aimm.mean())
print(mse(deposition.delineation, deposition.aimm) ** 0.5)
print(mae(deposition.delineation, deposition.aimm))

print(erosion.aimm.mean())
print(mse(erosion.delineation, erosion.aimm) ** 0.5)
print(mae(erosion.delineation, erosion.aimm))
