import json
from crud.functions.json.read_json import readJson  

def admission(file_name:str, datas_json:list):
  try: # verificação da resposta
    ask = int(input('Quantas MATRÍCULAS deseja adicionar?\nR: '))
    print()
    for _ in range(ask):
        try:
          values = []
          for i in datas_json:
            values.append(i['codigo'])
          code_admission = int(input('Código da Matrícula: ').strip())
          if code_admission in values:
            return print('Código em uso!')
          
          values = []
          for i in readJson('turmas'):
            values.append(i['codigo'])
          code_classes = int(input('Código da turma: ').strip())
          if code_classes not in values:
            return print('Código da turma inexistente!')
          
          values = []
          for i in readJson('estudantes'):
            values.append(i['codigo'])
          code_student = int(input('Código do(a) estudante: ').strip())
          if code_student not in values:
            return print('Código do(a) estudante inexistente!')
          
          print()
          datas_json.append({
            'codigo' : code_admission,
            'codigo_turma' : code_classes,
            'codigo_estudante' : code_student
          })
          with open(file_name + '.json', 'w') as file:
            json.dump(datas_json, file, ensure_ascii=False)
            file.close()
        except:
          return print('Valor Inválido!\n')
  except:
    return print('Valor Inválido!\n')
