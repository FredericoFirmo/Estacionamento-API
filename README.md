# Estacionamento-API

Este projeto implementa dois métodos HTTP para trabalhar como servidor de um estacionamento.

O método GET responde com a quantidade de vagas disponíveis, em uso e totais do estacionamento.

O método POST valida se o dado recebido na requisição é válido e retorna o status da movimentação no estacionamento, variando entre: Entrada, saída ou usuário inválido.

## Uvicorn, sqlite3 e FastAPI

Uvicorn é uma implementação de servidor web para python.
sqlite3 é uma biblioteca que implementa um banco de dados SQL.
FastAPI é um framework Web para desenvolvimento de APIs RESTful em Python.

## Instalação de bibliotecas
Use o gerenciador de pacotes [pip](https://pip.pypa.io/en/stable/) para instalar as bibliotecas necessárias.

```bash
pip install uvicorn
pip install db-sqlite3
pip install fastapi
```

## Execução do programa

Rode o arquivo main.py e acesse o link a seguir visualizar os endpoints na plataforma swagger: [Documentação](http://127.0.0.1/docs#/)

## Resultado esperado para o método GET:

{
  "Totalvagas": 100,
  "EmUso": 0,
  "Livre": 100
}

## Resultado esperado para o método POST

{"Status":modo}

**modo** pode assumir os seguintes valores: Entrada, saída ou Inválido


