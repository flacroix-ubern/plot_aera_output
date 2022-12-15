import sys
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#Arguments 
simulation_id=str(sys.argv[1]) 
stocktake_year=float(sys.argv[2])
print(stocktake_year)

#read aera output files, convert to pandas dataframe
print("from folder ", "/scratch/snx3000/flacroix/{}/".format(simulation_id))
print("plot full AERA output for year {}".format(stocktake_year))
aera_folder="/scratch/snx3000/flacroix/{}/".format(simulation_id)
metadata=pd.read_csv(aera_folder + "AERA/meta_data.nc.timeseries.csv")
timeseries_stocktake=metadata[metadata["year_stocktake"]==stocktake_year]
length_TS=len(timeseries_stocktake["temp_anth"])

#
#plot AERA output timeseries
fig,ax = plt.subplots(2,2,figsize=(12, 9))
ax[0,0].plot(timeseries_stocktake["year"],timeseries_stocktake["total_emission"])
ax[0,1].plot(timeseries_stocktake["year"],timeseries_stocktake["ff_emission"])
ax[1,0].plot(timeseries_stocktake["year"],timeseries_stocktake["temp_anth"])
ax[1,1].plot(timeseries_stocktake["year"],timeseries_stocktake["temp_anth_rel"])
ax[0,0].set_title("total_emission")
ax[0,1].set_title("ff_emission")
ax[1,0].set_title("temp_anth")
ax[1,1].set_title("temp_anth_rel")
fig.suptitle("{}, Stocktake={}".format(simulation_id,str(stocktake_year)),fontsize=14)
fig.savefig("aeraplot_{}_stockyear_{}.png".format(simulation_id,str(stocktake_year)))
