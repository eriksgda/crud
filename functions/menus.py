def menu(): # função que retorna o menu principal
  print('---------- MENU ----------\n'
        '[1] Gerenciar estudantes\n'
        '[2] Gerenciar professores\n'
        '[3] Gerenciar disciplinas\n'
        '[4] Gerenciar turmas\n'
        '[5] Gerenciar matrículas\n'
        '[0] Sair\n')
  try: # verificação da resposta
    choice = int(input('Informe a ação desejada: '))
    if choice > 5 or choice < 0:
      return print('Valor Inválido!\n')
    else:
      return choice
  except:
    return print('Valor Inválido!\n')


def menu_operations(dict_choice:dict, choice:int): # função que retorna o menu de operações
    print(f'''
---------- [{dict_choice[choice]}] MENU DE OPERAÇÕES ----------
[1] Incluir
[2] Listar
[3] Atualizar
[4] Excluir
[5] Voltar ao menu principal
[0] Sair
''')
    try: # verificação da resposta
      choice_op = int(input('Informe a ação desejada: '))
      if choice_op > 5 or choice_op < 0:
        return print('Valor Inválido!\n')
      else:
        return choice_op
    except:
      return print('Valor Inválido!\n')
  
  
def operation(dict_choice_op:dict, choice_op:int): # função que retorna a função que ira executar
  print(f'========== {dict_choice_op[choice_op]} ==========\n')
  