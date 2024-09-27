import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
   # Leitura dos dados do arquivo CSV
    df = pd.read_csv('epa-sea-level.csv')
    
    # Criação do gráfico de dispersão
    fig, ax = plt.subplots()
    ax.scatter(df["Year"], df["CSIRO Adjusted Sea Level"])
    
    # Primeira linha de tendência (utilizando todos os dados)
    regress_1 = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    anos_previstos = pd.Series(range(1880, 2051))  # Incluindo o ano de 2050 para corresponder ao teste
    ax.plot(anos_previstos, regress_1.intercept + regress_1.slope * anos_previstos, 'r', label='Linha de tendência 1')
    
    # Segunda linha de tendência (após 2000)
    df_2000 = df[df["Year"] >= 2000]
    regress_2 = linregress(df_2000["Year"], df_2000["CSIRO Adjusted Sea Level"])
    anos_previstos_2 = pd.Series(range(2000, 2051))  # Incluindo o ano de 2050
    ax.plot(anos_previstos_2, regress_2.intercept + regress_2.slope * anos_previstos_2, 'b', label='Linha de tendência 2')
    
    # Adiciona rótulos e título ao gráfico
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")
    ax.set_title("Rise in Sea Level")
    
    # Exibir a legenda
    ax.legend()
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()