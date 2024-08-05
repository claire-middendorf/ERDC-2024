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

floods = '/Users/clairemiddendorf/Desktop/repos/ERDC-2024-main/floods.csv' #a file with return periods and peak streamflows
flood_duration = 41.2 #desired duration of flood (days)
base_flow = 50714 #base flow of river
HYDRO = 'hydrograph.csv' #unit hydrograph csv file
INVERSE = 'reverse.csv'


def main():
    
        flood_df = pd.read_csv(floods,
                                   header=None,
                                   names=['Returmn Period', 'peak_streamflow'])
                                  
        
        #creating unit hydrograph from flood duration, intervals of 15 minutes
        
        num_intervals = round(flood_duration*24*4)
        
        time_peak = flood_duration/2.67
        
        rising_int = round(num_intervals/2.67)
        falling_int = round(num_intervals-rising_int)
        
        rising_slope = []
        falling_slope = []
        x=0
        while x < len(flood_df):
            
            slope_1 = flood_df.iloc[x,1]/time_peak
            rising_slope.append(slope_1)
            
            slope_2=-(flood_df.iloc[x,1])/(flood_duration-time_peak)
            falling_slope.append(slope_2)
            
            x=x+1
            
        falling_intercept = []
        x=0
        while x < len(flood_df):
            
            falling_intercept.append(-(falling_slope[x] * flood_duration))
            x=x+1
        
        t = [0]
        x=1
        while x < num_intervals:
            t.append(0.01042*x)
            x=x+1
        
        hydrograph = pd.DataFrame({'t':t})   
        
        
        #adds base flow to hydrograph
        j = 0
        brise_slope = (-base_flow/time_peak)
        bfall_slope = (base_flow/(flood_duration-time_peak))
        bfall_intercept = base_flow - (bfall_slope*flood_duration)
        baseflow_rising = []
        baseflow_falling = []
        
        while j < rising_int:
            
            value = t[j] * brise_slope + base_flow
            baseflow_rising.append(value)
                
            j = j+1
            
        j = 0
        while j < falling_int:
            
            value = t[j + rising_int] * bfall_slope + bfall_intercept
            baseflow_falling.append(value)
            j= j+1
        
        baseflow_limbs = baseflow_rising + baseflow_falling
        
        
        count = 0 
        length = len(flood_df)
        while count < length:
            
            rising_limb=[]
            y = 0
            while y < rising_int:
                flow = hydrograph['t'][y]*rising_slope[count]
                flow = flow + baseflow_limbs[y]
                rising_limb.append(flow)
                y= y+1
                
            falling_limb=[]
            z=0
            while z<falling_int:
                flow = (hydrograph['t'][z+rising_int]*falling_slope[count] +falling_intercept[count])
                flow = flow + baseflow_limbs[z+rising_int]
                falling_limb.append(flow)
                z=z+1
                
            limbs = rising_limb + falling_limb 
            
            hydrograph[str(flood_df.iloc[count,0]) +'-year Flood'] = limbs
            count = count+1
                              
        
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