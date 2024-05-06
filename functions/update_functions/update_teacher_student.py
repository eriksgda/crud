import json

def update_teacher_student(datas_json:list, file_name:str):
  try:
    choice_update = int(input('O que deseja alterar:\n' 
                              '[0] Nome\n'
                              '[1] CPF\nR:  ').strip())
  except:
    return print('Valor inválido!')
  try:
    choice_code = int(input('Digite o código de quem deseja alterar: '))
  except:
    return print('Valor inválido!')
  
  values = [] # valores de cada estudante
  for i in datas_json:
    values  += i.values()

  if choice_code not in values: # verificação se o código existe
    return print('Código Não Encontrado!')

  for i in datas_json:
    if i['codigo'] == choice_code:
      if choice_update == 0: # verificação se vai alterar o nome
        print()
        print(f'Nome Antigo: {i['nome']}')
        update_ = input('Novo nome:').title()
        if update_ not in values:
          i['nome'] = update_
          with open(file_name + '.json', 'w') as file:
            json.dump(datas_json, file, ensure_ascii=False)
            file.close()
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
          with open(file_name + '.json', 'w') as file:
            json.dump(datas_json, file, ensure_ascii=False)
            file.close()
          break
        else:
          print('CPF já incluso nos dados!')
          break
