'''
Claire Middendorf 

Given a file with return periods and peak streamflows, this code creates a hydrograph of user's specified duration

'''
#import libraries
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
from IPython.display import display
import seaborn as sns
import random

floods = 'floods.csv' #a file with return periods and peak streamflows
flood_duration = 58 #desired duration of flood (days)
base_flow = 50714 #base flow of river
HYDRO = 'hydrograph.csv' #unit hydrograph csv file
return_periods = [1.01,2,5,10,25,50,100] #desired return periods for Gumbel Method

def main():

        unit_hydro = pd.read_csv(HYDRO) 
        interval = flood_duration/5
            
        hydrograph = pd.DataFrame()
            
        hydrograph['t'] = unit_hydro['t/tp'].apply(lambda x: (x * interval)) 
        
        count = 0 
        length = len(floods.index)
        while count < length:
            hydrograph[str(floods.iloc[count,1]) +'-year Flood'] = unit_hydro['q/qp'].apply(
            lambda x: (x * floods.iloc[count,2]))
            count = count+1
        
        pd.set_option('display.max_columns', None)
        display(hydrograph)
        
        
        # Create a line chart
        fig, ax = plt.subplots()
        
        palette=sns.color_palette(palette='Blues_d')
        
        count = 1
        while count < length:   
            plt.plot(hydrograph['t'], hydrograph.iloc[:,count], color = random.choice(palette),linestyle='-', label=str(floods.iloc[count,1]) +'-year Flood')
            count = count+1
                    
            
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
