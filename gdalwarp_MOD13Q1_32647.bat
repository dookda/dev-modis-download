set in_path= "C:\workspace\modis\ndvi_2017"
set out_path= "C:\workspace\modis\ndvi_2017_warp_32647"
md %out_path%

cd /d %in_path%


FORFILES /m *h27v07*.hdf /C "cmd /c gdalwarp -overwrite -t_srs EPSG:32647 -of GTiff \"HDF4_EOS:EOS_GRID:@path:MODIS_Grid_16DAY_250m_500m_VI:250m 16 days NDVI\" %out_path%\\ndvi_@fname.tif"

