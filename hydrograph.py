'''
Creates a hydrograph of user's specified duration

'''


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
