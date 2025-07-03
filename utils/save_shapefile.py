import os
import geopandas as gpd
from config import DATA_FOLDER

def save_shapefile(gdf: gpd.GeoDataFrame, folder_name: str):
    """
    Save a GeoDataFrame as a shapefile in the specified data folder.

    Parameters:
    - gdf: GeoDataFrame to save.
    - folder_name: Name of the subfolder (within DATA_FOLDER) to save the shapefile in.
    """
    save_path = os.path.join(DATA_FOLDER, folder_name)

    if not os.path.exists(save_path):
        os.makedirs(save_path)

    filepath = os.path.join(save_path, "data.shp")
    gdf.to_file(filepath)

    print(f"Shapefile saved to {filepath}")