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


def menu_operations(v_choice:dict, choice:int): # função que retorna o menu de operações
    print(f'''
---------- [{v_choice[choice]}] MENU DE OPERAÇÕES ----------
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
  
  
def operation(v_choice_op:dict, choice_op:int): # função que retorna a função que ira executar
  print(f'========== {v_choice_op[choice_op]} ==========\n')
  



def include(choice:int, v_choice:dict, lista_op:dict): # função que adiciona (incluir) nas listas
  if choice == 1 or choice == 2: # pra saber se é Quantos ou Quantas
    try: # verificação da resposta
      ask = int(input(f'Quantos {v_choice[choice]} deseja adicionar?\nR: '))
      print()
      if ask.is_integer():
        for i in range(ask):
          lista_op[choice].append(input(f'Adicionar {v_choice[choice]} N°{i + 1} ').strip().title()) # adiciona na lista
          # " ".join(nome_estudante.split()) 
      else: 
        return print('Valor Inválido!\n') 
    except:
      return print('Valor Inválido!\n')
  else: # pra saber se é Quantos ou Quantas
    try: # verificação da resposta
      ask = int(input(f'Quantas {v_choice[choice]} deseja adicionar?\nR: '))
      print()
      if ask.is_integer():
        for i in range(ask):
          lista_op[choice].append(input(f'Adicionar {v_choice[choice]} N°{i + 1}: ').strip().title()) # adiciona na lista
      else:
        return print('Valor Inválido!\n')
    except:
      return print('Valor Inválido!\n')
    