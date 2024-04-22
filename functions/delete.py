def delete(choice_code:int, data_dict:dict):
  values = [] # valores de cada estudante
  for i in data_dict['estudantes']:
    values  += i.values()

  if choice_code not in values: #verificação se o codigo do aluno existe
    return print('Valor Não Encontrado!')

  for i in data_dict['estudantes']:
    if i['codigo'] == choice_code:
        print()
        print(f'Código do Aluno: {i['codigo']}')
        print(f'Nome do Aluno: {i['nome']}')
        print(f'CPF do Aluno: {i['cpf']}')
        print()
        try:
          delete = int(input(f'Tem certeza que desaja EXCLUIR o aluno {i['nome']}?' 
                             '\n[0] NÃO'
                             '\n[1] SIM'
                             '\nR: '))
        except:
          return print('Valor Inválido!')
        
        if delete == 0:
          print(f'O aluno {i['nome']} não será excluído!')
          break
        else:
          index = data_dict['estudantes'].index(i)
          data_dict['estudantes'].pop(index)
          print(f'O aluno {i['nome']} foi excluído!')

       
          
  