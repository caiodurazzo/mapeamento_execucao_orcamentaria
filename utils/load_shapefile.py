import os
import geopandas as gpd
from config import DATA_FOLDER

def load_shapefile(folder_name: str, filename: str = "data.shp", **read_kwargs) -> gpd.GeoDataFrame:
    """
    Load a shapefile from a specified subfolder within the data folder.

    Args:
        folder_name (str): The name of the subfolder inside DATA_FOLDER where the shapefile is stored.
        filename (str, optional): The name of the shapefile. Defaults to 'data.shp'.
        **read_kwargs: Additional keyword arguments passed to geopandas.read_file().

    Returns:
        gpd.GeoDataFrame: The loaded GeoDataFrame.
    """
    file_path = os.path.join(DATA_FOLDER, folder_name, filename)
    
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The shapefile {filename} does not exist in {os.path.join(DATA_FOLDER, folder_name)}.")
    
    return gpd.read_file(file_path, **read_kwargs)