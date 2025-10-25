#%%
import pandas_datareader.data as pdr 
import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt

#%% Importar base juros 10y e dxy
treasury10y_df = pdr.DataReader('DGS10', 'fred', '2024-01-20', dt.date.today()).dropna()
treasury10y_df = treasury10y_df / treasury10y_df.iloc[0]
break_even_inflation_rate = pdr.DataReader('T10YIE', 'fred', '2024-01-20', dt.date.today()).dropna()
break_even_inflation_rate = break_even_inflation_rate / break_even_inflation_rate.iloc[0]
# %%
plt.figure(figsize = (12,6))
plt.plot(treasury10y_df, label='Juros 10 anos', color='blue')
plt.plot(break_even_inflation_rate, label='Break-Even Inflation Rate', color='red')
plt.legend()
plt.text(treasury10y_df.index[-1], plt.ylim()[0] - 0.03, 'Fabricio Orlandin, CFP®', fontsize=15, ha='right', color='slategray')
plt.show()
# %%
