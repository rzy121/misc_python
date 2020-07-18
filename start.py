import pandas as pd
import numpy as np
from os import environ as env

# Pandas options
pd.options.display.max_columns = 30

# Visualization
import matplotlib.pyplot as plt
import seaborn as sns
try:
    from jupyterthemes import jtplot
    jtplot.style(theme = 'oceans16')
except ImportError:
    plt.style.use('bmh')

# If in ipython, load autoreload extension & run plots inline
if 'ipython' in globals():
    print('\nWelcome to IPython!')
    ipython.magic('load_ext autoreload')
    ipython.magic('autoreload 2')
    ipython.magic('matplotlib inline')

print('Usual libraries have been loaded.')
