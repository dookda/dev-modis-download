import arcpy
from arcpy import env
from arcpy.sa import *

# Set the current workspace
arcpy.env.workspace = "C:/workspace/modis/ndvi_2017_warp_32647_npp"

outfolder = "C:/workspace/modis/ndvi_2017_warp_32647_bm/"

arcpy.CheckOutExtension("Spatial")
# Get and print a list of GRIDs from the workspace
rasters = arcpy.ListRasters("*", "TIF")

for r in rasters:
    rname = r[:10]+".tif"
    print(rname)
    # Execute Times
    outRas = Divide(r, 0.5)
    # Save the output 
    outRas.save(outfolder+rname)
    print("ok ")

