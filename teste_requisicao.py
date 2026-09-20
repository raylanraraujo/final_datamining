import requests

#código para tentar usar o request, mas não funcionou! apenas para mostrar como fizemos
url = "https://lista.mercadolivre.com.br/iphone"

headers = {
    "User-Agent": "Mozilla/5.0"
}

resposta = requests.get(url, headers = headers) # faz a requisição na url so site

print(resposta.status_code) # mostra o status da requisição
print(resposta.text[:1000]) # mostra o conteudo da requisição

print("ui-search-layout__item" in resposta.text)