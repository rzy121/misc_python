import pandas as pd
import numpy as np
import os
from dotenv import load_dotenv
load_dotenv()

# Pandas optionspd.options.display.max_columns = 30
pd.set_option('display.max_columns', None)

# Visualization
import matplotlib.pyplot as plt
import seaborn as sns
plt.style.use('bmh')
sns.set(style='darkgrid')

# If in ipython, load autoreload extension & run plots inline
if 'ipython' in globals():
    print('\nWelcome to IPython!')
    ipython.magic('load_ext autoreload')
    ipython.magic('autoreload 2')
    ipython.magic('matplotlib inline')

print('Usual libraries have been loaded.')
