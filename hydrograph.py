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
INVERSE = 'reverse.csv'


def main():
    
        flood_df = pd.read_csv(floods,
                                   header=None,
                                   names=['Returmn Period', 'peak_streamflow'])

        unit_hydro = pd.read_csv(HYDRO)
        inverse = pd.read_csv(INVERSE, header = None, names = ['qp'])
        inverse['base_flow_adds'] = inverse['qp'].apply(lambda x: x*base_flow)
    
        hydrograph = pd.DataFrame()
        
        interval = flood_duration/5
        hydrograph['t'] = unit_hydro['t/tp'].apply(lambda x: (x * interval))
        
        count = 0 
        length = len(flood_df)
        while count < length:
            hydrograph[str(flood_df.iloc[count,0]) +'-year Flood'] = unit_hydro['q/qp'].apply(
            lambda x: (x * flood_df.iloc[count,1]))
            count = count+1
        
        #adds base flow to hydrograph
        j = 1
        row_list = range(0,len(hydrograph)-1,1)
        while j != len(hydrograph.columns):
            for i in row_list:
                hydrograph.iloc[i,j]= hydrograph.iloc[i,j] + base_flow*inverse.iloc[i,0]
                
            j = j+1
                
        last_row = len(hydrograph) - 1
        hydrograph.iloc[last_row,1:] = base_flow
        
        display(hydrograph)
        
        # Create a line chart
        fig, ax = plt.subplots()
        
        palette=sns.color_palette(palette='Blues_d')
        
        count = 0
        while count < length:   
            plt.plot(hydrograph['t'], hydrograph.iloc[:,count+1], color = random.choice(palette),linestyle='-', label=str(flood_df.iloc[count,0]) +'-year Flood')
            count = count+1
                    
            
         # Add title and labels
        plt.title('Hydrograph')
        plt.xlabel('Time (Days)')
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
