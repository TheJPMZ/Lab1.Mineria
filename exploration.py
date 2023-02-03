import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pandas_profiling import ProfileReport

from quickda.explore_data import *
from quickda.clean_data import *
from quickda.explore_numeric import *
from quickda.explore_categoric import *
from quickda.explore_numeric_categoric import *
from quickda.explore_time_series import *

datos = pd.read_csv('baseball.csv')

# 1.1 Explore data making a summary of the data
#print(datos.head())
#print(datos.describe())
#print(datos.info())
#explore(datos)
#profile = ProfileReport(datos)
#profile.to_file("your_report.html")

# 1.3
#eda_num(datos)
#eda_cat(datos, "game_type")

#1.4
cat_col = ["away_team","boxscore_url","date","game_type","home_team","other_info_string"]
#numeric_datos = clean(datos, "dropcols", cat_col)

#eda_num(numeric_datos, method='correlation')
#profile_num = ProfileReport(datos)
#profile_num.to_file("your_report2.html")



# 1.5

#for x in cat_col:
#    eda_cat(datos, x)

# 1.6

#Open the file and erase every "']" and ": "
datos = datos.replace("']","", regex=True)
datos = datos.replace(": ","", regex=True)
datos = datos.replace("Start Time","", regex=True)
datos = datos.replace("Local","", regex=True)

cat_col = ["away_team","boxscore_url","date","game_type","home_team","other_info_string"]
datos = clean(datos, "dtypes", cat_col, "category")

datos = clean(datos, "dropcols", ["other_info_string","boxscore_url",])

datos = clean(datos, "standardize")

datos = clean(datos, "duplicates")

datos = clean(datos, method = "dropmissing")

d = clean(datos, "replaceval",
		  columns = ["attendance"],
		  to_replace = "",
		  value = np.nan)