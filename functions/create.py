# penso em criar uma função apra cada uma das opções, ou ter apenas uma função com varios cases
import json
from crud.functions.json.read_json import readJson

def create(choice:int, dict_choice:dict): # função que adiciona (incluir) nas listas
  file_name = dict_choice[choice].lower()
  datas_json = readJson(file_name)
  match choice:
    case 1:
      try: # verificação da resposta
        ask = int(input(f'Quantos {dict_choice[choice]} deseja adicionar?\nR: '))
        print()
        if ask.is_integer():
          for _ in range(ask):
            try:
              code = int(input('Código do estudante: ').strip())
              student = input('Nome do Estudante: ').strip()
              cpf = int(input('Digite o cpf: ').strip())
              print()
              datas_json.append({
                'codigo':code, 
                'nome' : student,
                'cpf' : cpf
                })
              with open(file_name + '.json', 'w') as file:
                json.dump(datas_json, file, ensure_ascii=False)
                file.close()
            except:
              return print('Valor Inválido!\n')
      except:
        return print('Valor Inválido!\n')
    case _:
      print('EM DESENVOLVIMENTO...')
