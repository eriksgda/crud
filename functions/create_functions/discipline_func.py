import json

def discipline(file_name:str, datas_json:list):
  try: # verificação da resposta
    ask = int(input(f'Quantas DISCIPLINAS deseja adicionar?\nR: '))
    print()
    if ask.is_integer():
      for _ in range(ask):
        try:
          values= []
          for i in datas_json :
            values  += i.values()

          code = int(input('Código da disciplina: ').strip())
          if code in values:
            return print('Código já incluso!')
          
          name = input('Nome da disciplina: ').strip()
          if code in values or not name:
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