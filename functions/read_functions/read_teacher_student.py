
def read_teacherStudent(choice:int, dict_choice:dict, data_json:list):
  print(f'--------------- [{dict_choice[choice]}] ---------------')
  print('Codigo              Nome              CPF')
  for x in data_json:
    print(f'{x['codigo']:>5}{x['nome']:^30}{x['cpf']}')
