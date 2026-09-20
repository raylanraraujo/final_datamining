# Guia de Configuração do Ambiente Virtual

## 1. Criar o ambiente virtual
Execute o comando abaixo no terminal da pasta do seu projeto:

```bash
python -m venv venv
```

## 2. Ativar o ambiente virtual
O comando depende do sistema operacional que você está utilizando:

- **Windows (PowerShell):** `.\venv\Scripts\Activate.ps1`
- **Windows (Prompt de Comando / CMD):** `.\venv\Scripts\activate.bat`
- **Linux / macOS:** `source venv/bin/activate`
- **git bash:** `source venv/bin/activate`


## 3. Verificar a ativação
Após o comando, o nome `(venv)` deverá aparecer no início da linha do seu terminal.

## 4. Instalar as dependências (se houver o arquivo requirements.txt)
```bash
pip install -r requirements.txt
```

## 5. Executar o script
```bash
python main.py
```