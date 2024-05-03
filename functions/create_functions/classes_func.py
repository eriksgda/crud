import json
from crud.functions.json.read_json import readJson

def classes(file_name:str, datas_json:list):
  try: # verificação da resposta
    ask = int(input(f'Quantas TURMAS deseja adicionar?\nR: '))
    print()
    if ask.is_integer():
      for _ in range(ask):
        try:
          values= []
          for i in datas_json:
            values  += i.values()

          code_class = int(input('Código da turma: ').strip())
          if code_class in values:
            return print('Código já incluso!')
          
          values = []
          for i in readJson('professores'):
            values += i.values()
          code_teacher = int(input('Código do(a) professor(a): ').strip())
          if code_teacher not in values:
            return print('Código do(a) professor(a) inexistente!')
          
          values = []
          for i in readJson('disciplinas'):
            values += i.values()
          code_discipline = int(input('Código da disciplina: ').strip())
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
  
