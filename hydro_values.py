# -*- coding: utf-8 -*-

"""
Claire Middendorf

    Creates a unit hydrograph for a specific flood duration in intervals

"""

#import libraries
import pandas as pd
import numpy as np



def hydro_vals(flood_duration,interval_hr):
    
    HYDRO = '/Users/clairemiddendorf/Desktop/repos/ERDC-2024-main/hydrograph.csv' #unit hydrograph csv file
    
    INVERSE ='/Users/clairemiddendorf/Desktop/repos/ERDC-2024-main/reverse.csv'

    unit_hydro = pd.read_csv(HYDRO)
    
    unit_inverse = pd.read_csv(INVERSE)
    
    num_points = len(unit_hydro)
  
    num_intervals = flood_duration * 24 * (1/interval_hr) 
    
    #number of points between each int
    inter_num = round(num_intervals/5)
     
    new_hydrograph = pd.DataFrame()
    
    baseflow_vals = pd.DataFrame()
    
    
    x = 0
    while x < num_points:
        
        if x + 1 == 33:
            break
        
        if x == 0: 
            
            x_point = [unit_hydro.iloc[x,0],unit_hydro.iloc[x+1,0]]
            y_point = [unit_hydro.iloc[x,1],unit_hydro.iloc[x+1,1]]
            
            points = round((x_point[1] - x_point[0]) * inter_num) + 1
            
            x_values = np.linspace(x_point[0],x_point[1],points)
            
            interp_values = np.interp(x_values, x_point,y_point)
            
            interp_df = pd.DataFrame({"t/tp": x_values,
                        "q/qp":interp_values})
            
        
        else:
            
            x_point = [unit_hydro.iloc[x,0],unit_hydro.iloc[x+1,0]]
            y_point = [unit_hydro.iloc[x,1],unit_hydro.iloc[x+1,1]]
            
            points = round((x_point[1] - x_point[0]) * inter_num) + 1
            
            x_values = np.linspace(x_point[0],x_point[1],points)
            
            interp_values = np.interp(x_values, x_point,y_point)
            
            interp_df = pd.DataFrame({"t/tp": x_values,
                        "q/qp":interp_values})
            
            interp_df = interp_df.drop(0)
        
            
        new_hydrograph = pd.concat([new_hydrograph, interp_df], ignore_index=True, axis = 0)
        
        x = x+1
        
    
    
    x = 0
    while x < num_points:
        
        if x + 1 == 33:
            break
        
        else:
            x_point = [unit_inverse.iloc[x,0],unit_inverse.iloc[x+1,0]]
            y_point = [unit_inverse.iloc[x,1],unit_inverse.iloc[x+1,1]]
            
            points = round((x_point[1] - x_point[0]) * inter_num) + 1
            
            x_values = np.linspace(x_point[0],x_point[1],points)
            
            interp_values = np.interp(x_values, x_point,y_point)
            
            interp_df = pd.DataFrame({"t/tp": x_values,
                        "q/qp":interp_values})
        
            
        baseflow_vals = pd.concat([baseflow_vals, interp_df], ignore_index=True, axis = 0)
        
        x = x+1
    
    
    return new_hydrograph, baseflow_vals  
    
    
