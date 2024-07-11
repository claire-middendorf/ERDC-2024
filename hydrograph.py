'''
Given a file with return periods and peak streamflows, this code creates a hydrograph of user's specified duration

'''

HYDRO = 'hydrograph.csv'
INT = 2
floods = 'floods.csv' #a file with return periods and peak streamflows

        unit_hydro = pd.read_csv(HYDRO) 
        interval = INT
            
        hydrograph = pd.DataFrame()
            
        hydrograph['t'] = unit_hydro['t/tp'].apply(lambda x: (x * interval)) 
        
        count = 0 
        length = len(floods.index)
        while count < length:
            hydrograph[str(floods.iloc[count,1]) +'-year Flood'] = unit_hydro['q/qp'].apply(
            lambda x: (x * floods.iloc[count,2]))
            count = count+1
                
        # Create a line chart
        fig, ax = plt.subplots()
        
        count = 1
        length2 = len(hydrograph.columns)
        while count < length:   
            plt.plot(hydrograph['t'], hydrograph.iloc[:,count], linestyle='-', label=str(floods.iloc[count,1]) +'-year Flood')
            count = count+1
                    
            
        # Add title and labels
        plt.title('Hydrograph')
        plt.xlabel('Time')
        plt.ylabel('Flow Rate (cfs)')
        ax.yaxis.set_major_formatter(mpl.ticker.StrMethodFormatter('{x:,.0f}'))
            
        # Display grid
        plt.grid(True)
            
        plt.legend(loc='best')
        plt.tight_layout()
            
        # Show the plot
        plt.show()
