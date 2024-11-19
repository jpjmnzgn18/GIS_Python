#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def explore_gdb(gdb_path):
    import geopandas as gpd
    import os
    import fiona
    import matplotlib.pyplot as plt
    layers = fiona.listlayers(gdb_path)
    for layer in layers:
        print(f"layer name is {layer}")
        gdf = gpd.read_file(gdb_path, layer = layer)
        print(f"EPSG code is {gdf.crs}")
        print(f"numer of rows is {len(gdf)}")
        print(f"geometry type is {gdf.geom_type.unique()}")
        print(f"columns are {list(gdf.columns)}\n") # starts in next line, this improves readability
        fig, ax = plt.subplots(figsize = (8,6))
        gdf.plot(ax = ax)
        ax.set_title(f"Layer: {layer}")
        plt.show()
        print("-----------------------------------")

