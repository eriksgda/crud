def read(choice:int, dict_choice:dict, dictt:dict):
  print(f'--------------- [{dict_choice[choice]}] ---------------')
  for i in dictt['estudantes']:
    print(f'{i['codigo']:<5}{i['nome']:^30}{i['cpf']:<5}')