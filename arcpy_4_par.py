import arcpy
from arcpy import env
from arcpy.sa import *

# Set the current workspace
arcpy.env.workspace = "C:/workspace/modis/ndvi_2017_warp_32647_scale_factor"

outfolder = "C:/workspace/modis/ndvi_2017_warp_32647_par"
solarRas = "C:/workspace/modis/solar_interp"

arcpy.CheckOutExtension("Spatial")
# Get and print a list of GRIDs from the workspace
rasters = arcpy.ListRasters("*", "TIF")

for r in rasters:
    rname = "SLR"+r[-11:-4]
    #rname = r[:10]
    rint = int(r[-7:-4])
    print(rname)

    # Execute Times
    if rint <= 31:
        outRas = Times(0.45, r)
    elif rint <= 59:
        outRas = Times(0.45, r)
    elif rint <= 90:
        outRas = Times(0.45, r)
    elif rint <= 120:
        outRas = Times(0.45, r)
    elif rint <= 151:
        outRas = Times(0.45, r)
    elif rint <= 181:
        outRas = Times(0.45, r)
    elif rint <= 212:
        outRas = Times(0.45, r)
    elif rint <= 243:
        outRas = Times(0.45, r)
    elif rint <= 273:
        outRas = Times(0.45, r)
    elif rint <= 304:
        outRas = Times(0.45, r)
    elif rint <= 334:
        outRas = Times(0.45, r)
    elif rint <= 365:
        outRas = Times(0.45, r)    

    # Save the output 
    outRas.save(outfolder+"/"+rname+".tif")
    print("ok ")

