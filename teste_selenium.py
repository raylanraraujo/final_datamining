from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd

# Abre o navegador e acessa o site
navegador = webdriver.Chrome() 
navegador.get("https://lista.mercadolivre.com.br/iphone")

# Aguarda 5 segundos para o carregamento da página
time.sleep(5) 

# Metadados fixos do projeto
fonte = "mercadolivre" 
categoria = "smartphone"
subcategoria = "iphone"

# Localiza todos os anúncios 
produtos = navegador.find_elements(By.CLASS_NAME, "ui-search-layout__item") # procura os elementos com a classe ui-search-layout__item

dados = [] # cria uma lista vazia para armazenar os dados dos produtos

# Extrai as informações de cada anúncio
for produto in produtos:
    titulo = produto.find_element(By.CLASS_NAME, "poly-component__title") 
    url_produto = titulo.get_attribute("href")
    preco_atual = produto.find_element(By.CLASS_NAME, "poly-price__current") 
    preco = preco_atual.find_element(By.CLASS_NAME, "andes-money-amount") 
    preco_aria = preco.get_attribute("aria-label")

    # Monta o dicionário com os dados coletados
    registro = {
        "fonte": fonte,
        "categoria": categoria,
        "subcategoria": subcategoria,
        "titulo": titulo.text,
        "preco": preco_aria,
        "url_produto": url_produto
    }

    dados.append(registro)

# Converte em DataFrame e exibe no terminal
df = pd.DataFrame(dados) 
print("Dados brutos coletados com sucesso!")

# Salva os dados brutos em CSV
df.to_csv("dados_brutos.csv", index=False, encoding='utf-8-sig', sep=';')

navegador.quit()
# Mantém o navegador aberto até a confirmação
