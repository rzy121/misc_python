import pandas as pd
import numpy as np
import os
import time
from dotenv import load_dotenv
load_dotenv()

# Pandas optionspd.options.display.max_columns = 30
pd.set_option('display.max_columns', None)

# Visualization
import matplotlib.pyplot as plt
import seaborn as sns


sns.set_theme(style='darkgrid')
plt.style.use('fivethirtyeight')

# Auto-enable inline plotting

try:
    from IPython import get_ipython
    ipython = get_ipython()
    if ipython:
        ipython.run_line_magic('matplotlib', 'inline')
        ipython.run_line_magic('load_ext', 'autoreload')
        ipython.run_line_magic('autoreload', '2')
except Exception as e:
    pass  # You can log this if needed

def timer(func):
    """decorator to time any function."""
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"⏱️ {func.__name__} ran in {time.time() - start:.3f} sec")
        return result
    return wrapper

class Env:
    """Convenient access to environment variables."""
    def get(self, key, default=None):
        value = os.getenv(key, default)
        print(f"🔐 {key} = {value}")
        return value

env = Env()


# --- Confirmation Flag ---
__startup_loaded__ = True