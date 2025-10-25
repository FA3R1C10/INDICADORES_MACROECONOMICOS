#%% Bibliotecas
from bcb import sgs
import pandas as pd
import matplotlib.pyplot as plt

#%% Construção do dataframe
selic0 = sgs.get(432, "1999-03-05", "2006-03-04")
selic1 = sgs.get(432, "2006-03-05", "2008-03-04")
selic2 = sgs.get(432, "2008-03-05", "2016-03-04")
selic3 = sgs.get(432, "2016-03-05", "2025-10-16")
selic = pd.concat([selic0, selic1, selic2, selic3], axis=0)

ipca0 = sgs.get(433, "1999-03-05", "2006-03-04")
ipca1 = sgs.get(433, "2006-03-05", "2008-03-04")
ipca2 = sgs.get(433, "2008-03-05", "2016-03-04")
ipca3 = sgs.get(433, "2016-03-05", "2025-10-16")
ipca = pd.concat([ipca0, ipca1, ipca2, ipca3], axis = 0)

#%% Refinar os dataframes
selic = selic[selic.index.isin(ipca.index)]

ipca = ipca.iloc[5:,:]
selic = selic.iloc[:-5,:]
ipca = ipca.reset_index(drop=True)
selic = selic.reset_index(drop=True)
df_Selic_IPCA = pd.concat([selic, ipca], axis = 1)
df_Selic_IPCA = df_Selic_IPCA.rename(columns={"432": "Selic", "433": "IPCA"})

# %%
plt.figure(figsize = (16,8))
plt.scatter(x = df_Selic_IPCA["IPCA"], y = df_Selic_IPCA["Selic"])

plt.show()
# %%
