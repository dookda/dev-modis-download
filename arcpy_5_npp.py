import arcpy
from arcpy import env
from arcpy.sa import *

# Set the current workspace
arcpy.env.workspace = "C:/workspace/modis/ndvi_2017_warp_32647_scale_factor"

outfolder = "C:/workspace/modis/ndvi_2017_warp_32647_npp/"
sr = "C:/workspace/modis/solar_interp/"

arcpy.CheckOutExtension("Spatial")
# Get and print a list of GRIDs from the workspace
rasters = arcpy.ListRasters("*", "TIF")

for r in rasters:
    #sr = solarRas+r[-11:-4]
    rname = r[:10]+".tif"
    rint = int(r[-7:-4])
    print(rname)
    
    # Execute Times
    if rint <= 31:
        outRas = Times(0.45, Times(1.8, Times(Plus(-0.1, Times(r, 1.5)), Times(0.45, sr+"sr_jan.tif"))))
    elif rint <= 59:
        outRas = Times(0.45, Times(1.8, Times(Plus(-0.1, Times(r, 1.5)), Times(0.45, sr+"sr_feb.tif"))))
    elif rint <= 90:
        outRas = Times(0.45, Times(1.8, Times(Plus(-0.1, Times(r, 1.5)), Times(0.45, sr+"sr_mar.tif"))))
    elif rint <= 120:
        outRas = Times(0.45, Times(1.8, Times(Plus(-0.1, Times(r, 1.5)), Times(0.45, sr+"sr_apr.tif"))))
    elif rint <= 151:
        outRas = Times(0.45, Times(1.8, Times(Plus(-0.1, Times(r, 1.5)), Times(0.45, sr+"sr_may.tif"))))
    elif rint <= 181:
        outRas = Times(0.45, Times(1.8, Times(Plus(-0.1, Times(r, 1.5)), Times(0.45, sr+"sr_jun.tif"))))
    elif rint <= 212:
        outRas = Times(0.45, Times(1.8, Times(Plus(-0.1, Times(r, 1.5)), Times(0.45, sr+"sr_jul.tif"))))
    elif rint <= 243:
        outRas = Times(0.45, Times(1.8, Times(Plus(-0.1, Times(r, 1.5)), Times(0.45, sr+"sr_aug.tif"))))
    elif rint <= 273:
        outRas = Times(0.45, Times(1.8, Times(Plus(-0.1, Times(r, 1.5)), Times(0.45, sr+"sr_sep.tif"))))
    elif rint <= 304:
        outRas = Times(0.45, Times(1.8, Times(Plus(-0.1, Times(r, 1.5)), Times(0.45, sr+"sr_oct.tif"))))
    elif rint <= 334:
        outRas = Times(0.45, Times(1.8, Times(Plus(-0.1, Times(r, 1.5)), Times(0.45, sr+"sr_nov.tif"))))
    elif rint <= 365:
        outRas = Times(0.45, Times(1.8, Times(Plus(-0.1, Times(r, 1.5)), Times(0.45, sr+"sr_dec.tif"))))

    # Save the output 
    outRas.save(outfolder+rname)
    print("ok ")
    

