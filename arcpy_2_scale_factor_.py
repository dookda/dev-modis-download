import arcpy
from arcpy import env
from arcpy.sa import *

# Set the current workspace
arcpy.env.workspace = "C:/workspace/modis/ndvi_2017_warp_32647"

outfolder = "C:/workspace/modis/ndvi_2017_warp_32647_scalefactor/"

arcpy.CheckOutExtension("Spatial")
# Get and print a list of GRIDs from the workspace
rasters = arcpy.ListRasters("*", "TIF")

for r in rasters:
    rname = r[13:21]+".tif"
    print(rname)
    # Execute Times
    outTimes = Times(r, 0.0001)
    # Save the output 
    outTimes.save(outfolder+rname)
    print("ok")

