# penso em criar uma função apra cada uma das opções, ou ter apenas uma função com varios cases
import json
from crud.functions.json.read_json import readJson

def student_and_teacher(choice:int, dict_choice:dict, file_name, datas_json):
  try: # verificação da resposta
    ask = int(input(f'Quantos(as) {dict_choice[choice]} deseja adicionar?\nR: '))
    print()
    if ask.is_integer():
      for _ in range(ask):
        try:
          values= []
          for i in datas_json :
            values  += i.values()

          code = int(input(f'Código do {dict_choice[choice].lower()}: ').strip())
          if code in values:
            return print('Código já incluso!')
          name = input(f'Nome do {dict_choice[choice].lower()}: ').strip()
          if name in values:
            return print('Nome já incluso!')
          cpf = int(input('Digite o cpf: ').strip())
          if cpf in values:
            return print('CPF já incluso!')
          print()
          datas_json.append({
            'codigo':code, 
            'nome' : name,
            'cpf' : cpf
            })
          with open(file_name + '.json', 'w') as file:
            json.dump(datas_json, file, ensure_ascii=False)
            file.close()
        except:
          return print('Valor Inválido!\n')
  except:
    return print('Valor Inválido!\n')

def discipline(choice:int, dict_choice:dict, file_name, datas_json):
  try: # verificação da resposta
    ask = int(input(f'Quantos(as) {dict_choice[choice]} deseja adicionar?\nR: '))
    print()
    if ask.is_integer():
      for _ in range(ask):
        try:
          values= []
          for i in datas_json :
            values  += i.values()

          code = int(input(f'Código da {dict_choice[choice].lower()}: ').strip())
          if code in values:
            return print('Código já incluso!')
          name = input(f'Nome da {dict_choice[choice].lower()}: ').strip()
          if code in values:
            return print('Nome já incluso!')
          print()
          datas_json.append({
            'codigo':code, 
            'nome' : name
          })
          with open(file_name + '.json', 'w') as file:
            json.dump(datas_json, file, ensure_ascii=False)
            file.close()
        except:
          return print('Valor Inválido!\n')
  except:
    return print('Valor Inválido!\n')
  

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
          if code_teacher in values:
            return print('Código já incluso!')
          
          values = []
          for i in readJson('disciplinas'):
            values += i.values()
          code_discipline = int(input(f'Código da {dict_choice[choice - 1].lower()}: ').strip())
          if code_discipline in values:
            return print('Código já incluso!')
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
  

def matriculas(choice:int, dict_choice:dict, file_name, datas_json):
  try: # verificação da resposta
    ask = int(input(f'Quantos(as) {dict_choice[choice]} deseja adicionar?\nR: '))
    print()
    if ask.is_integer():
      for _ in range(ask):
        try:
          values = []
          for i in readJson('turma'):
            values += i.values()
          code_classes = int(input(f'Código da {dict_choice[choice - 1].lower()}: ').strip())
          if code_classes in values:
            return print('Código já incluso!')
          
          values = []
          for i in readJson('estudantes'):
            values += i.values()
          code_student = int(input(f'Código do {dict_choice[choice - 4].lower()}: ').strip())
          if code_student in values:
            return print('Código já incluso!')
          print()
          datas_json.append({
            'codigo_c' : code_classes,
            'codigo_s' : code_student
          })
          with open(file_name + '.json', 'w') as file:
            json.dump(datas_json, file, ensure_ascii=False)
            file.close()
        except:
          return print('Valor Inválido!\n')
  except:
    return print('Valor Inválido!\n')

def create(choice:int, dict_choice:dict): # função que adiciona (incluir) nas listas
  file_name = dict_choice[choice].lower()
  datas_json = readJson(file_name)
  match choice:
    case 1:
      student_and_teacher(choice, dict_choice, file_name, datas_json)
    case 2:
      student_and_teacher(choice, dict_choice, file_name, datas_json)
    case 3:
      discipline(choice, dict_choice, file_name, datas_json)
    case 4:
      classes(choice, dict_choice, file_name, datas_json)
    case 5:
      matriculas(choice, dict_choice, file_name, datas_json)
    case _:
      print('EM DESENVOLVIMENTO...')
