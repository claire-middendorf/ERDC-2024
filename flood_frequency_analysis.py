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

else: 
    



