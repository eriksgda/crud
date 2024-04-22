# penso em criar uma função apra cada uma das opções, ou ter apenas uma função com varios cases 

def create(choice:int, dict_choice:dict, data_dict:dict): # função que adiciona (incluir) nas listas
  match choice:
    case 1:
      try: # verificação da resposta
        ask = int(input(f'Quantos {dict_choice[choice]} deseja adicionar?\nR: '))
        print()
        if ask.is_integer():
          for _ in range(ask):
            try:
              code = int(input('Código do estudante: ').strip())
              student = input('Nome do Estudante: ').strip()
              cpf = int(input('Digite o cpf: ').strip())
              print()
              data_dict['estudantes'].append({
                'codigo':code, 
                'nome' : student,
                'cpf' : cpf
                })
            except:
              return print('Valor Inválido!\n')
      except:
        return print('Valor Inválido!\n')
    case _:
      print('EM DESENVOLVIMENTO...')
