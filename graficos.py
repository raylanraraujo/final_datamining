import pandas as pd
import matplotlib.pyplot as plt

# carrega os dados
df = pd.read_csv("dados_tratados.csv", sep=';') 

# define os limites e os nomes das faixas de preço
faixas = [2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, float("inf")]
nomes_faixas = [
    "2-3 mil", "3-4 mil", "4-5 mil", "5-6 mil",
    "6-7 mil", "7-8 mil", "8-9 mil", "9-10 mil", "10 mil+"
]

# Classifica os preços nas faixas criadas
df["faixa_preco"] = pd.cut(
    df["preco"],
    bins=faixas,
    labels=nomes_faixas,
    right=False
) # o bins define os limites das faixas, e o labels define os nomes que serão atribuídos a cada faixa. O parâmetro right=False indica que o limite superior da faixa não está incluído na faixa.

# Conta quantos produtos existem em cada faixa (sem reordenar)
quantidade_por_faixa = df["faixa_preco"].value_counts(sort = False)

# Gráfico 1: Gráfico de barras por faixa personalizada
quantidade_por_faixa.plot(kind="bar") # plot() é o método que cria o gráfico, e o parâmetro kind="bar" indica que o gráfico será do tipo barra.
plt.title("Quantidade de ofertas de iPhone por faixa de preço")
plt.xlabel("Faixa de preço")
plt.ylabel("Quantidade de ofertas")
plt.xticks(rotation=45) # Inclina os rótulos do eixo X para facilitar a leitura
plt.tight_layout() # Ajusta o espaçamento
plt.show()

# Gráfico 2: Histograma da distribuição de preços
plt.hist(df["preco"], bins=10)
plt.title("Distribuição dos preços dos iPhones")
plt.xlabel("Preço (R$)")
plt.ylabel("Quantidade de ofertas")
plt.tight_layout()
plt.show()

# Gráfico 3: Boxplot para identificar mediana e possíveis discrepâncias (outliers)
plt.boxplot(df["preco"])
plt.title("Distribuição dos preços dos iPhones")
plt.ylabel("Preço (R$)")
plt.tight_layout()
plt.show()