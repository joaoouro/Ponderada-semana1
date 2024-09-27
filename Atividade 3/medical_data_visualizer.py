import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Carregamento do arquivo CSV com dados médicos
df = pd.read_csv('medical_examination.csv')

# Criando uma coluna 'overweight' (acima do peso) usando a fórmula do IMC
df['overweight'] = (df['weight'] / ((df['height'] / 100) ** 2) > 25).astype(int)

# Ajustando os valores de colesterol e glicose para binário (1 = anormal, 0 = normal)
df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)

# Função para desenhar o gráfico categórico (catplot)
def draw_cat_plot():
    # Definição da variável df_cat que será utilizada para plotar o gráfico
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke'])

    # Criação do gráfico em formato catplot (gráfico categórico)
    fig = sns.catplot(data=df_cat, kind='count', x='variable', hue='value', col='cardio').set(ylabel='total').fig

    # Salvando o gráfico categórico como um arquivo de imagem
    fig.savefig('catplot.png')
    return fig

# Função para desenhar o mapa de calor (heatmap)
def draw_heat_map():
    # Filtrando os dados conforme as condições descritas (limpeza de dados)
    df_heat = df[(df['ap_lo'] <= df['ap_hi']) &  # Pressão diastólica não pode ser maior que a sistólica
                 (df['height'] >= df['height'].quantile(0.025)) &  # Removendo outliers de altura (abaixo do 2.5%)
                 (df['height'] <= df['height'].quantile(0.975)) &  # Removendo outliers de altura (acima do 97.5%)
                 (df['weight'] >= df['weight'].quantile(0.025)) &  # Removendo outliers de peso (abaixo do 2.5%)
                 (df['weight'] <= df['weight'].quantile(0.975))]   # Removendo outliers de peso (acima do 97.5%)

    # Calculando a correlação entre as variáveis do dataframe filtrado
    corr = df_heat.corr()

    # Criando uma máscara para mostrar apenas a metade superior da matriz de correlação
    mask = np.triu(corr)

    # Criando uma figura e os eixos do gráfico
    fig, ax = plt.subplots()

    # Desenhando o mapa de calor com a máscara aplicada, números anotados, e quadrados perfeitos
    ax = sns.heatmap(corr, annot=True, fmt='0.01f', mask=mask, square=True)

    
    fig.savefig('heatmap.png')
    return fig