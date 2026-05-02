# Sistema de Controle de Rega 

Esse projeto começou de uma necessidade bem simples: organizar melhor a rega das minhas próprias plantas.

Tenho um pequeno jardim em casa e, com o tempo, fui percebendo como era fácil esquecer de regar algumas plantas ou até acabar regando mais do que o necessário. Foi daí que surgiu a ideia de criar um sistema que me ajudasse nesse controle.

O sistema foi desenvolvido em Python e utiliza um banco de dados MySQL para armazenar informações como nome da planta, local e frequência de rega.

## O que o sistema faz

- Verifica automaticamente quais plantas precisam ser regadas no dia  
- Mostra um relatório simples no terminal  
- Utiliza uma view no banco de dados para facilitar essa verificação  

## Tecnologias utilizadas

- Python  
- MySQL  
- MySQL Connector  

## Como usar

Para executar o sistema, é necessário:

1. Ter o MySQL instalado e configurado  
2. Criar o banco de dados com a estrutura utilizada no projeto  
3. Atualizar a senha do banco no arquivo `alerta.py`  
4. Executar o script no terminal  

## Observação

O projeto foi adaptado posteriormente para um trabalho acadêmico, mas a ideia original veio de uma necessidade real do dia a dia.  

Com o tempo, ele pode ser melhorado com novas funcionalidades, como integração com sensores ou uma interface gráfica.


Projeto desenvolvido por Rosa Maria de Oliveira Neves 
