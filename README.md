# Script de verificação de dados
## diggy.py
### team: list[Member] = load_team()
1. A variável team chama a função load_team() e recebe uma lista de Member.
### backup: str = manage_backup(True, current_date())
1. A variável backup chama a função manage_backup(), passando 2 argumentos e recebe uma string.
2. O primeiro argumento é um booleano True indicando que um backup deve ser criado.
3. O segundo argumento é a função current_date() que retorna uma string com a data atual.
### manage_member(team)
1. Verifica o tamanho da lista para adicionar membros à lista.
### manage_team(arg)
1. Analisa cada membro da lista e atualiza seus dados.
2. Dados iguais o atributo __warning incrementa em 1.
3. Dados diferentes os atributos __level e __score são atualizados e o __warning recebe 0.
### remove_member(arg)
1. Analisa cada membro da lista e verifica se o método get_warning() rertorna 7.
2. Caso haja, será questionado se tem a intenção de retirar o membro da lista.
3. Caso afirmativo o membro será deletado da lista.
### write_team(arg)
1. Grava as informações em um arquivo JSON.
### Em caso de exceção:
1. Os argumentos False e variável backup são passados como argumentos para a função manage_backup()
2. O backup criado é, então, deletado, pois não houve alteração no arquivo original.
## team.py
### class Member
1. Chamada pela função load_team() para instanciar membros do grupo.
2. São criados 4 atributos privados na instanciação.
3. Todos os 4 atributos têm seu respectivo getter.
4. Não foi criado setter para os atributos, porém um método que atualiza os 4 atributos ao mesmo tempo.
5. Método especial \_\_repr\_\_() retorna uma string.
### add_member(arg)
1. Tenta adicionar à lista uma instância da classe Member em uma determinada posição.
2. Retorna a nova lista.
3. Em caso de erro a lista inicial é retornada.
### list_member(arg)
1. Imprime os nomes de cada membro da lista.
### load_team()
1. Abre um contexto "with open" recebendo um arquivo JSON como argumento.
2. Os dados do arquivo JSON são armazenados em um dicionário.
3. O dicionário é transformado em uma lista contendo instâncias da classe Member.
4. Retorna a lista de Member.
### manage_member(arg)
1. Verifica o tamanho do parâmetro arg.
2. Caso seja menor que 30 tenta adicionar um Member na lista de arg.
### manage_team(arg)
1. Para cada membro do parâmetro tenta atualizar os valores de Member.
2. Após capturar os novos valores tenta confirmar os novos valores.
3. Em caso de erro na parte 2 é repetido o processo de captura de dados.
4. Em caso de confirmação na parte 2 os novos dados são atualizados.
### remove_member(arg)
1. Cria uma lista de string resultante do retorno do método get_name() de cada Member do argumento recebido por arg.
2. Verifica se em cada Member o método get_warning() retorna 7 e adiciona o get_name() á lista caso verdadeiro.
3. Caso contenha algum nome na parte 2 tenta excluir de arg através do índice.
### write_team(arg)
1. O argumento passado ao parâmetro arg é transformado em uma lista de string.
2. Depois a lista de string é transformada em um dicionario contendo lista de inteiros.
3. Abre-se um contexto "with open" em modo de gravação.
4. O dicionário é passado como argumento de função chamada pelo contexto.
## bg_op.py
### current_date()
1. Pega do sistema a data-hora atual.
2. Transforma a data-hora atual em string.
3. Transforma a string em lista de string.
4. Retorna o primeiro índice da lista.
### current_path()
1. Retorna o caminho absoluto do arquivo com "\\" ou "/" dependendo so SO.
### manage_backup(create_bkp, bkp_name)
1. Caso o primeiro argumento recebido seja verdadeiro é criado um backup.
2. Caso contrário o backup atual é removido.
### sys_clear()
1. Limpa a tela do terminal.