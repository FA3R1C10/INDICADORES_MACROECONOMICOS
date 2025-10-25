from bcb import sgs
import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt

taxa_desocupacao = sgs.get("24369", start="2010-01-01", end=dt.datetime.today())
ipca = sgs.get("433", start="2010-01-01", end=dt.datetime.today())

plt.figure(figsize=(16,8))
plt.plot(taxa_desocupacao, label="Taxa de Desemprego (%)", color="gray")
plt.plot(ipca, label="IPCA (%)", color="red")
plt.legend()
plt.grid(True)
plt.annotate("fonte: Banco Central do Brasil / CAGED", xy=(0, -0.1), xycoords="axes fraction", fontsize=10, color="lightgray", ha="left", va="center")
plt.annotate("Fabricio Orlandin, CFP®", xy=(1, -0.1), xycoords="axes fraction", fontsize=10, color="lightgray", ha="right", va="center")
plt.show()