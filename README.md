EQUIPE 4: Jonathan Gustavo Inacio de Lira, Giovanna Figueiredo Soares

Olá Equipe Coder!



Este código realiza a tarefa de buscar dados de bancos brasileiros a partir de uma API pública e armazená-los em um banco de dados SQLite.

*Etapas do Código

-Importação das Bibliotecas

O código utiliza duas bibliotecas principais: sqlite3, para manipulação do banco de dados SQLite, e requests, para realizar requisições HTTP.

-Definição da URL da API

É definida a URL da API que fornece informações sobre os bancos brasileiros.

-Requisição e Recebimento dos Dados

O código faz uma requisição HTTP do tipo GET para a API e obtém os dados dos bancos em formato JSON.

-Conexão com o Banco de Dados SQLite

Uma conexão com um banco de dados SQLite chamado bancos.db é estabelecida, e um cursor é criado para executar comandos SQL.

-Criação das Tabelas no Banco de Dados
São criadas três tabelas:

-bancos: Armazena o nome, código e ISPB dos bancos.

-codigos_bancarios: Armazena o nome do banco e seu código.

-bancos_ispb: Armazena o nome do banco e seu ISPB.


-Inserção dos Dados nas Tabelas

Para cada banco recebido da API, o código insere os dados nas três tabelas mencionadas, contanto que todos os campos necessários (nome, codigo, ispb) estejam presentes. Os dados são inseridos de forma a garantir que as informações estejam corretamente distribuídas entre as tabelas.

-Salvamento e Fechamento da Conexão

Finalmente, o código salva todas as mudanças feitas no banco de dados e fecha a conexão com o SQLite.


![TABELA1](https://github.com/JowGuh/CODERHOUSER-EQUIPE-4/assets/152320761/8eae5ea5-47ba-4f54-8853-b57d55c45538)  ![TABELA2](https://github.com/JowGuh/CODERHOUSER-EQUIPE-4/assets/152320761/d834fe78-8e00-45ad-afc6-51c89de57905)  ![TABELA3](https://github.com/JowGuh/CODERHOUSER-EQUIPE-4/assets/152320761/d9fae9e7-8104-4359-9d26-bc614c971301)



