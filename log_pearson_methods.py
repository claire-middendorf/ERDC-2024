# -*- coding: utf-8 -*-

"""
Claire Middendorf

    Classes and methods to generate flood frequency analysis.

    Sources:
        https://peps.python.org/pep-0008/
        https://peps.python.org/pep-0257/
"""

# import
import numpy as np
import pandas as pd



def process_peakflow_data(data=pd.DataFrame) -> pd.DataFrame:
    """process peakflow dataframe for analysis"""

    peakflow = data.sort_values(by='peak_streamflow', ascending=False)
    n = len(peakflow)
    rank = pd.Series(range(1, n+1, 1))
    peakflow.insert(loc=0, column='rank', value=rank, allow_duplicates=True)
    peakflow.reset_index(drop=True, inplace=True)

    return peakflow


def log_pearson_stats(data=pd.DataFrame):
    """add additional statistics; returns two structures"""

    n = len(data)

    # log values and averages
    data['Q_log10'] = np.log10(data['peak_streamflow'])
    avg_Q = data["peak_streamflow"].mean()
    avg_logQ = data['Q_log10'].mean()

    # required calculations as new columns
    data['(log Q - avg(logQ))^2'] = data['Q_log10'].apply(
        lambda x: (x - avg_logQ) ** 2)
    data['(log Q - avg(logQ))^3'] = data['Q_log10'].apply(
        lambda x: (x - avg_logQ) ** 3)
    data['Return Period (Tr)'] = data['rank'].apply(lambda x: (n + 1) / x)
    data['Exceedance Probability'] = data['Return Period (Tr)'].apply(
        lambda x: 1 / x)

    # statistics
    sum_squared = sum(data['(log Q - avg(logQ))^2'])
    sum_cubed = sum(data['(log Q - avg(logQ))^3'])
    stdev = np.std(data['Q_log10'], ddof=1)
    variance = np.var(data['Q_log10'])

    # Calculations of skew coefficients
    skew_coeff = data['Q_log10'].skew()

    peakflow_stats = {
        'avg_Q': avg_Q,
        'avg_logQ': avg_logQ,
        'sum_squared': sum_squared,
        'sum_cubed': sum_cubed,
        'stdev': stdev,
        'variance': variance,
        'skew_coeff': skew_coeff,
    }

    return data, peakflow_stats


def process_coefficients(skew_coeff: float, regional_skew: float,
                         n: int) -> dict:
    """generate related coefficient data"""

    var_reg_skew = 0.302

    if skew_coeff <= 0.9:
        a = -0.33 + 0.08 * abs(skew_coeff)
    else:
        a = -0.52 + 0.3 * abs(skew_coeff)

    if skew_coeff <= 1.5:
        b = 0.94 - 0.26 * abs(skew_coeff)
    else:
        b = 0.55

    # variance of skew
    var_station_skew = 10 ** (a - b * np.log10(n / 10))

    # weighting factor
    w = var_reg_skew / (var_station_skew + var_reg_skew)
    weighted_skew = w * skew_coeff + (1 - w) * regional_skew

    # Uses the Frequency Factors K for log-Pearson Type III Distributions
    # Haan,1977,Table 7.7, to input the following values
    k = round(skew_coeff, 1)

    if k < 0:
        if k > skew_coeff:
            k1 = k
            k2 = round(k - 0.1, 1)
        else:
            k2 = k
            k1 = round(k + 0.1, 1)

    if k >= 0:
        if k > skew_coeff:
            k1 = k
            k2 = round(k - 0.1, 1)
        else:
            k2 = k
            k1 = round(k + 0.1, 1)

    coeff_dict = {
        'var_reg_skew': var_reg_skew,
        'a': a,
        'b': b,
        'var_station_skew': var_station_skew,
        'w': w,
        'weighted_skew': weighted_skew,
        'k': k,
        'k1': k1,
        'k2': k2,
    }

    return coeff_dict


class FrequencyFactors:
    def __init__(self, k1, k2, weighted_skew, avg_logQ, stdev):
        self.k1 = k1
        self.k2 = k2
        self.weighted_skew = weighted_skew
        self.avg_logQ = avg_logQ
        self.stdev = stdev

    def find_k(self, above, below):
        slope = (below - above) / (self.k2 - self.k1)
        k = slope * (self.weighted_skew - self.k1) + above
        return k

    def find_q(self, k_value):
        log_q = self.avg_logQ + (k_value * self.stdev)
        q_value = 10 ** log_q
        return q_value


