from crud.functions.json.read_json import readJson
from crud.functions.create_functions.student_teacher import student_and_teacher
from crud.functions.create_functions.discipline_func import discipline
from crud.functions.create_functions.classes_func import classes
from crud.functions.create_functions.admissions_func import admission


def create(choice:int, dict_choice:dict): # função que adiciona (incluir) nas listas
  file_name = dict_choice[choice].lower()
  datas_json = readJson(file_name)
  match choice:
    case 1:
      student_and_teacher(choice, dict_choice, file_name, datas_json)
    case 2:
      student_and_teacher(choice, dict_choice, file_name, datas_json)
    case 3:
      discipline(file_name, datas_json)
    case 4:
      classes(file_name, datas_json)
    case 5:
      admission(file_name, datas_json)
    case _:
      print('EM DESENVOLVIMENTO...')