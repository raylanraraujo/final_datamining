import pandas as pd

# Carrega os dados
df = pd.read_csv("dados_tratados.csv", sep=';')

# Total de produtos
quantidade_produtos = len(df)
print("quantidade de produtos:", quantidade_produtos) 

# Média e mediana dos preços
preco_medio = df["preco"].mean() 
print(f"preço medio dos iphones são: R$ {preco_medio:.2f}") 

preco_mediana = df["preco"].median() 
print(f"ao valor da mediana dos iphones é: R$ {preco_mediana:.2f}")

# Menor e maior preço
menor_preco = df["preco"].min()
maior_preco = df["preco"].max()

# Busca o produto mais barato e o mais caro pelo índice
produto_mais_barato = df.loc[df["preco"].idxmin()]
produto_mais_caro = df.loc[df["preco"].idxmax()]

print(f"o menor preço é: R$ {menor_preco:.2f}") 
print("o produto mais barato é:", produto_mais_barato["titulo"])

print(f"o maior preço é: R$ {maior_preco:.2f}") 
print("o produto mais caro é:", produto_mais_caro["titulo"])

# Agrupa e lista os produtos por faixas de R$ 1.000
for inicio in range(int(menor_preco), int(maior_preco), 1000):
    fim = inicio + 1000

    produtos_faixa = df[
        (df["preco"] >= inicio) &
        (df["preco"] < fim)
    ]

    print(f"\nFaixa de R$ {inicio} até R$ {fim - 1}")
    print("Quantidade:", len(produtos_faixa))

    if not produtos_faixa.empty:
        print(produtos_faixa["titulo"].to_string(index=False))
    else:
        print("Nenhum produto nesta faixa.")