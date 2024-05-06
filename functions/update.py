from crud.functions.json.read_json import readJson
from crud.functions.update_functions.update_teacher_student import update_teacher_student
from crud.functions.update_functions.update_discipline import update_disciplines
from crud.functions.update_functions.update_classes import update_class
from crud.functions.update_functions.update_admissions import update_admission

def update(choice:int, dict_choice:dict):
  file_name = dict_choice[choice].lower()
  datas_json = readJson(file_name)
  match choice:
    case 1:
      update_teacher_student(datas_json, file_name)
    case 2:
      update_teacher_student(datas_json, file_name)
    case 3:
      update_disciplines(datas_json, file_name)
    case 4:
      update_class(datas_json, file_name, dict_choice)
    case 5:
      update_admission(datas_json, file_name, dict_choice)
    case _:
      print('EM DESENVOLVIMENTO...')

          
  