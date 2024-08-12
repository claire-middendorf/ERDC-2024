# ERDC-2024
I created this Python script to perform flood frequency analysis and then create hydrographs. 

flood_frequency_interval.py file: The scripts can either perform a Log-Pearson Type 3 analysis or a Gumbel analysis. The script will then create a hydrograph for either of these analyses. There is an example of the input file required for this script in the required files folder (sample_FFA_input.csv). This data can be found using the USGS National Water Dashboard and going to the site page for the river station. 

There are some other inputs that are needed to run the program: 

REGIONAL_SKEW : regional skew coefficient for river station, found using the map image (skew_coeffs_map.png) in the required files folder; used in Log-Pearson Type III analysis 

flood_duration = desired duration of flood (days) 

base_flow = base flow of river; can be found using the USGS Baseflow Forecasts 

return_periods = desired return periods 

interval_min = the desired hydrograph output interval (eg put 15 if you want flows for every 15 minutes of the flood) 

A hydrograph is a graph showing the rate of flow versus time. In this case, it represents the flow rate during a flooding event predicted by a flood frequency analysis. The triangular_hydrograph Python file will create a triangular hydrograph (equivalent to the curvilinear hydrograph) if you already have the return periods and the peak stream flows. A sample input file for this script is in the required files folder. (sample_hydrograph_input.csv)  

Some other required files are needed to run this program successfully. The k_table.csv file contains the k values needed to perform a Log-Pearson Type 3 analysis. The reverse.csv file is needed to create hydrographs as it helps calculate the base flow values to add to the hydrograph. The hydrograph.csv file is the USGS unit hydrograph used to create hydrographs for each flood frequency analysis.  
