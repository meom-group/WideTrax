from collections import defaultdict
from datetime import datetime, timedelta
import os
import re
import sys
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import matplotlib.pyplot as plt
import numpy as np
import pyinterp
import pyinterp.fill as fill
import xarray as xr

# =============================================================================
# filtre_donnees
# =============================================================================

def filtre_donnees(donnees, seuil_min, seuil_max, type_filtre="passe-bas"):
    """
    Filters the data based on the specified thresholds and the chosen filter type.

    This function applies a filter to the provided data, either in low-pass or high-pass mode. Data outside the thresholds will be excluded
    
    Parameters
    -----------
    param donnees : str
        Path to the directory containing the NetCDF files
    param seuil_min : list
        List with the boundaries of the region of interest [longitude_min, latitude_min, longitude_max, latitude_max]
    param seuil_max : str
        the max seuil
    param type_filtre : int
        just for test
    
    Returns
    --------
    donnees_filtrees : Dict
        Dictionary containing the xarray.Datasets for the region
        
    """
    if type_filtre not in ["passe-bas", "passe-haut"]:
        raise ValueError("Le type de filtre doit être 'passe-bas' ou 'passe-haut'.")
    
    if not isinstance(donnees, (list, np.ndarray)):
        raise TypeError("Les données doivent être une liste ou un tableau numpy.")
    
    if type_filtre == "passe-bas":
        # Garder uniquement les valeurs en dessous du seuil_max
        donnees_filtrees = [x for x in donnees if x <= seuil_max]
    else:  # Passe-haut
        # Garder uniquement les valeurs au-dessus du seuil_min
        donnees_filtrees = [x for x in donnees if x >= seuil_min]
    
    return donnees_filtrees

# =============================================================================
# test_function
# =============================================================================

def test_function(a, b):
    """
    This is a test function that adds two numbers.

    Parameters
    ----------
    a : int or float
        The first number.
    b : int or float
        The second number.

    Returns
    -------
    result : int or float
        The sum of `a` and `b`.

    """
    result = a + b
    return result

