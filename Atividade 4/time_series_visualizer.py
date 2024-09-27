import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
# Importa os dados e define a coluna 'date' como índice
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'], index_col='date')

# Clean data
# Remove os valores fora do intervalo de 2.5% a 97.5%
df = df[(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975))]
 # Lista de meses para usar nos gráficos
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
def draw_line_plot():
    # Draw line plot
    # Cria o gráfico de linha
    fig, ax = plt.subplots()
    fig.set_size_inches(20, 6)
    ax.plot(df.index, df['value'], color='red')
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')





    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    # Agrupa os dados por ano e mês e calcula a média
    df_bar = df.copy()
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.month
    df_bar = df_bar.groupby(['year', 'month'])['value'].mean().unstack()
    df_bar.columns = months  # Replace month numbers with month names

    # Draw bar plot
    # Cria o gráfico de barras
    fig, ax = plt.subplots()
    fig.set_size_inches(10, 10)
    df_bar.plot(kind='bar', ax=ax)
    ax.set_xlabel('Years')
    ax.set_ylabel('Average Page Views')
    ax.legend(title='Months', labels=months)





    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Reorganize os dados para os gráficos de caixa
    df_box['monthnumber'] = df_box['date'].dt.month
    df_box = df_box.sort_values(by='monthnumber')
    
    # Cria os subplots para os gráficos de caixa (usando Seaborn)
    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(16, 6))
    
    # Gráfico de caixa por ano com paleta de cores
    sns.boxplot(data=df_box, x='year', y='value', ax=axes[0], palette="Set2")
    axes[0].set_title('Year-wise Box Plot (Trend)')
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')
    
    # Gráfico de caixa por mês com paleta de cores
    sns.boxplot(data=df_box, x='month', y='value', ax=axes[1], palette="Set3")
    axes[1].set_title('Month-wise Box Plot (Seasonality)')
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
