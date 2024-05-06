from crud.functions.json.read_json import readJson

def read_admission(data_json:list):
  data_s = readJson('estudantes')
  data_c = readJson('turmas')
  print(f'--------------- [MATRÍCULAS] ---------------')
  print('Cod. Matricula     Cod. Turma     Estudante / Cod.')
  for x in data_json:
    cod_matricula = x['codigo']
    cod_turma = x['codigo_turma'] 
    cod_estudante = x['codigo_estudante'] 
    for xx in data_s:
      if xx['codigo'] == cod_estudante:
        index_estudante = data_s.index(xx)
        break
      else:
        index_estudante = None
    for xxx in data_c:
      if xxx['codigo'] == cod_turma:
        turma = True
        break
      else:
        turma = False

    menssagem = 'Excluído/Não encontrado'
    if index_estudante == None and turma != False:
      print(f'{cod_matricula:>5}{cod_turma:^30}{menssagem}')
    elif turma == False and index_estudante != None:
      print(f'{cod_matricula:>5}{menssagem:^30}{data_s[index_estudante]['nome']}/{cod_estudante}')
    elif index_estudante == None and turma == False:
      print(f'{cod_matricula:>5}{menssagem:^30}{menssagem}')
    else:
      print(f'{cod_matricula:>5}{cod_turma:^30}{data_s[index_estudante]['nome']}/{cod_estudante}')