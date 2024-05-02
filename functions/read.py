from crud.functions.json.read_json import readJson

def read(choice:int, dict_choice:dict):
  file_name = dict_choice[choice].lower()
  data_json = readJson(file_name)
  print(f'--------------- [{dict_choice[choice]}] ---------------')
  for student in data_json:
    print(f'{student['codigo']:<5}{student['nome']:^30}{student['cpf']:<5}')