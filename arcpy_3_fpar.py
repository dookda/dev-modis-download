import arcpy
from arcpy import env
from arcpy.sa import *

# Set the current workspace
arcpy.env.workspace = "C:/workspace/modis/ndvi_2017_warp_32647_scale_factor"

outfolder = "C:/workspace/modis/ndvi_2017_warp_32647_fpar"

arcpy.CheckOutExtension("Spatial")
# Get and print a list of GRIDs from the workspace
rasters = arcpy.ListRasters("*", "TIF")

for r in rasters:
    #prefix = r[5:8]
    #rname = r
    rname = r[:10]
    print(rname)
    # Execute Times
    outRas = Plus(-0.1, Times(r, 1.5))
    # Save the output 
    outRas.save(outfolder+"/"+rname+".tif")
    print("ok ")

