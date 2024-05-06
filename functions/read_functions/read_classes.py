from crud.functions.json.read_json import readJson

def read_class(data_json:list):
  data_t = readJson('professores')
  data_d = readJson('disciplinas')
  print(f'------------------------- [TURMAS] -------------------------')
  print(f'Cod. Turma            Professores / Cod.         Disciplinas / Cod')
  for x in data_json:
    cod_turma = x['codigo'] 
    cod_professor = x['codigo_prof'] 
    cod_disciplina = x['codigo_disciplina']
    for xx in data_t:
      if xx['codigo'] == cod_professor:
        index_prof = data_t.index(xx)
        break
      else:
        index_prof = None
  
    for xxx in data_d:
      if xxx['codigo'] == cod_disciplina:
        index_disciplina = data_d.index(xxx)
        break
      else:
        index_disciplina = None

    menssagem = 'Excluído/Não encontrado'
    if index_prof == None and index_disciplina != None:
      disciplina = data_d[index_disciplina]['nome'] + ' / ' + str(cod_disciplina)
      print(f'{cod_turma:>5}{menssagem:^50}{disciplina}')
    elif index_disciplina == None and index_prof != None:
      professor = data_t[index_prof]['nome'] + ' / ' + str(cod_professor)
      print(f'{cod_turma:>5}{professor:^50}{menssagem}')
    elif index_prof == None and index_disciplina == None:
      print(f'{cod_turma:>5}{menssagem:^50}{menssagem}')
    else:
      disciplina = data_d[index_disciplina]['nome'] + ' / ' + str(cod_disciplina)
      professor = data_t[index_prof]['nome'] + ' / ' + str(cod_professor)
      print(f'{cod_turma:>5}{professor:^50}{disciplina}')


