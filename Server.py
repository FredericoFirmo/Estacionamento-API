from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from BancodeDados import BancodeDados
from config import estacionamento

app = FastAPI()
db = BancodeDados()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=["*"],
    allow_headers=["*"]
)

class Item(BaseModel):
    tag_id: str

class Server(Item):
    @app.post("/validarUser")
    async def validarUser(conteudo: Item):
        tag_id = conteudo.tag_id
        #conexão com o banco de dados
        banco,cursor = db.conectarBanco()

        #Consultar se o usuário existe no banco
        todosUsuarios = db.obterDadosComFiltro(cursor,'user',tag_id)
        quantidadeUsuarios = len(todosUsuarios)
        #Se não existe retorna o status: inválido
        if(quantidadeUsuarios == 0):
            return {"Status":"Invalido"}
        
        #Passo 01: Entrada e saída: Consultar na tabela contagem, se não existe é entrada, se existe é saida.
        usuariosNaTabelaContagemPorTagId = db.obterDadosComFiltro(cursor,'contagem',tag_id)
        existeNoEstacionamento = len(usuariosNaTabelaContagemPorTagId)

        if(existeNoEstacionamento == 0):
            modo = db.inserirDados(banco,cursor,'contagem',tag_id)
        elif(existeNoEstacionamento > 0):
            modo = db.apagarDados(banco,cursor,'contagem',tag_id)
        else:
            return "Falha na execução!"

        return {"Status":modo}

    #Obter a quantidade de vagas disponíveis, em uso e total.
    @app.get("/contagem/")
    def obterContagem():
        totalVagas = estacionamento['totalVagas']
        banco,cursor = db.conectarBanco()
        usuariosNaTabelaContagem = db.obterDados(cursor,'contagem')
        vagasEmUso = len(usuariosNaTabelaContagem)
        return {"Totalvagas": totalVagas,"EmUso": vagasEmUso,"Livre": totalVagas - vagasEmUso}