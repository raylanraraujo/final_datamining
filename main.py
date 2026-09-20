import os  # Módulo utilizado para verificar a existência de arquivos no sistema

def executar_scraping():
    # Chama o script de coleta de dados no Mercado Livre
    print("\n[1/5] Executando Coleta de Dados (Selenium)...")
    import teste_selenium

def executar_tratamento():
    # Chama o script de limpeza (valida primeiro se o CSV de origem existe)
    print("\n[2/5] Executando Tratamento de Dados...")
    if not os.path.exists("dados_brutos.csv"):
        print(
            "Erro: O arquivo 'dados_brutos.csv' não foi encontrado. Execute o scraping primeiro!"
        )
        return
    import tratamento

def executar_analise():
    # Chama o script de análises e métricas estatísticas
    print("\n[3/5] Executando Análise Estatística...")
    if not os.path.exists("dados_tratados.csv"):
        print(
            "Erro: O arquivo 'dados_tratados.csv' não foi encontrado. Execute o tratamento primeiro!"
        )
        return
    import analise

def executar_graficos():
    # Chama o script de geração e exibição dos gráficos
    print("\n[4/5] Gerando Gráficos...")
    if not os.path.exists("dados_tratados.csv"):
        print(
            "Erro: O arquivo 'dados_tratados.csv' não foi encontrado. Execute o tratamento primeiro!"
        )
        return
    import graficos

def executar_dashboard():
    #Chama o script do dashboard
    print("\n[5/5] Gerando Dashboard...")
    if not os.path.exists("dados_tratados.csv"):
        print(
            "Erro: O arquivo 'dados_tratados.csv' não foi encontrado. Execute o tratamento primeiro!"
        )
        return
    import dashboard

def exibir_menu():
    # Interface principal e controle do fluxo de navegação
    while True:
        print("\n" + "=" * 40)
        print("      SISTEMA DE WEB SCRAPING IPHONE    ")
        print("=" * 40)
        print("1. Coletar dados brutos (Selenium)")
        print("2. Tratar dados (Limpeza e conversão)")
        print("3. Exibir análise de preços")
        print("4. Exibir gráficos")
        print("5. Exibir dashboard")
        print("0. Sair")
        print("=" * 40)

        opcao = input("Escolha uma opção (0-5): ").strip()

        # Roteamento das opções do usuário
        if opcao == "1":
            executar_scraping()
        elif opcao == "2":
            executar_tratamento()
        elif opcao == "3":
            executar_analise()
        elif opcao == "4":
            executar_graficos()
        elif opcao == "5":
            executar_dashboard()
        elif opcao == "0":
            print("\nSaindo do programa. Até logo!")
            break
        else:
            print("\nOpção inválida! Digite um número de 0 a 5.")

# Executa o menu caso o script seja rodado diretamente
if __name__ == "__main__":
    exibir_menu()