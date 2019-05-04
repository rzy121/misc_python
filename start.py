import pandas as pd
import numpy as np

# Pandas options
pd.options.display.max_columns = 30

# Visualization
import matplotlib.pyplot as plt
import seaborn as sns
plt.style.use('bmh')

# If in ipython, load autoreload extension & run plots inline
if 'ipython' in globals():
    print('\nWelcome to IPython!')
    ipython.magic('load_ext autoreload')
    ipython.magic('autoreload 2')
    ipython.magic('matplotlib inline')

print('Usual libraries have been loaded.')
