from crud.functions.json.read_json import readJson

def read(choice:int, dict_choice:dict):
  if choice != 5 and choice != 4 and choice !=3:
    file_name = dict_choice[choice].lower()
    data_json = readJson(file_name)
    print(f'--------------- [{dict_choice[choice]}] ---------------')
    print('Codigo              Nome              CPF')
    for x in data_json:
      print(f'{x['codigo']:<5}{x['nome']:^30}{x['cpf']:<5}')
  elif choice == 3:
    file_name = dict_choice[choice].lower()
    data_json = readJson(file_name)
    print(f'--------------- [{dict_choice[choice]}] ---------------')
    print('Codigo                           Nome')
    for x in data_json:
      print(f'{x['codigo']:<5}{x['nome']:^30}')
  elif choice == 4:
    file_name = dict_choice[choice].lower()
    data_json = readJson(file_name)
    print(f'--------------- [{dict_choice[choice]}] ---------------')
    print('Cod.               Cod.             Cod.\n'
          'Turma           Professores        Disciplinas')
    for x in data_json:
      print(f'{x['codigo_c']:<5}{x['codigo_t']:^30}{x['codigo_d']:<5}')
  elif choice == 5:
    file_name = dict_choice[choice].lower()
    data_json = readJson(file_name)
    print(f'--------------- [{dict_choice[choice]}] ---------------')
    print('Cod. Turmas              Cod. Estudantes          Nome Estudante')
    for x in data_json:
      print(f'{x['codigo_c']:<5}{x['codigo_s']:^30}')
