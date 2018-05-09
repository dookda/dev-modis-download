import arcpy
from arcpy import env
from arcpy.sa import *

# Set the current workspace
arcpy.env.workspace = "C:/workspace/modis/ndvi_2017_warp_32647"

nppOut = "C:/workspace/modis/ndvi_2017_warp_32647_npp/"
bmOut = "C:/workspace/modis/ndvi_2017_warp_32647_bm/"
sr = "C:/workspace/modis/solar_interp/"

arcpy.CheckOutExtension("Spatial")
# Get and print a list of GRIDs from the workspace
rasters = arcpy.ListRasters("*", "TIF")

for r in rasters:
    #sr = solarRas+r[-11:-4]
    rname = r[13:21]+".tif"
    rint = int(r[18:21])
    print(rname)
    print(rint)
    
    # Execute Times
    if rint <= 31:
        npp = Con(Times(0.45, Times(1.8, Times(Plus(-0.1, Times(Times(r, 0.0001), 1.5)), Times(0.45, sr+"sr_jan.tif")))) > 0, Times(0.45, Times(1.8, Times(Plus(-0.1, Times(Times(r, 0.0001), 1.5)), Times(0.45, sr+"sr_jan.tif")))), 0)
        bm = Divide(npp, 0.5)
    elif rint <= 59:
        npp = Con(Times(0.45, Times(1.8, Times(Plus(-0.1, Times(Times(r, 0.0001), 1.5)), Times(0.45, sr+"sr_feb.tif")))) > 0, Times(0.45, Times(1.8, Times(Plus(-0.1, Times(Times(r, 0.0001), 1.5)), Times(0.45, sr+"sr_feb.tif")))), 0)
        bm = Divide(npp, 0.5)
    elif rint <= 90:
        npp = Con(Times(0.45, Times(1.8, Times(Plus(-0.1, Times(Times(r, 0.0001), 1.5)), Times(0.45, sr+"sr_mar.tif")))) > 0, Times(0.45, Times(1.8, Times(Plus(-0.1, Times(Times(r, 0.0001), 1.5)), Times(0.45, sr+"sr_mar.tif")))), 0)
        bm = Divide(npp, 0.5)
    elif rint <= 120:
        npp = Con(Times(0.45, Times(1.8, Times(Plus(-0.1, Times(Times(r, 0.0001), 1.5)), Times(0.45, sr+"sr_apr.tif")))) > 0, Times(0.45, Times(1.8, Times(Plus(-0.1, Times(Times(r, 0.0001), 1.5)), Times(0.45, sr+"sr_apr.tif")))), 0)
        bm = Divide(npp, 0.5)
    elif rint <= 151:
        npp = Con(Times(0.45, Times(1.8, Times(Plus(-0.1, Times(Times(r, 0.0001), 1.5)), Times(0.45, sr+"sr_may.tif")))) > 0, Times(0.45, Times(1.8, Times(Plus(-0.1, Times(Times(r, 0.0001), 1.5)), Times(0.45, sr+"sr_may.tif")))), 0)
        bm = Divide(npp, 0.5)
    elif rint <= 181:
        npp = Con(Times(0.45, Times(1.8, Times(Plus(-0.1, Times(Times(r, 0.0001), 1.5)), Times(0.45, sr+"sr_jun.tif")))) > 0, Times(0.45, Times(1.8, Times(Plus(-0.1, Times(Times(r, 0.0001), 1.5)), Times(0.45, sr+"sr_jun.tif")))), 0)
        bm = Divide(npp, 0.5)
    elif rint <= 212:
        npp = Con(Times(0.45, Times(1.8, Times(Plus(-0.1, Times(Times(r, 0.0001), 1.5)), Times(0.45, sr+"sr_jul.tif")))) > 0, Times(0.45, Times(1.8, Times(Plus(-0.1, Times(Times(r, 0.0001), 1.5)), Times(0.45, sr+"sr_jul.tif")))), 0)
        bm = Divide(npp, 0.5)
    elif rint <= 243:
        npp = Con(Times(0.45, Times(1.8, Times(Plus(-0.1, Times(Times(r, 0.0001), 1.5)), Times(0.45, sr+"sr_aug.tif")))) > 0, Times(0.45, Times(1.8, Times(Plus(-0.1, Times(Times(r, 0.0001), 1.5)), Times(0.45, sr+"sr_aug.tif")))), 0)
        bm = Divide(npp, 0.5)
    elif rint <= 273:
        npp = Con(Times(0.45, Times(1.8, Times(Plus(-0.1, Times(Times(r, 0.0001), 1.5)), Times(0.45, sr+"sr_sep.tif")))) > 0, Times(0.45, Times(1.8, Times(Plus(-0.1, Times(Times(r, 0.0001), 1.5)), Times(0.45, sr+"sr_sep.tif")))), 0)
        bm = Divide(npp, 0.5)
    elif rint <= 304:
        npp = Con(Times(0.45, Times(1.8, Times(Plus(-0.1, Times(Times(r, 0.0001), 1.5)), Times(0.45, sr+"sr_oct.tif")))) > 0, Times(0.45, Times(1.8, Times(Plus(-0.1, Times(Times(r, 0.0001), 1.5)), Times(0.45, sr+"sr_oct.tif")))), 0)
        bm = Divide(npp, 0.5)
    elif rint <= 334:
        npp = Con(Times(0.45, Times(1.8, Times(Plus(-0.1, Times(Times(r, 0.0001), 1.5)), Times(0.45, sr+"sr_nov.tif")))) > 0, Times(0.45, Times(1.8, Times(Plus(-0.1, Times(Times(r, 0.0001), 1.5)), Times(0.45, sr+"sr_nov.tif")))), 0)
        bm = Divide(npp, 0.5)
    elif rint <= 365:
        npp = Con(Times(0.45, Times(1.8, Times(Plus(-0.1, Times(Times(r, 0.0001), 1.5)), Times(0.45, sr+"sr_dec.tif")))) > 0, Times(0.45, Times(1.8, Times(Plus(-0.1, Times(Times(r, 0.0001), 1.5)), Times(0.45, sr+"sr_dec.tif")))), 0)
        bm = Divide(npp, 0.5)

    # Save the output 
    npp.save(nppOut+rname)
    bm.save(bmOut+rname)
    
    print("ok ")

