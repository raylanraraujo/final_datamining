import pandas as pd

# Carrega os dados brutos
df = pd.read_csv("dados_brutos.csv", sep=';')

# Validações de nulos e duplicados
# print(df.isnull().sum()) # o isnull verifica se tem dados faltando e o sum soma quantos estão faltando
# print("dados duplicados:", df.duplicated().sum()) # conta quantos dados estão duplicados

# Remove anúncios com valores em centavos para simplificar o tratamento
df = df[~df["preco"].str.contains("centavo", na=False)]

# Limpa o texto da coluna de preço e converte para número
df["preco"] = df["preco"].str.replace("reais", "") 
df["preco"] = pd.to_numeric(df["preco"]) 

#Exporta os dados tratados para um outro arquivo CSV
df.to_csv("dados_tratados.csv", index=False, encoding='utf-8-sig', sep=';') 

# Mensagens de confirmação
print("dados tratados com sucesso") 
print("total de produtos:", len(df))
