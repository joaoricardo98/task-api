# task-api

## Ambiente
### requisitos
- python 3.8+

### passo a passo

Criar A Venv

`
python3 -m venv .venv/
`

Entrar na venv

`source .venv/bin/activate`


## Execução

Realizar as migrações

`python manage.py migrate`

Rodar o servidor

`python manage.py runserver`

## End-points
###Usuario

####Criar Usuario

POST `/users/`

body
```json
{
    "name": "nome"
}
```
####Listar Usuarios
GET `/users/`

response
```json
[
    {
        "name": "nome1",
        "id": 1
    },
    {
        "name": "nome2",
        "id": 2
    }
]
```
####Buscar Usuario específico 
GET `/users/<id_user:int>/`

response
```json
{
    "name": "nome1",
    "id": 1
}
```
####Deletar Usuario específico 
DELETE `/users/<id_user:int>/`

###Tasks
###Criar uma tarefa
POST `/tasks/`

body
```json
 {
     "description": "description1",
     "user": 1
 }
```
#### Listar as tarefas
GET `/tasks/`

response
```json
[
     {
         "description": "description1",
         "user": 1
     }
]
```
####Buscar tarefa específica
GET `/tasks/<task_id:int>/`

response
```json
 {
     "description": "description1",
     "user": 1
 }
```
####Deletar a tarefa específica
DELETE `/tasks/<task_id:int>/`

####Atualizar a tarefa especifica
PATCH `/tasks/<task_id:int>/`

body
```json
{
    "status": 2
}
```


###Tasks por usuario

####Listar todas as tarefas do usuario
GET `/users/<id_user:int>/tasks/`

response
```json
[
    {
        "description": "description1",
        "status": 1
    }
]
```