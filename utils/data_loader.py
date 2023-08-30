import numpy as np
import pandas as pd

def _get_distances_from_dbfs():
    distances = pd.read_parquet("/dbfs/FileStore/demo_optimalisatie/Rotterdam_pois_distances.parquet").values
    return distances
