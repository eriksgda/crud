import json

def update_disciplines(datas_json:list, file_name:str):
  try:
    choice_code = int(input('Digite o código da disciplina que deseja alterar: '))
  except:
    return print('Valor inválido!')
  
  values = [] # valores de cada estudante
  for i in datas_json:
    values  += i.values()

  if choice_code not in values: # verificação se o código existe
    return print('Código Não Encontrado!')

  for i in datas_json:
    if i['codigo'] == choice_code:
      print()
      print(f'Disciplina Antiga: {i['nome']}')
      update_ = input('Nova Disciplina:').title()
      if update_ not in values:
        i['nome'] = update_
        with open(file_name + '.json', 'w') as file:
          json.dump(datas_json, file, ensure_ascii=False)
          file.close()
        break
      else:
        print('Disciplina já incluso nos dados!')
        break
