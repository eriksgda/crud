from crud.functions.json.read_json import readJson

def read_admission(data_json:list):
  data_s = readJson('estudanteS')
  print(f'--------------- [MATRÍCULAS] ---------------')
  print('Cod. Turmas                    Nome Estudante')
  for x in data_json:
    cod_turma = x['codigo_c'] 
    cod_estudante = x['codigo_s'] 
    for xx in data_s:
      if xx['codigo'] == cod_estudante:
        index_estudante = data_s.index(xx)
        break
    print(f'{cod_turma:<5}{data_s[index_estudante]['nome']:^30}')