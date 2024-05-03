import json

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