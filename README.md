#  Sistema Automatizado de Monitoramento e Alerta de Regas

Este projeto nasceu de uma necessidade real e prática do meu cotidiano: gerenciar e monitorar a saúde e a frequência de regas de uma coleção diversa de plantas residenciais (incluindo folhagens, flores, suculentas e cactos). 

Originalmente concebido para uso pessoal, o sistema foi expandido e refinado como **Projeto Integrador** para o curso superior de Tecnologia em **Análise e Desenvolvimento de Sistemas (UNISA)**. Ele demonstra a integração de ponta a ponta (*End-to-End*) entre uma aplicação **Python** e um banco de dados **MySQL relacional**, aplicando regras de negócio customizadas para a geração de alertas automatizados.


##  Tecnologias e Ferramentas Utilizadas

* **Linguagem Principal:** Python 3.x
* **Banco de Dados:** MySQL (Gerenciado via MySQL Workbench)
* **Driver de Conexão:** mysql-connector-python
* **Persistência de Logs:** Manipulação de arquivos nativa do Python (.txt)


##  Arquitetura e Regras de Negócio

O sistema realiza uma varredura automatizada na tabela de dados, extrai o histórico de cada planta e aplica critérios específicos baseados em sua tipologia para determinar a necessidade de intervenção:

* Folhagens: Intervalo máximo de segurança de 5 dias entre as regas.
* Flores: Intervalo máximo de segurança de 5 dias entre as regas.
* Suculentas: Intervalo máximo de segurança de 10 dias entre as regas.
* Cactos: Intervalo máximo de segurança de 15 dias entre as regas.

### Funcionalidades do Script Python:
1. **Conexão Dinâmica:** Estabelece comunicação segura com o banco de dados "meu_refugio".
2. **Processamento e Análise:** Calcula em tempo real, através do módulo datetime, a data limite de rega de cada planta conforme sua tipologia (folhagem, flor, suculenta ou cacto), identificando automaticamente situações de atraso.
3. **Mecanismo de Alerta:** Dispara avisos de **REGA URGENTE** detalhando o nome da planta e sua localização exata.
4. **Auditoria (Logs):** Grava automaticamente o resultado de cada varredura em um arquivo físico chamado **registro_rega.txt**, gerando histórico de monitoramento.


##  Estrutura do Repositório

* alerta.py: Código-fonte principal em Python responsável pela inteligência do sistema e alertas.
* meu_refugio.sql: Script de exportação da estrutura do banco de dados e registros das plantas.
* LICENSE: Licença de uso do projeto (MIT).
* .gitignore: Filtro de segurança para arquivos de cache e credenciais.

---

##  Como Executar o Projeto

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/seu-usuario/seu-repositorio.git](https://github.com/seu-usuario/seu-repositorio.git)
