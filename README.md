# GIS_Python
Python scripts for basic GIS analyses

Includes:

1. Explore_gdb script to get useful information about a geodatabase (name of feature classes, column headings, coordinate system, geometry type and plot of each feature class). It works when user supplies directory of the geodatabase.
2. Surface_raster_automated script which has as an input contour lines or a DEM, and aspect, slope, hillshade and curvature rasters will be generated. The user should specify the units for slope raster (degrees or percent rise) and which method is used to calculate aspect and slope, wether geodesic or planar (geodesic is better for long very long extensions). The rasters will be saved in an output folder specified by the user.
