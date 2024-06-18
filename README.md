# Test Laborit - LLM :: Text2SQL

## Visão Geral
Este projeto é uma aplicação web Flask que traduz perguntas de usuários em consultas SQL usando uma API de IA. Ele se conecta a um banco de dados MySQL para recuperar e exibir os resultados. Abaixo estão os detalhes de cada parte do script.

## Dependências
- Python 3.x
- Flask
- pymysql
- openai
- re
- logging

## Instruções de Configuração
1. Clone o repositório.
2. Instale as dependências necessárias usando pip:
   ```bash
   pip install flask pymysql openai
   ```
   ou rode o requiriments.txt:
   ```bash
   pip install -r requiriments.txt
   ```

3. As configurações o banco de dados e a API estão localizadas no arquivo `config.py` na raiz do projeto.

## Descrição do Script

### Imports

O script importa várias bibliotecas essenciais para sua execução, incluindo Flask, pymysql, e outras.

### Inicialização da Aplicação Flask

A aplicação Flask é inicializada com 
```bash
app = Flask(__name__)
```

### Configuração do Banco de Dados

O dicionário `db_config` contém os detalhes de configuração para conectar ao banco de dados MySQL, incluindo host, porta, usuário, senha e nome do banco de dados.

### Inicialização da API

A chave da API é configurada usando `openai.api_key = API + str(last())`, combinando uma chave base do arquivo de configuração e uma parte adicional gerada pela função `last`. Fiz em caráter de teste sem considerar os termos de segurança pois se trata de um teste, mas o ideal que a chave vem criptografada pelos meios comuns ou chaves de dupla custódia.

### Configuração de Logging

O nível de logging é configurado para INFO usando
```bash
logging.basicConfig(level=logging.INFO)
```

### Função: Obter Esquema do Banco de Dados

A função `get_db_schema()` conecta-se ao banco de dados MySQL e recupera o esquema de todas as tabelas, retornando um dicionário com os nomes das tabelas e suas colunas.

### Função: Executar Consulta SQL

A função `execute_query(query)` executa uma consulta SQL fornecida e processa os resultados, arredondando valores numéricos. Ela também lida com erros de execução da consulta.

### Função: Text-to-SQL usando IA

A função `text_to_sql(question: str, schema: dict) -> str` converte uma pergunta em linguagem natural em uma consulta SQL usando o modelo de IA. Ela constrói um contexto com a descrição do esquema do banco de dados e usa a API para gerar a consulta SQL. Somente depois de ler toda a estrutura do database ela está preparada para montar as consultas

### Rotas

#### Rota Principal

A rota `'/'` renderiza a página principal usando `return render_template('index.html')`.

#### Rota `/ask`

A rota `/ask`, que lida com solicitações POST, recebe uma pergunta do usuário, obtém o esquema do banco de dados, gera a consulta SQL usando a função `text_to_sql`, executa a consulta e retorna os resultados no `index.html` preparado para recebê-lo.

### Main

O script é executado em modo debug com `app.run(debug=True)` quando executado diretamente.

## Uso
1. Inicie a aplicação Flask:
   ```bash
   python app.py
   ```
2. Navegue para `http://127.0.0.1:5000/` em seu navegador web.

- [localhost](http://127.0.0.1:5000/)

3. Insira uma pergunta relacionada ao banco de dados no campo de entrada e envie para obter os resultados.

## Notas de Segurança
- Certifique-se de que informações sensíveis, como chaves de API e credenciais do banco de dados, sejam gerenciadas de forma segura e não estejam hardcoded no código.
- Considere usar variáveis de ambiente ou uma ferramenta de gerenciamento de configuração para gerenciar informações sensíveis.

## Internacionalização
> :AVISO IMPORTANTE: **SOBRE AS CONSULTAS**: Preferencialmente na Língua -> EN-US
- O sistema LLM e Text2SQL foi desenvolvido para trabalhar com um banco de dados inteiramente em inglês. Devido a algumas traduções, certas pesquisas podem não ser completas ou precisas devido a erros de tradução. Isso ocorre porque a tradução automática pode não capturar corretamente o contexto ou os termos técnicos específicos usados nas consultas e no esquema do banco de dados. Para minimizar esses problemas, é recomendável usar termos e perguntas em inglês sempre que possível.

## Resumo do teste.
- Foi um desafio pois com esse modelo minimizamos a forma de gerar consultas e deixamos a IA gerar os cruzamentos de informações e extração de forma que o sistema fique mais independente. Obrigado ao time de seleção da Laborit por propor esse desafio.
