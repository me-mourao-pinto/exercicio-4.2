from fastapi import FastAPI, status
from pydantic import BaseModel

app = FastAPI()

tarefas = [
    {"id": 1, "titulo": "estudar APIs REST", "concluida": True}
]
prox_id = 2


class TarefaIn(BaseModel):
    titulo: str


@app.post("/tarefas", status_code=201)
def criar_tarefa(t: TarefaIn):
    global prox_id
    nova = {"id": prox_id, "titulo": t.titulo, "concluida": False}
    tarefas.append(nova)
    prox_id += 1
    return nova


@app.get("/tarefas")
def listar_tarefas():
    return tarefas
