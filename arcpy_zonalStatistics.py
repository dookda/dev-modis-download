import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/workspace/modis/ndvi_2017_warp_32647_bm"
outfolder = "C:/workspace/modis/ndvi_2017_warp_32647_bm_zstat/"

# Set local variables
#inZoneData = "C:/workspace/modis/straw_sample_point_32647.shp"
#zoneField = "ID_ZST"
#inZoneData = "C:/workspace/modis/thailand_landuse_a_32647.shp"
#zoneField = "GLU_CODE"
inZoneData = "C:/workspace/modis/th_lu_32647"
zoneField = "GLU_CODE"

    
arcpy.CheckOutExtension("Spatial")

# Get and print a list of GRIDs from the workspace
rasters = arcpy.ListRasters("*", "TIF")
for r in rasters:
    rname = r[:8]+".dbf"
    print(rname)
    outZSaT = ZonalStatisticsAsTable(inZoneData, zoneField, r, 
                                 outfolder+rname, "NODATA", "ALL")
    print("ok")
    


