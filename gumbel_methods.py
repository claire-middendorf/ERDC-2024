# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 14:10:42 2024

@author: clairemiddendorf
"""

# import
import numpy as np
import pandas as pd
import math as math



def process_peakflow_data(data=pd.DataFrame):
    """process peakflow dataframe for analysis"""

    data = data.sort_values(by='peak_streamflow', ascending=False)
    n = len(data)
    rank = range(1,n+1,1)
    data.insert(0, "Rank", rank, True)
    data.reset_index(drop=True, inplace=True)

    return data


def gumbel_stats(data=pd.DataFrame, return_periods=list):
    """add additional statistics; returns two structures"""

    # statistics
    n = len(data)
    avg_Q = data["peak_streamflow"].mean()
    stdev = np.std(data['peak_streamflow'], ddof=1)
    alpha = ((math.sqrt(6))*stdev)/3.1415926
    mu = avg_Q - 0.5772*alpha
    a = 0.44 #constant using Gringotten's method
   
    data['qi - Exceedance Probability'] = data['Rank'].apply(
        lambda x: (x - a)/(n+1-(2*a)))
    
    data['pi - non-exceedance Probability'] = data['qi - Exceedance Probability'].apply(
        lambda x: 1-x)
    
    data['Tp Estimated'] = data['pi - non-exceedance Probability'].apply(
        lambda x: 1/(1-x))
    
    data['(x-mu)/alpha'] = data['peak_streamflow'].apply(
        lambda x: (x-mu)/alpha)
    
    data['p theoretical'] = data['(x-mu)/alpha'].apply(
        lambda x: math.exp((-math.exp(-x))))
    
    data['Tp Theoretical'] = data['p theoretical'].apply(
        lambda x: 1/(1-x))
    
    #find peak streamflows of specific flood years
    
    floods = pd.DataFrame()
    floods['Return Periods'] = return_periods
    floods['Peak Streamflow (cfs)'] = floods['Return Periods'].apply(
        lambda x: -alpha * math.log(-math.log(1-(1/x))) + mu )
    

    return data, floods
