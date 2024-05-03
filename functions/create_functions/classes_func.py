import json
from crud.functions.json.read_json import readJson

def classes(choice:int, dict_choice:dict, file_name, datas_json):
  try: # verificação da resposta
    ask = int(input(f'Quantos(as) {dict_choice[choice]} deseja adicionar?\nR: '))
    print()
    if ask.is_integer():
      for _ in range(ask):
        try:
          values= []
          for i in datas_json:
            values  += i.values()

          code_class = int(input(f'Código da {dict_choice[choice].lower()}: ').strip())
          if code_class in values:
            return print('Código já incluso!')
          
          values = []
          for i in readJson('professores'):
            values += i.values()
          code_teacher = int(input(f'Código da {dict_choice[choice - 2].lower()}: ').strip())
          if code_teacher not in values:
            return print('Código do(a) professor(a) inexistente!')
          
          values = []
          for i in readJson('disciplinas'):
            values += i.values()
          code_discipline = int(input(f'Código da {dict_choice[choice - 1].lower()}: ').strip())
          if code_discipline not in values:
            return print('Código da disciplina inexistente!')
          
          print()
          datas_json.append({
            'codigo_c':code_class, 
            'codigo_t' : code_teacher,
            'codigo_d' : code_discipline,
          })
          with open(file_name + '.json', 'w') as file:
            json.dump(datas_json, file, ensure_ascii=False)
            file.close()
        except:
          return print('Valor Inválido!\n')
  except:
    return print('Valor Inválido!\n')
  
