import os
import numpy as np
import pandas as pd

def add_total_value_counts(df, df_total, cols=[]):
    for c in cols:
        vc = df_total[c].value_counts()
        df['{}_FREQ'.format(c)] = df[c].map(vc)
    return df
    