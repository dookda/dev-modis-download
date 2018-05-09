import arcpy
from arcpy import env
from arcpy.sa import *

## set workspace
## arcpy.env.workspace = "C:/workspace/modis/solar_interp"

## IDW variables
fs = "C:/workspace/modis/thailand_solar_av5y_32647.shp"
mask = "C:/workspace/modis/thailand_boundary_32647.shp"
out = "C:/workspace/modis/solar_interp/"
cellSize =250.0
power = 2
searchRadius = RadiusVariable(12, 150000)

# Check out the ArcGIS Spatial Analyst extension license
arcpy.CheckOutExtension("Spatial")
arcpy.env.extent = mask
arcpy.env.mask = mask

fields = arcpy.ListFields(fs)
i = 0
for field in fields:
    if field.name[:2] == 'sr':
        # Execute IDW
        # outIDW = Idw(fs, field.name, cellSize, power, searchRadius)
        # Save the output 
        # outIDW.save(out+field.name)
        print field.name+" ok"



