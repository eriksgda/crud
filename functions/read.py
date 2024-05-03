from crud.functions.json.read_json import readJson
from crud.functions.read_functions.read_teacher_student import read_teacherStudent
from crud.functions.read_functions.read_disciplines import read_discipline
from crud.functions.read_functions.read_classes import read_class
from crud.functions.read_functions.read_admissions import read_admission

def read(choice:int, dict_choice:dict):
  file_name = dict_choice[choice].lower()
  data_json = readJson(file_name)
  if choice == 1 or choice == 2:
    read_teacherStudent(choice, dict_choice, data_json)
  elif choice == 3:
    read_discipline(data_json)
  elif choice == 4:
    read_class(data_json)
  elif choice == 5:
    read_admission(data_json)
  else:
    print('EM DESENVOLVIMENTO...')