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
1. Manipula as classes do módulo ```team.py```.
2. Função ```adding_member()``` adiciona um TeamMember a Team.
3. Função ```entering_member()``` verifica se Team contém 30 elementos em seu atributo.
4. Função ```list_member()``` imprime o nome de cada TeamMember inserido em Team.
5. Função ```load_team()``` lê um arquivo JSON e cria objetos dos tipos Team e TeamMember com os dados lidos.
6. Função ```manage_team()``` itera sobre cada TeamMember em Team e atualiza os dados.
7. Função ```quitting_member()``` verifica se há a necessidade de retirar um TeamMember de Team.
8. Função ```remove_member()``` remove TeamMember se uma determinada condição for alcançada.
9. Função ```write_team()``` grava os dados de Team em um arquivo JSON. 
## Arquivo dependente: ```team.py```
### class ```TeamMember```
1. Simula um membro de um grupo.
### class ```Team```
1. Simula um grupo.
