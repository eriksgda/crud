
def update(choice_update:int, data_dict:dict):
  try:
    choice_code = int(input('Digite o código do aluno que deseja alterar: '))
  except:
    return print('Valor inválido!')
  
  values = [] # valores de cada estudante
  for i in data_dict['estudantes']:
    values  += i.values()

  if choice_code not in values: # verificação se o código existe
    return print('Valor Não Encontrado!')

  for i in data_dict['estudantes']:
    if i['codigo'] == choice_code:
      if choice_update == 0: # verificação se vai alterar o nome
        print()
        print(f'Nome Antigo: {i['nome']}')
        update_ = input('Novo nome:').title()
        if update_ not in values:
          i['nome'] = update_
          break
        else:
          print('Nome já incluso nos dados!')
          break
      elif choice_update == 1: # verificação se vai alterar o cpf
        print()
        print(f'CPF Antigo: {i['cpf']}')
        try:
          update_ = int(input('Novo CPF:'))
        except:
          return print('Valor Inválido!')
        if update_ not in values:
          i['cpf'] = update_
          break
        else:
          print('CPF já incluso nos dados!')
          break

          
  