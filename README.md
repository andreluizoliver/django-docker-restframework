# Requisitos:
* Python: 3.5.2
* Pip: 18.1
* Virtualenv: 16.0.0
* Trello Card Numbers: 

# Padrão Nome Branch:
	
* Feature: São branches no qual são desenvolvidos recursos novos para o projeto em questão. Essas branches tem por convenção nome começando com feature/ (exemplo: feature/new-layout) e são criadas a partir da branch develop (pois um recurso pode depender diretamente de outro recurso em algumas situações), e, ao final, são juntadas com a branch develop;
	* feature/[ID_TRELLO]_Descricao_do_que_foi_feito_na_branch

* Hotfix: São branches no qual são realizadas correções de bugs críticos encontrados em ambiente de produção, e que por isso são criadas a partir da branch master, e são juntadas diretamente com a branch master e com a branch develop (pois os próximos deploys também devem receber correções de bugs críticos, certo?). Por convenção, essas branches tem o nome começando com hotfix/ e terminando com o próximo sub-número de versão (exemplo: hotfix/2.31.1), normalmente seguindo as regras de algum padrão de versionamento, como o padrão do versionamento semântico, que abordei neste post;
	* hotfix/[ID_TRELLO]_Descricao_do_que_foi_feito_na_brench

* Release: São branches com um nível de confiança maior do que a branch develop, e que se encontram em nível de preparação para ser juntada com a branch master e com a branch develop (para caso tenha ocorrido alguma correção de bug na branch release/* em questão). Note que, nessas branches, bugs encontrados durante os testes das features que vão para produção podem ser corrigidos mais tranquilamente, antes de irem efetivamente para produção. Por convenção, essas branches tem o nome começando com release/ e terminando com o número da próxima versão do software (seguindo o exemplo do hotfix, dado acima, seria algo como release/2.32.0), normalmente seguindo as regras do versionamento semântico, como falado acima;
	* release/99.99.99

# Instalação do Ambiente:

* Clonar repositorio
```
	$ git clone https://{user}@bitbucket.org/4Effect/backend-intelbras.git
```

* Acessar pasta do repositorio git 
```
	$ cd backend-intelbras
```

* Instalar Virtualenv
```
	$ pip3 install virtualenv
	$ virtualenv --version
```

* Criar ambiente virtual
```
	$ python3 -m venv env-intelbras
```

* Acessar ambiente virtual
```
	LINUX:
	$ source env-intelbras/bin/activate
```
```
	WINDOWS:
	$ env-intelbras\Scripts\activate.bat
```

* Atualizar pip
```
	$ pip install --upgrade pip
```

* Instalar dependencia no ambiente virtual
```
	$ pip install -r requirements.txt
```

* Acessar pasta do projeto django
```
	$ cd backend-intelbras/
```
* Criar base de dados
```
	$ python manage.py makemigrations
	$ python manage.py migrate
```

* Criar base de dados postgres
```
    Instalar o servidor postgres, usar imagem docker ou usar elephantSQL 
    
	$ python manage.py makemigrations --database=postgres
	$ python manage.py migrate --database=postgres
```

* Criar usuario
```
	$ python manage.py createsuperuser
```

* Iniciar servidor web
```
	$ python manage.py runserver 0.0.0.0:8080
```

* Acessar no browser o url 
```
	http://127.0.0.1:8080/api/
	http://127.0.0.1:8080/admin/
	http://127.0.0.1:8080/docs/
```

# Iniciar aplicação:

* Acessar pasta do repositorio git 
```
	$ cd backend-intelbras
```

* Acessar ambiente virtual
```
	LINUX:
	$ source env-intelbras/bin/activate
```
```
	WINDOWS:
	$ env-intelbras\Scripts\activate.bat
```

* Iniciar servidor web
```
	$ python backend-intelbras/manage.py runserver 0.0.0.0:8080
```

* Acessar no browser o url 
```
	http://127.0.0.1:8080/api/
	http://127.0.0.1:8080/admin/
	http://127.0.0.1:8080/docs/
```

# Parar aplicação:

* Parar servidor web
```
	Pessionar: 2 x CONTROL-C
```

* Sair do ambiente virtual
```
	$ deactivate
```

# Subir aplicação Docker:

* Comando para subir serviço
```
	$ docker-compose up
```