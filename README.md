# Rede Social

Essa api foi desenvolvida pensando em um ambiente de uma rede social, onde tem requisições básicas
sobre interações de usuarios, tais como criar uma interação de amizade ou seguidor enter diversos
usuarios e suas respectivas linhas do tempo (feed).

Para colocar o projeto em prática, e conseguir rodar o servidor da api, existem alguns passos
que devemos seguir:

1. Criar um banco de dados postgre (nome de sua escola)

2. Configure o arquivo .env.example, onde :

2.1 PGHOST - host em que o servidor sera executado (localhost, para rodar em sua propria maquina)
2.2 PGPORT - porta que o banco sera executada (5432, padrão do postgre)
2.3 PGUSER - usuario do posgtre
2.4 PGPASSWORD - senha do usuario postgre
2.5 PGDATABASE - nome do banco de dados
2.6 SECRET_KEY - nome da sua chave secreta (pode ser qualquer string)

3. feito isso, remova .example do final do arquivo, e deixe somente .env

Abra seu terminal na raiz do projeto e rode os seguintes comandos:

1. Crie seu ambiente virtual:

```bash
python -m venv venv
```

2. Ative seu venv:

```bash
# linux:
source venv/bin/activate

# windows:
.\venv\Scripts\activate
```

3. instale os pacatoes de requerimentos

```bash
pip install -r requirements.txt
```

4. execute as migrações

```bash
python manage.py migrate
```

5. rode o servidor

```bash
python manage.py runserver
```
