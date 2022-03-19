# Script de verificação de dados
1. Lê os dados de um arquivo JSON
2. Cria um backup.
3. Verifica se alguém saiu do grupo e retira da lista.
4. Verifica se o grupo está incompleto e adiciona à lista.
5. Atualiza os valores de cada membro do grupo.
6. Grava os novos valores em um arquivo JSON.
7. Em caso de erro o backup é deletado.
## Arquivo principal: ```main.py```
1. Cria uma variável do tipo Team chamando a classe ```Team```
2. Cria um backup e amazena o caminho do backup pela função ```create_backup()```
3. Atualiza os valores da variável team pelo método ```Team.manage_team()```
5. Grava os valores da variável team em um arquivo JSON pelo método ```Team.write_team()```
6. Em caso de erro a função ```delete_backup()``` deleta o backup existente.
## Arquivo dependente: ```bg_op.py```
1. Realiza operações "nos bastidores".
2. Função ```command()``` retorna uma string de comando com base no SO.
3. Função ```console()``` executa diversas operações no terminal ou cmd.
4. Função ```create_backup()``` cria um backup.
5. Função ```current_date()``` retorna uma string com a data atual no formato 'yyyy-mm-dd'.
6. Função ```current_path()``` retorna uma string com o caminho absoluto da aplicação.
7. Função ```delete_backup()``` deleta um backup.
8. Função ```is_win()``` verifica se o Sistema Operacional é Windows.
9. Função ```sys_clear()``` limpa a tela do terminal ou cmd.
## Arquivo dependente: ```member.py```
### class ```Member```
1. Simula um membro de grupo.
## Arquivo dependente: ```team.py```
### class ```Team```
1. Simula um grupo.
