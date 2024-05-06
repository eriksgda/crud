def read_discipline(data_json:list):
  print(f'--------------- [DISCIPLINAS] ---------------')
  print(' Codigo                           Nome')
  for x in data_json:
    print(f'{x['codigo']:>5}{x['nome']:>35}')