#%% Importando bibliotecas
from bcb import sgs
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import datetime as dt
#%% Criando dataframe IPCA e Núcleo IPCA
ipca_df = sgs.get('433', start= '2020-01-01', end= dt.date.today())
ipca_df = ipca_df.rolling(window=12).apply(lambda x: ((x / 100 + 1).prod() - 1) * 100).dropna()
food_beverages_df = sgs.get('1635', start= '2020-01-01', end= dt.date.today())
food_beverages_df = food_beverages_df.rolling(window=12).apply(lambda x: ((x / 100 + 1).prod() - 1) * 100).dropna()
housing_df = sgs.get('1636', start= '2020-01-01', end= dt.date.today())
housing_df = housing_df.rolling(window=12).apply(lambda x: ((x / 100 + 1).prod() - 1) * 100).dropna()
domestic_goods_df = sgs.get('1637', start= '2020-01-01', end= dt.date.today())
domestic_goods_df = domestic_goods_df.rolling(window=12).apply(lambda x: ((x / 100 + 1).prod() - 1) * 100).dropna()
clothing_df = sgs.get('1638', start= '2020-01-01', end= dt.date.today())
clothing_df = clothing_df.rolling(window=12).apply(lambda x: ((x / 100 + 1).prod() - 1) * 100).dropna()
transport_df = sgs.get('1639', start= '2020-01-01', end= dt.date.today())
transport_df = transport_df.rolling(window=12).apply(lambda x: ((x / 100 + 1).prod() - 1) * 100).dropna()
communication_df = sgs.get('1640', start= '2020-01-01', end= dt.date.today())
communication_df = communication_df.rolling(window=12).apply(lambda x: ((x / 100 + 1).prod() - 1) * 100).dropna()
health_personal_care_df = sgs.get('1641', start= '2020-01-01', end= dt.date.today())
health_personal_care_df = health_personal_care_df.rolling(window=12).apply(lambda x: ((x / 100 + 1).prod() - 1) * 100).dropna()
personal_expenditures_df = sgs.get('1642', start= '2020-01-01', end= dt.date.today())
personal_expenditures_df = personal_expenditures_df.rolling(window=12).apply(lambda x: ((x / 100 + 1).prod() - 1) * 100).dropna()
education_df = sgs.get('1643', start= '2020-01-01', end= dt.date.today())
education_df = education_df.rolling(window=12).apply(lambda x: ((x / 100 + 1).prod() - 1) * 100).dropna()
nucleo_df = sgs.get('11426', start = '2020-01-01', end= dt.date.today())
nucleo_df = nucleo_df.rolling(window=12).apply(lambda x: ((x / 100 + 1).prod() - 1) * 100).dropna()
# %% Criando gráfico com IPCA e Núcleo
plt.figure(figsize=(20,10))
plt.plot(ipca_df, label='IPCA_12m', color='blue')
plt.plot(nucleo_df, label='Núcleo IPCA', color='black')
plt.plot(food_beverages_df, label='Alimentação e Bebidas', color='orange')
plt.plot(housing_df, label='Habitação', color='green')
plt.plot(domestic_goods_df, label='Artigos de Residência', color='purple')
plt.plot(clothing_df, label='Vestuário', color='brown')
plt.plot(transport_df, label='Transportes', color='red')
plt.plot(communication_df, label='Comunicação', color='pink')
plt.plot(health_personal_care_df, label='Saúde e Cuidados Pessoais', color='cyan')
plt.plot(personal_expenditures_df, label='Despesas Pessoais', color='magenta')
plt.plot(education_df, label='Educação', color='gray')
plt.title('IPCA e Núcleo IPCA - 12 meses', fontsize=20)
plt.legend()
plt.ylabel('% 12 meses')
# Incluir nome no rodapé
plt.text(ipca_df.index[-1], plt.ylim()[0] - 0.7, 'Fabricio Orlandin, CFP®', fontsize=15, ha='right', color='slategray')
#Incluir percentual final
plt.annotate(f'{ipca_df.iloc[-1,0]:.2f}%',
             xy = (ipca_df.index[-1], ipca_df.iloc[-1, 0] - 0.2),
             fontsize = 10, color = 'blue', ha = 'left')
plt.annotate(f'{nucleo_df.iloc[-1,0]:.2f}%',
             xy = (nucleo_df.index[-1], nucleo_df.iloc[-1, 0] - 0.2),
             fontsize = 10, color = 'black', ha = 'left')
#Incluir linhas com as metas
plt.axhline(y=1.5, color='gray', linestyle='--', linewidth=1, label='1,5%')  # Linha em 1,5%
plt.axhline(y=3.0, color='red', linestyle='--', linewidth=1, label='3,0%')  # Linha em 3%
plt.axhline(y=4.5, color='gray', linestyle='--', linewidth=1, label='4,5%')  # Linha em 4,5%
#Incluir percentual objetivos
plt.text(ipca_df.index[-1], 1.5, '1,5%', verticalalignment='bottom', color='gray', fontsize=10)
plt.text(ipca_df.index[-1], 3.0, '3,0%', verticalalignment='bottom', color='red', fontsize=10)
plt.text(ipca_df.index[-1], 4.5, '4,5%', verticalalignment='bottom', color='gray', fontsize=10)
plt.show()
