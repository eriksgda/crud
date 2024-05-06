import json
from crud.functions.json.read_json import readJson
from crud.functions.read import read
def update_admission(datas_json:list, file_name:str, dict_choice:dict):
  try:
    choice_update = int(input('O que deseja alterar:\n' 
                              '[0] Código de Turma\n'
                              '[1] Código do(a) Estudante\nR:  ').strip())
  except:
    return print('Valor inválido!')
  try:
    choice_code = int(input('Digite o código da matrícula que deseja alterar: '))
  except:
    return print('Valor inválido!')
  
  values = [] # valores de cada estudante
  for i in datas_json:
    values.append(i['codigo'])

  if choice_code not in values: # verificação se o código existe
    return print('Código Não Encontrado!')

  for i in datas_json:
    if i['codigo'] == choice_code:
      if choice_update == 0: # verificação se vai alterar o código da turma
        print()
        read(4, dict_choice)
        print()
        try:
          update_ = int(input('Novo código: '))
        except:
          return print('Valor Inválido!')
        data_c = readJson('turmas')
        values = []
        for x in data_c:
          values.append(x['codigo'])
        if update_ in values:
          i['codigo_turma'] = update_
          with open(file_name + '.json', 'w') as file:
            json.dump(datas_json, file, ensure_ascii=False)
            file.close()
          break
        else:
          print('Código da turma inexistente!')
          break
      elif choice_update == 1: # verificação se vai alterar o codigo do estudante
        print()
        read(1, dict_choice)
        print()
        try:
          update_ = int(input('Novo código: '))
        except:
          return print('Valor Inválido!')
        data_s = readJson('estudantes')
        values = []
        for x in data_s:
          values.append(x['codigo'])
        if update_ in values:
          i['codigo_estudante'] = update_
          with open(file_name + '.json', 'w') as file:
            json.dump(datas_json, file, ensure_ascii=False)
            file.close()
          break
        else:
          print('Código do(a) estudante inexistente!')
          break