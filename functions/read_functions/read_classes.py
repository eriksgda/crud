from crud.functions.json.read_json import readJson

def read_class(data_json:list):
  data_t = readJson('professores')
  data_d = readJson('disciplinas')
  print(f'--------------- [TURMAS] ---------------')
  print('Cod.               Nome             Nome\n'
        'Turma           Professores        Disciplinas')
  for x in data_json:
    cod_turma = x['codigo_c'] 
    cod_professor = x['codigo_t'] 
    cod_disciplina = x['codigo_d']
    for xx in data_t:
      if xx['codigo'] == cod_professor:
        index_prof = data_t.index(xx)
        break
    for xxx in data_d:
      if xxx['codigo'] == cod_disciplina:
        index_disciplina = data_d.index(xxx)
        break
    print(f'{cod_turma:<5}{data_t[index_prof]['nome']:^30}{data_d[index_disciplina]['nome']:<5}')