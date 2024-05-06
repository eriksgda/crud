import json
from crud.functions.json.read_json import readJson
from crud.functions.read import read

def update_class(datas_json:list, file_name:str, dict_choice:dict):
  try:
    choice_update = int(input('O que deseja alterar:\n' 
                              '[0] Código do(a) Professor(a)\n'
                              '[1] Código da Disciplina\nR:  ').strip())
  except:
    return print('Valor inválido!')
  try:
    choice_code = int(input('Digite o código da turma que deseja alterar: '))
  except:
    return print('Valor inválido!')
  
  values = [] # valores de cada estudante
  for i in datas_json:
    values.append(i['codigo'])

  if choice_code not in values: # verificação se o código existe
    return print('Código Não Encontrado!')

  for i in datas_json:
    if i['codigo'] == choice_code:
      if choice_update == 0: # verificação se vai alterar o código do professor
        print()
        read(2, dict_choice)
        print()
        try:
          update_ = int(input('Novo código: '))
        except:
          return print('Valor Inválido!')
        data_t = readJson('professores')
        values = []
        for x in data_t:
          values.append(x['codigo'])
        if update_ in values:
          i['codigo_prof'] = update_
          with open(file_name + '.json', 'w') as file:
            json.dump(datas_json, file, ensure_ascii=False)
            file.close()
          break
        else:
          print('Código do(a) professor(a) inexistente!')
          break
      elif choice_update == 1: # verificação se vai alterar a disciplina
        print()
        read(3, dict_choice)
        print()
        try:
          update_ = int(input('Novo código: '))
        except:
          return print('Valor Inválido!')
        data_d = readJson('disciplinas')
        values = []
        for x in data_d:
          values.append(x['codigo'])
        if update_ in values:
          i['codigo_disciplina'] = update_
          with open(file_name + '.json', 'w') as file:
            json.dump(datas_json, file, ensure_ascii=False)
            file.close()
          break
        else:
          print('Código de dsiciplina inexistente!')
          break