#%%
import pandas_datareader.data as pdr
import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt
import numpy as np
#%%
# Importar base PCE
pce_df = pdr.DataReader("PCECTPI", "fred", "2019-01-01", dt.datetime.today())
print(pce_df)
# Calcular a variação mensal
pce_var_df = pce_df.pct_change().dropna()
pce_var12_df = pce_var_df.rolling(window=12).apply(lambda x: (np.prod(x+1)-1)*100, raw=True).dropna()
print(pce_var12_df)

#%%
plt.figure(figsize=(15,7))
plt.plot(pce_var12_df, label= "PCE 12 meses", color= "black")
plt.legend()
plt.show()


# %%
