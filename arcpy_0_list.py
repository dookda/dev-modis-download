import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/workspace/modis/ndvi_2017_warp_32647_bm"

# Get and print a list of GRIDs from the workspace
rasters = arcpy.ListRasters("*", "TIF")
for r in rasters:
    rname = r[:8]
    print(rname)
    


