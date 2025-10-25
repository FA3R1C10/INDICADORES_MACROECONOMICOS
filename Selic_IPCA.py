#%%
from bcb import sgs
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import datetime as dt

#%%
selic = sgs.get("432", "2018-01-01", dt.date.today()) #importa base selic
ipca = sgs.get("433", "2018-01-01", dt.date.today()) #importa ipca mensal
ipca_12m = sgs.get("13522", "2018-01-01", dt.date.today()) #importa ipca 12 meses
ipca_nucleo = sgs.get("4466", "2017-01-01", dt.date.today()) #importa ipca núcleo mensal com um ano a mais para calcular 12 meses desde o início
ipca_nucleo_12m = ipca_nucleo.rolling(window=12).apply(lambda x: (np.prod((x/100)+1)-1)*100,raw=True).dropna() #calcula ipca núcleo 12 meses
ipca_nucleo_12m = ipca_nucleo_12m[ipca_nucleo_12m.index >= ipca.index.min()] #inicia a base do ipca núcleo 12 meses para o mesmo período do ipca mensal
#ipca_nucleo = ipca_nucleo[ipca_nucleo.index >= ipca.index.min()] #inicia a base ipca núcleo mensal para o mesmo período do ipca mensal excluindo os anteriores para plotar gráfico

# %%
plt.figure(figsize=(16,8))

plt.plot(selic, label='Selic', color='black')
plt.plot(ipca_12m, label="IPCA 12m", color="blue")
plt.plot(ipca_nucleo_12m, label= "Núcleo IPCA 12m", color= "darkblue")


plt.bar(x=ipca.index, height= ipca.iloc[:,0], width=20, label="IPCA Mensal", color="blue")
#plt.bar(x= ipca_nucleo.index, height= ipca_nucleo.iloc[:,0], width=20,  label="Núcleo IPCA Mensal", color="darkblue")

plt.annotate(f"{ipca_12m.iloc[-1,0]:.2f}%", xy = (ipca_12m.index[-1], ipca_12m.iloc[-1,0] + 0.3), fontsize=10, color="blue", ha="left", va="center")
plt.annotate(f"{ipca_nucleo_12m.iloc[-1,0]:.2f}%", xy = (ipca_nucleo_12m.index[-1], ipca_nucleo_12m.iloc[-1,0]-0.2), fontsize=10, color= "darkblue", ha="left", va="center")
plt.annotate(f"{selic.iloc[-1,0]:.2f}%", xy = (selic.index[-1], selic.iloc[-1,0] - 0.2), fontsize=10, color= "black", ha="left", va="center")
plt.annotate(f"{ipca.iloc[-1,0]:.2f}%", xy = (ipca.index[-1], ipca.iloc[-1,0] + 0.2), fontsize=10, color="blue", ha="left", va="center")

plt.annotate("Fonte: Banco Central do Brasil / IBGE", xy = (0, -0.1), xycoords= 'axes fraction', fontsize=10, color='gray', ha="left", va="center")
plt.annotate("Fabricio Orlandin, CFP®", xy=(1, -0.1), xycoords= "axes fraction", fontsize=10, color="gray", ha="right", va="center")

plt.axhline(y=1.5, color='gray', linestyle='--', linewidth=1)  # Linha em 1,5%
plt.axhline(y=3.0, color='black', linestyle='-', linewidth=1)  # Linha em 3%
plt.axhline(y=4.5, color='gray', linestyle='--', linewidth=1)  # Linha em 4,5%

plt.text(x = ipca.index[-2], y= 3.1, s="Meta 3%", fontsize= 8, color= "black")
plt.text(x = ipca.index[-4], y= 4.2, s="Banda Superior 4,5%", fontsize= 8, color= "gray")
plt.text(x = ipca.index[-3], y= 1.6, s="Banda Inferior 3%", fontsize= 8, color= "gray")

plt.legend()
plt.show()

# %%
