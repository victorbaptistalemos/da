# Script de verificação de dados
1. Lê os dados de um arquivo JSON
2. Cria um backup.
3. Verifica se alguém saiu do grupo e retira da lista.
4. Verifica se o grupo está incompleto e adiciona à lista.
5. Atualiza os valores de cada membro do grupo.
6. Grava os novos valores em um arquivo JSON.
7. Em caso de erro o backup é deletado.
## Arquivo principal: ```diggy.py```
1. Cria uma variável do tipo Team pela função ```load_team()```
2. Cria um backup e amazena o caminho do backup pela função ```manage_backup()```
3. Atualiza os valores da variável team pela função ```manage_team(team)```
4. Verifica se há dados para excluir da variável team pela função ```remove_member(team)```
5. Grava os valores da variável team em um arquivo JSON pela função ```write_team(team)```
6. Em caso de erro a função ```manage_backup(False, backup)``` deleta o backup existente.
## Arquivo dependente: ```bg_op.py```
1. Realiza operações "nos bastidores".
2. Função ```console()``` executa diversas operações no terminal ou cmd.
3. Função ```current_date()``` retorna uma string com a data atual no formato 'yyyy-mm-dd'.
4. Função ```current_path()``` retorna uma string com o caminho absoluto da aplicação.
5. Função ```is_win()``` verifica se o Sistema Operacional é Windows.
6. Função ```manage_backup()``` cria ou deleta um backup.
7. Função ```sys_clear()``` limpa a tela do terminal ou cmd.
## Arquivo dependente: ```member.py```
### class ```Member```
1. Simula um membro de grupo.
## Arquivo dependente: ```team.py```
### class ```Team```
1. Simula um grupo.
