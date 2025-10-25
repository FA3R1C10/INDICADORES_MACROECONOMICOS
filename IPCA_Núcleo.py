#%% Importando bibliotecas
from bcb import sgs
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import datetime as dt

#%% Criando dataframe IPCA e Núcleo IPCA
ipca = sgs.get("433", "2019-01-01", dt.datetime.today())
ipca_12m = sgs.get("13522", "2019-01-01", dt.datetime.today())
selic = sgs.get("432", "2019-01-01", dt.datetime.today())
nucleo = sgs.get("28751", "2019-01-01", dt.datetime.today())
nucleo12m = nucleo.rolling(window=12).apply(lambda x:(np.prod(1 + x / 100) - 1) * 100, raw = True).dropna()
desemprego = sgs.get("24369", "2019-01-01", dt.datetime.today())
ipca_12m = ipca_12m.loc[ipca_12m.index >= nucleo12m.index[0]]
selic = selic.loc[selic.index >= nucleo12m.index[0]]
ipca = ipca.loc[ipca.index >= nucleo12m.index[0]]
desemprego = desemprego.loc[desemprego.index >= nucleo12m.index[0]]
# %% Plotar Gráfico
plt.figure(figsize=(16,8))
plt.bar(x = desemprego.index, height=desemprego.iloc[:,0], width=80, color = "lightgray", label = "Índice de Desemprego")
plt.bar(x = ipca.index, height=ipca.iloc[:,0], width=20, color = "darkblue", label = "IPCA mensal")
plt.plot(ipca_12m, label = "IPCA_12m", color = "darkblue")
plt.plot(selic, label = "Selic", color = "black")
plt.plot(nucleo12m, label = "Núcleo IPCA", color = "blue")
plt.annotate("fonte: IBGE via Banco Central do Brasil", xy = (0, -0.1), xycoords = "axes fraction", color = "black", fontsize = 10, ha = "left", va = "center")
plt.annotate("Fabricio Orlandin, CFP®", xy = (1, -0.1), xycoords = "axes fraction", color = "black", fontsize = 10, ha = "right", va = "center")
plt.annotate(f"{ipca.iloc[-1,0]}%", xy = (ipca.index[-1], ipca.iloc[-1,0] - 0.8), color = "darkblue", fontsize = 8, ha = "left", va = "top")
plt.annotate(f"{ipca.iloc[-2,0]}%", xy = (ipca.index[-2], ipca.iloc[-2,0] - 0.4), color = "darkblue", fontsize = 8, ha = "right", va = "bottom")
plt.annotate(f"{ipca.loc["2024-09-01"].iloc[0]}%", xy = (ipca.loc["2024-09-01"].name, ipca.loc["2024-09-01"].iloc[0] - 0.8), color = "darkblue", fontsize = 8, ha = "center", va = "top")
plt.annotate(f"{ipca_12m.iloc[-1,0]}%", xy = (ipca_12m.index[-1], ipca_12m.iloc[-1,0] + 0.2), color = "darkblue", fontsize = 8, ha = "center", va = "bottom")
plt.annotate(f"{nucleo12m.iloc[-1,0]:.2f}%", xy = (nucleo12m.index[-1], nucleo12m.iloc[-1,0] - 0.2), color = "blue", fontsize = 8, ha = "center", va = "top")
plt.annotate(f"{selic.iloc[-1,0]}%", xy = (selic.index[-1], selic.iloc[-1,0] - 0.2), color = "black", fontsize = 8, ha = "center", va = "top")
plt.annotate(f"{desemprego.iloc[-1,0]}%", xy = (desemprego.index[-1], desemprego.iloc[-1,0] + 0.3), color = "gray", fontsize = 8, ha = "left", va = "bottom")
plt.axhline(y = ipca.iloc[-1,0], linestyle = "--", color = "darkblue")
plt.axhline(y = 4.5, linestyle = "--", color = "gray")
plt.axhline(y = 3.0, linestyle = "--", color = "gray")
plt.axhline(y = 1.5, linestyle = "--", color = "gray")
plt.annotate("teto da meta 4,5%", xy = (ipca.index[-1], 4.5 - 0.3), color = "gray", fontsize = 8, ha = "center", va = "bottom")
plt.annotate("meta 3%", xy = (ipca.index[-1], 3 + 0.1), color = "gray", fontsize = 8, ha = "center", va = "bottom")
plt.annotate("piso da meta 1,5%", xy = (ipca.index[-1], 1.5 + 0.1), color = "gray", fontsize = 8, ha = "center", va = "bottom")
plt.title("Inflação, Juros e Desemprego - BR", loc = "left")
plt.legend()
plt.show()
# %%
print(nucleo)
print(nucleo12m)
# %%
difusao = sgs.get(21379, "2019-01-01", dt.datetime.today())
plt.figure(figsize=(16,8))
plt.plot(difusao, label = "IPCA_Difusão", color = "darkblue")
plt.annotate("fonte: IBGE via Banco Central do Brasil", xy = (0, -0.1), xycoords = "axes fraction", color = "black", fontsize = 10, ha = "left", va = "center")
plt.annotate("Fabricio Orlandin, CFP®", xy = (1, -0.1), xycoords = "axes fraction", color = "black", fontsize = 10, ha = "right", va = "center")
plt.annotate(f"{difusao.iloc[-1,0]}", xy = (difusao.index[-1], difusao.iloc[-1,0] - 0.1), color = "darkblue", fontsize = 8, ha = "left", va = "top")
plt.annotate(f"{difusao.iloc[-2,0]}", xy = (difusao.index[-2], difusao.iloc[-2,0] + 0.1), color = "darkblue", fontsize = 8, ha = "left", va = "bottom")
plt.title("Difusão do IPCA", loc = "left")
plt.legend()
plt.show()
# %%
