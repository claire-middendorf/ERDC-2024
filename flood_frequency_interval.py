# -*- coding: utf-8 -*-

"""
Claire Middendorf

    Process Log-Pearson Type III or Gumbel flood frequency analysis 
    Produces hydrographs after each analysis

"""

# import libraries
import matplotlib as mpl
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import log_pearson_methods as lp
import k_table as kdata
import gumbel_methods as gb
import hydro_values as hv
from IPython.display import display
import seaborn as sns
import random

# globals
INPUT = 'station_rulo.csv' #csv file with peak streamflow data
REGIONAL_SKEW = -0.3 #regional skew for river station (use map image) for Log-Pearson
flood_duration = 57.9 #desired duration of flood (days)
base_flow = 50714 #base flow of river
return_periods = [5,10,25,50] #desired return periods for Gumbel Method
interval_min = 15 #desired output interval (ie flow every 15 minutes)

interval_hr = interval_min/60
interval_day = interval_hr/24

#flood frequency analysis: Write 1 for Log-Pearson Type III or 2 for Gumbel
method = 1


def main():
    
    #log-pearson type III method
    if method == 1:
        # step 1 - read in peakflow data
        peak_flow_df = pd.read_csv(INPUT,
                                   header=None,
                                   names=['date', 'peak_streamflow'])
    
        # step 2 - process peakflow data
        peak_flow_df2 = lp.process_peakflow_data(peak_flow_df)
    
        # step 3 - process peakflow stats; returns df and a dict
        peakflow_df3, summary_stats_dict = lp.log_pearson_stats(peak_flow_df2)
    
        # step 4 - process coefficients
        coefficient_dict = lp.process_coefficients(skew_coeff=summary_stats_dict['skew_coeff'],
                                                   regional_skew=REGIONAL_SKEW,
                                                   n=len(peakflow_df3))
    
        # step 5 - process analysis
        
        # bring in frequency factors
        k_df = pd.DataFrame.from_records(kdata.frequency_factors_records)
        k_df2 = k_df.set_index('cs')
        
        # use k1 and k2 from coefficient dict
        one_k = [k_df2.loc[coefficient_dict['k1'], '1.0101'],
                 k_df2.loc[coefficient_dict['k2'], '1.0101']]
        two_k = [k_df2.loc[coefficient_dict['k1'], '2'], 
                 k_df2.loc[coefficient_dict['k2'], '2']]
        five_k = [k_df2.loc[coefficient_dict['k1'], '5'], 
                  k_df2.loc[coefficient_dict['k2'], '5']]
        ten_k = [k_df2.loc[coefficient_dict['k1'], '10'], 
                 k_df2.loc[coefficient_dict['k2'], '10']]
        twenty5_k = [k_df2.loc[coefficient_dict['k1'], '25'], 
                     k_df2.loc[coefficient_dict['k2'], '25']]
        fifty_k = [k_df2.loc[coefficient_dict['k1'], '50'], 
                   k_df2.loc[coefficient_dict['k2'], '50']]
        hundred_k = [k_df2.loc[coefficient_dict['k1'], '100'], 
                     k_df2.loc[coefficient_dict['k2'], '100']]
        twohundred_k = [k_df2.loc[coefficient_dict['k1'], '200'],
                        k_df2.loc[coefficient_dict['k2'], '200']]
        
        # initiate class
        ff_class = lp.FrequencyFactors(k1=coefficient_dict['k1'],
                                       k2=coefficient_dict['k2'],
                                       weighted_skew=coefficient_dict['weighted_skew'],
                                       avg_logQ=summary_stats_dict['avg_logQ'],
                                       stdev=summary_stats_dict['stdev'])
        
        # process k to find q
        one = ff_class.find_q(ff_class.find_k(one_k[0], one_k[1]))
        two = ff_class.find_q(ff_class.find_k(two_k[0], two_k[1]))
        five = ff_class.find_q(ff_class.find_k(five_k[0], five_k[1]))
        ten = ff_class.find_q(ff_class.find_k(ten_k[0], ten_k[1]))
        twenty_five = ff_class.find_q(ff_class.find_k(twenty5_k[0], twenty5_k[1]))
        fifty = ff_class.find_q(ff_class.find_k(fifty_k[0], fifty_k[1]))
        hundred = ff_class.find_q(ff_class.find_k(hundred_k[0], hundred_k[1]))
        two_hundred = ff_class.find_q(ff_class.find_k(twohundred_k[0],
                                                     twohundred_k[1]))
    
        flood_frequencies = np.array([one,two,five,ten,twenty_five,fifty,hundred,two_hundred])
        
        
        pd.set_option('display.max_columns', None)
        
        #logarithmic curve fitting
        r_periods = np.array([1.0101,2,5,10,25,50,100,200]) 
        log_periods = np.log(r_periods)
        curve = np.polyfit(log_periods,flood_frequencies,1)
        a = curve[0]
        b = curve[1]
        
        peak_flows = a*np.log(return_periods) + b
        
        pd.set_option('display.max_columns', None)
        display(peak_flows)
        
        #creates table of return periods and streamflows 
        #final outcome of flood frequency analysis
        flood_df =pd.DataFrame()
        flood_df['Return Periods'] = return_periods
        flood_df['Peak Streamflows'] = peak_flows
        display(flood_df)

        # step 6 - visualization
        
        unit_hydro, unit_baseflow = hv.hydro_vals(flood_duration, interval_hr)
    
        hydrograph = pd.DataFrame()
        
        time_days = [0]
        
        for i in range(0,len(unit_hydro)):
            val = time_days[i] + interval_day
            time_days.append(val)
        
        time_minutes = [0]
        
        for i in range(0,len(unit_hydro)):
            val = time_minutes[i] + interval_min
            time_minutes.append(val)

        hydrograph['Time (days)'] = time_days
        
        hydrograph['Time (minutes)'] = time_minutes
        
        count = 0 
        length = len(flood_df)
        while count < length:
            hydrograph[str(flood_df.iloc[count,0]) +'-year Flood'] = unit_hydro['q/qp'].apply(
            lambda x: (x * flood_df.iloc[count,1]))
            count = count+1
        
        #adds base flow to hydrograph
        j = 2
        row_list = range(0,len(hydrograph)-1,1)
        while j != len(hydrograph.columns):
            for i in row_list:
                hydrograph.iloc[i,j]= hydrograph.iloc[i,j] + base_flow*unit_baseflow.iloc[i,1]
                
            j = j+1
                
        last_row = len(hydrograph) - 1
        hydrograph.iloc[last_row,2:] = base_flow
        
        display(hydrograph)
       
      
        
        # Create a line chart
        fig, ax = plt.subplots()
        
        palette=sns.color_palette(palette='Blues_d')
        
        count1 = 2
        count2 = 0
        length = len(hydrograph.columns)
        while count1 < length:   
            plt.plot(hydrograph['Time (days)'], hydrograph.iloc[:,count1], color = random.choice(palette), label=str(flood_df.iloc[count2,0]) +'-year Flood')
            count1 = count1+1
            count2 = count2+1
                    
        
        # Add title and labels
        plt.title('Hydrograph')
        plt.xlabel('Time (days)')
        plt.ylabel('Flow Rate (cfs)')
        ax.yaxis.set_major_formatter(mpl.ticker.StrMethodFormatter('{x:,.0f}'))
    
        # Display grid
        plt.grid(True)
    
        plt.legend(loc='best')
        plt.tight_layout()
    
        # Show the plot
        plt.show()
    
    #Gumbel Analysis
    else: 

        peak_flow_df = pd.read_csv(INPUT,
                                       header=None,
                                       names=['date', 'peak_streamflow'])
        
            
        peakflow = gb.process_peakflow_data(peak_flow_df)
        
        data, flood_df = gb.gumbel_stats(peakflow,return_periods)
        
        pd.set_option('display.max_columns', None)
        display(flood_df)
        
        
        # step 6 - visualization
        unit_hydro, unit_baseflow = hv.hydro_vals(flood_duration, interval_hr)
    
        hydrograph = pd.DataFrame()
        
        time_days = [0]
        
        for i in range(0,len(unit_hydro)):
            val = time_days[i] + interval_day
            time_days.append(val)
        
        time_minutes = [0]
        
        for i in range(0,len(unit_hydro)):
            val = time_minutes[i] + interval_min
            time_minutes.append(val)

        hydrograph['Time (days)'] = time_days
        
        hydrograph['Time (minutes)'] = time_minutes
        
        count = 0 
        length = len(flood_df)
        while count < length:
            hydrograph[str(flood_df.iloc[count,0]) +'-year Flood'] = unit_hydro['q/qp'].apply(
            lambda x: (x * flood_df.iloc[count,1]))
            count = count+1
        
        #adds base flow to hydrograph
        j = 2
        row_list = range(0,len(hydrograph)-1,1)
        while j != len(hydrograph.columns):
            for i in row_list:
                hydrograph.iloc[i,j]= hydrograph.iloc[i,j] + base_flow*unit_baseflow.iloc[i,1]
                
            j = j+1
                
        last_row = len(hydrograph) - 1
        hydrograph.iloc[last_row,2:] = base_flow
        
        display(hydrograph)
       
    
        # Create a line chart
        fig, ax = plt.subplots()
        
        palette=sns.color_palette(palette='Blues_d')
        
        count1 = 2
        count2 = 0
        length = len(hydrograph.columns)
        while count1 < length:   
            plt.plot(hydrograph['Time (days)'], hydrograph.iloc[:,count1], color = random.choice(palette), label=str(flood_df.iloc[count2,0]) +'-year Flood')
            count1 = count1+1
            count2 = count2+1
                    
        
        # Add title and labels
        plt.title('Hydrograph')
        plt.xlabel('Time (days)')
        plt.ylabel('Flow Rate (cfs)')
        ax.yaxis.set_major_formatter(mpl.ticker.StrMethodFormatter('{x:,.0f}'))
    
        # Display grid
        plt.grid(True)
    
        plt.legend(loc='best')
        plt.tight_layout()
    
        # Show the plot
        plt.show()


if __name__ == '__main__':
    main()
    
    
