import pandas as pd
import matplotlib.pyplot as plt

# LENDO OS DADOS TRATADOS
df = pd.read_csv("dados_tratados.csv", sep=";")

# INDICADORES PRINCIPAIS
quantidade = len(df)
preco_medio = df["preco"].mean()
preco_minimo = df["preco"].min()
preco_maximo = df["preco"].max()
mediana = df["preco"].median()

# FAIXAS DE PREÇO
faixas = [0,    2000,    3000,    4000,    5000,    6000,    7000,    8000,    9000,    10000,    float("inf")]
nomes_faixas = ["Até 2 mil",    "2-3 mil",    "3-4 mil",    "4-5 mil",    "5-6 mil",    "6-7 mil",    "7-8 mil",    "8-9 mil",    "9-10 mil",    "10 mil+"]

# Criando uma nova coluna com as faixas
df["faixa_preco"] = pd.cut(
    df["preco"],
    bins=faixas,
    labels=nomes_faixas,
    right=False
)

# Contando quantos produtos existem em cada faixa
quantidade_por_faixa = df["faixa_preco"].value_counts(sort=False)

# CRIANDO O DASHBOARD
fig, axs = plt.subplots(
    2,
    2,
    figsize=(14, 9)
)

# Título principal
fig.suptitle(
    "Dashboard de Análise de Preços de iPhones",
    fontsize=18,
    y=0.98
)

# 1 - RESUMO DOS DADOS

# Remove os eixos
axs[0, 0].axis("off")

# Título do quadro
axs[0, 0].text(
    0.1,
    0.90,
    "Resumo dos dados",
    fontsize=14,
    fontweight="bold"
)

# Informações do resumo
axs[0, 0].text(
    0.1,
    0.72,
    f"Quantidade de produtos: {quantidade}\n\n"
    f"Preço médio: R$ {preco_medio:.2f}\n\n"
    f"Menor preço: R$ {preco_minimo:.2f}\n\n"
    f"Maior preço: R$ {preco_maximo:.2f}\n\n"
    f"Mediana: R$ {mediana:.2f}",
    fontsize=12,
    verticalalignment="top"
)

# 2 - GRÁFICO DE BARRAS

quantidade_por_faixa.plot(
    kind="bar",
    ax=axs[0, 1]
)

axs[0, 1].set_title("Quantidade por faixa de preço")
axs[0, 1].set_xlabel("Faixa de preço")
axs[0, 1].set_ylabel("Quantidade de ofertas")
axs[0, 1].tick_params(axis="x", rotation=45)

# 3 - HISTOGRAMA

axs[1, 0].hist(    df["preco"],    bins=10)
axs[1, 0].set_title("Distribuição dos preços")
axs[1, 0].set_xlabel("Preço (R$)")
axs[1, 0].set_ylabel("Quantidade de ofertas")

# 4 - BOXPLOT

axs[1, 1].boxplot(df["preco"])
axs[1, 1].set_title("Boxplot dos preços")
axs[1, 1].set_ylabel("Preço (R$)")

# AJUSTANDO OS ESPAÇAMENTOS

plt.subplots_adjust(
    top=0.88,
    bottom=0.10,
    left=0.08,
    right=0.97,
    hspace=0.42,
    wspace=0.20
)

# MOSTRANDO O DASHBOARD
plt.show()