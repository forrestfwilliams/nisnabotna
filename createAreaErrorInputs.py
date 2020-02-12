import arcpy
import os
import pandas as pd
arcpy.env.overwriteOutput = True

os.chdir('C:\\Users\\fwillia1\\Desktop\\delineations')

aimm = 'cleaning.shp'
sites = ['1_3', '1_4', '1_5', '1_6', '2_3', '2_4', '2_5', '2_6', '3_3', '3_4',
         '3_5', '3_6', 'drake6', 'galloway4', 'graeve3',
         'griswold4', 'harris6', 'lamberson3', 'newell4',
         'niehaus3', 'schnepel6', 'schwenke5', 'stortenbecker5', 'toman5']

for site in sites:
    print(site)
    mask = '{}_mask.shp'.format(site)
    delin = '{}_pol.shp'.format(site)
##    clipMask = arcpy.CopyFeatures_management(mask, 'oldMasks\\{}'.format(mask))
    clipMask= arcpy.Clip_analysis(mask, 'oldMasks\\bbox.shp', 'oldMasks\\{}'.format(mask))
    aimmClip = arcpy.Clip_analysis(aimm, clipMask, 'oldMasks\\{}_aimm.shp'.format(site))
    delinClip = arcpy.Clip_analysis(delin, clipMask, 'oldMasks\\{}_delin.shp'.format(site))
