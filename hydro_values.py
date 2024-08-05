# -*- coding: utf-8 -*-

"""
Claire Middendorf

    Creates a unit hydrograph for a specific flood duration in 15 minute intervals

"""

#import libraries
import pandas as pd
import numpy as np


def hydro_vals(flood_duration,interval_hr):
    
    HYDRO = '/Users/clairemiddendorf/Desktop/repos/ERDC-2024-main/hydrograph.csv' #unit hydrograph csv file

    unit_hydro = pd.read_csv(HYDRO)
    
    num_points = len(unit_hydro)
    
    num_intervals = flood_duration * 24 * (1/interval_hr)
    
    inter_num = round(num_intervals/(num_points-1))
    
    new_hydrograph = pd.DataFrame()
    
    x = 0
    while x < num_points:
        
        if x + 1 == 33:
            break
        
        else:
            x_point = [unit_hydro.iloc[x,0],unit_hydro.iloc[x+1,0]]
            y_point = [unit_hydro.iloc[x,1],unit_hydro.iloc[x+1,1]]
            
            x_values = np.linspace(x_point[0],x_point[1],inter_num)
            
            interp_values = np.interp(x_values, x_point,y_point)
            
            interp_df = pd.DataFrame({"t/tp": x_values,
                        "q/qp":interp_values})
        
            
        new_hydrograph = pd.concat([new_hydrograph, interp_df], ignore_index=True, axis = 0)
        
        x = x+1
    
    peak = inter_num * 10
    
    rising_list = []
    falling_list = []
    
    
    x = 0
    while x < len(new_hydrograph):
        
        if x<peak:
            rising_list.append(new_hydrograph.iloc[x,1])
        
        else:
            falling_list.append(new_hydrograph.iloc[x,1])
        
        x = x+1
     
    rising_list.reverse()
    falling_list.reverse()
    
    limbs = rising_list + falling_list
 
    baseflow_vals = pd.DataFrame({"values": limbs})
    
    
    return new_hydrograph, baseflow_vals  
    
    

        
    
    
    
    
    
    
    
    
    
    
    





