#%% Importa bibliotecas
import pandas_datareader as pdr
import matplotlib.pyplot as plt
import datetime as dt
import numpy as np

#%% Coleta dados PCE, CPI e FED rate
unemployment = pdr.DataReader("UNRATE", "fred", "2019-01-01", dt.datetime.today())
pce_nominal = pdr.DataReader("PCEPILFE", "fred", "2019-01-01", dt.datetime.today())
pce = pce_nominal.pct_change().dropna() * 100
pce_12m = pce.rolling(window=12).apply(lambda x: (np.prod((x/100) + 1) -1) *100, raw = True).dropna()
cpi_nominal = pdr.DataReader("CPIAUCSL", "fred", "2019-01-01", dt.datetime.today())
cpi = cpi_nominal.pct_change().dropna() * 100
cpi_12m = cpi.rolling(window=12).apply(lambda x: (np.prod((x/100) + 1) - 1) * 100, raw=True).dropna()
cpi = cpi[cpi.index >= cpi_12m.index.min()]
fed = pdr.DataReader("FEDFUNDS", "fred", "2019-01-01", dt.datetime.today())
pce = pce[pce.index >= pce_12m.index[0]]
fed = fed[fed.index >= pce_12m.index[0]]
unemployment = unemployment.loc[unemployment.index >= pce_12m.index[0]]
# %% plotar gráficos
plt.figure(figsize=(16,8))
plt.plot(fed, color="black", label="FED Rates")
plt.plot(cpi_12m, color="blue", label="CPI 12m")
plt.plot(pce_12m, color="darkblue", label="PCE 12m")
plt.bar(x=unemployment.index, height=unemployment.iloc[:,0], width=80, label= "Unemployment Rate", color= "lightgray")
plt.bar(x=pce.index, height=pce.iloc[:,0], width=20, label="PCE monthly", color="darkblue")
plt.axhline(y = 2, color = "red", linestyle = "-", linewidth = 0.7)
plt.annotate(f"{fed.iloc[-1,0]:.2f}%", xy=(fed.index[-1], fed.iloc[-1,0] + 0.3), ha="right", va="center", color="black")
plt.annotate(f"{cpi_12m.iloc[-1, 0]:.1f}%", xy=(cpi_12m.index[-1], cpi_12m.iloc[-1,0] - 0.2), ha="left", va="center", color="blue", fontsize=10)
plt.annotate(f"{pce_12m.iloc[-1,0]:.1f}%", xy=(pce_12m.index[-1], pce_12m.iloc[-1,0] + 0.3), ha="right", va="center", color="darkblue", fontsize=10)
plt.annotate(f"{pce.iloc[-1,0]:.1f}%", xy=(pce.index[-1], pce.iloc[-1,0] + 0.2), ha="left", va="center", color="blue", fontsize=10)
plt.annotate(f"{unemployment.iloc[-1,0]:.1f}%", xy=(unemployment.index[-1], unemployment.iloc[-1,0] + 0.6), ha="left", va="center", color="gray", fontsize=10)
plt.text(x= pce.index[-2], y = 1.7, s= "Target 2%", color= "red", fontsize= 8)
plt.annotate("Fabricio Orlandin, CFP®", xy=(1, -0.1), xycoords="axes fraction", fontsize=10, color="gray", ha="right", va="center")
plt.annotate("fonte: Federal Reserve Bank of Saint Louis", xy=(0, -0.1), xycoords="axes fraction", fontsize=10, color="gray", ha="left", va="center")
plt.title("Inflação, Juros e Desemprego - US", loc= "left")
plt.legend()
plt.show()

# %%
