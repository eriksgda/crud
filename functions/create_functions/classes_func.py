import json
from functions.json.read_json import readJson

def classes(file_name:str, datas_json:list):
  try: # verificação da resposta
    ask = int(input(f'Quantas TURMAS deseja adicionar?\nR: '))
    print()
    if ask.is_integer():
      for _ in range(ask):
        try:
          values= []
          for i in datas_json:
            values.append(i['codigo'])

          code_class = int(input('Código da turma: ').strip())
          if code_class in values:
            return print('Código já incluso!')
          
          values = []
          for i in readJson('professores'):
            values.append(i['codigo'])
          code_teacher = int(input('Código do(a) professor(a): ').strip())
          if code_teacher not in values:
            return print('Código do(a) professor(a) inexistente!')
          
          values = []
          for i in readJson('disciplinas'):
            values.append(i['codigo'])
          code_discipline = int(input('Código da disciplina: ').strip())
          if code_discipline not in values:
            return print('Código da disciplina inexistente!')
          
          print()
          datas_json.append({
            'codigo':code_class, 
            'codigo_prof' : code_teacher,
            'codigo_disciplina' : code_discipline,
          })
          with open(file_name + '.json', 'w') as file:
            json.dump(datas_json, file, ensure_ascii=False)
            file.close()
        except:
          return print('Valor Inválido!\n')
  except:
    return print('Valor Inválido!\n')
  
