# -*- coding: utf-8 -*-

"""
Claire Middendorf

    Process Log-Pearson Type III flood frequency analysis

"""

# import libraries
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
import log-pearson-analysis as lp
import k_table as kdata
import gumbel-analysis as gb

# globals
INPUT = './src/jc_station.csv'
REGIONAL_SKEW = -0.3
T_INT = 2

method = input("Which flood frequency analysis? Write 1 for Log-Pearson Type III or 2 for Gumbel: ")

def main():

if method = 1:
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
    
        flood_frequencies = {
            "One-Year Flood": [one],
            "Two-Year Flood": [two],
            "Five-Year Flood": [five],
            "Ten-Year Flood": [ten],
            "Twenty-five-Year Flood": [twenty_five],
            "Fifty-Year Flood": [fifty],
            "Hundred-Year Flood": [hundred],
            "Two Hundred-Year Flood": [two_hundred]
        }
        ff_results = pd.DataFrame(flood_frequencies)
    
        print(ff_results)

        # step 6 - visualization
        unit_hydro = pd.read_csv(HYDRO)
        interval = T_INT
    
        hydrograph = pd.DataFrame()
    
        hydrograph['t'] = unit_hydro['t/tp'].apply(lambda x: (x * interval))
        hydrograph['1-year'] = unit_hydro['q/qp'].apply(
            lambda x: (x * ff_results['One-Year Flood']))
        hydrograph['2-year'] = unit_hydro['q/qp'].apply(
            lambda x: (x * ff_results['Two-Year Flood']))
        hydrograph['5-year'] = unit_hydro['q/qp'].apply(
            lambda x: (x * ff_results['Five-Year Flood']))
        hydrograph['10-year'] = unit_hydro['q/qp'].apply(
            lambda x: (x * ff_results['Ten-Year Flood']))
        hydrograph['25-year'] = unit_hydro['q/qp'].apply(
            lambda x: (x * ff_results['Twenty-five-Year Flood']))
        hydrograph['50-year'] = unit_hydro['q/qp'].apply(
            lambda x: (x * ff_results['Fifty-Year Flood']))
        hydrograph['100-year'] = unit_hydro['q/qp'].apply(
            lambda x: (x * ff_results['Hundred-Year Flood']))
        hydrograph['200-year'] = unit_hydro['q/qp'].apply(
            lambda x: (x * ff_results['Two Hundred-Year Flood']))
    
        # Create a line chart
        fig, ax = plt.subplots()
        plt.plot(hydrograph['t'], hydrograph['1-year'], linestyle='-', label="1-year")
        plt.plot(hydrograph['t'], hydrograph['2-year'], linestyle='-', label="2-year")
        plt.plot(hydrograph['t'], hydrograph['5-year'], linestyle='-', label="5-year")
        plt.plot(hydrograph['t'], hydrograph['10-year'], linestyle='-', label="10-year")
        plt.plot(hydrograph['t'], hydrograph['25-year'], linestyle='-', label="25-year")
        plt.plot(hydrograph['t'], hydrograph['50-year'], linestyle='-', label="50-year")
        plt.plot(hydrograph['t'], hydrograph['100-year'], linestyle='-', label="100-year")
        plt.plot(hydrograph['t'], hydrograph['200-year'], linestyle='-', label="200-year")
    
        # Add title and labels
        plt.title('Hydrograph')
        plt.xlabel('Time (hours)')
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
        
        return_periods = input("List the return periods for the desired peak streamflows: ")
        return_periods = return_periods.split(',')
        count = 0
        for i in return_periods:
            return_periods[count] = float(i)
            count = count + 1
            
        peakflow = process_peakflow_data(peak_flow_df)
        
        data, floods = gumbel_stats(peakflow)
        
        # step 6 - visualization
        unit_hydro = pd.read_csv('/Users/clairemiddendorf/Desktop/USACE Internship/flood_python/hydrograph.csv') 
        interval = 2
            
        hydrograph = pd.DataFrame()
            
        hydrograph['t'] = unit_hydro['t/tp'].apply(lambda x: (x * interval)) 
        
        count = 0 
        length = len(floods.index)
        while count < length:
            hydrograph[str(floods.loc[count,'Return Periods']) +'-year Flood'] = unit_hydro['q/qp'].apply(
            lambda x: (x * floods.loc[count,'Peak Streamflow (cfs)']))
            count = count+1
                
        # Create a line chart
        fig, ax = plt.subplots()
        
        count = 1
        length2 = len(hydrograph.columns)
        while count < length:   
            plt.plot(hydrograph['t'], hydrograph.iloc[:,count], linestyle='-', label=str(floods.loc[count,'Return Periods']) +'-year Flood')
            count = count+1
                    
            
        # Add title and labels
        plt.title('Hydrograph')
        plt.xlabel('Time (hours)')
        plt.ylabel('Flow Rate (cfs)')
        ax.yaxis.set_major_formatter(mpl.ticker.StrMethodFormatter('{x:,.0f}'))
            
        # Display grid
        plt.grid(True)
            
        plt.legend(loc='best')
        plt.tight_layout()
            
        # Show the plot
        plt.show()


