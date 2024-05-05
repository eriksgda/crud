import json
from crud.functions.json.read_json import readJson

def delete(choice_code:int, choice:int, dict_choice:dict):
  file_name = dict_choice[choice].lower()
  datas_json = readJson(file_name)
  values = [] # valores de cada estudante
  for i in datas_json :
    values.append(i['codigo'])

  if choice_code not in values: #verificação se o codigo do aluno existe
    return print('Valor Não Encontrado!')

  for i in datas_json:
    if i['codigo'] == choice_code:
        try:
          delete = int(input(f'Tem certeza que desaja EXCLUIR?' 
                             '\n[0] NÃO'
                             '\n[1] SIM'
                             '\nR: '))
        except:
          return print('Valor Inválido!')
        
        if delete == 0:
          print()
          print(f'Não será excluído!')
          break
        else:
          index = datas_json.index(i)
          datas_json.pop(index)
          with open(file_name + '.json', 'w') as file:
            json.dump(datas_json, file, ensure_ascii=False)
            file.close()
          print()
          print(f'Excluído com sucesso!')

       
          
  