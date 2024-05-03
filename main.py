from functions.menus import menu, menu_operations, operation
from crud.functions.create import create
from functions.read import read
from functions.update import update
from functions.delete import delete


dict_choice = {
  0: 'Finalizando Aplicação...',
  1: 'ESTUDANTES',
  2: 'PROFESSORES',
  3: 'DISCIPLINAS',
  4: 'TURMAS',
  5: 'MATRÍCULAS'
}

dict_choice_op = {
   0: 'Operação não adicionada...',
   1: 'INCLUIR',
   2: 'LISTAR',
   3: 'ATUALIZAR',
   4: 'EXCLUIR',
   5: 'VOLTAR AO MENU'
}

while True: # loop do menu
  choice = menu()  # escolha principal
  
  while choice not in dict_choice:  # verificação se é um valor aceito
    choice = menu()
    
  if choice == 0:     # verificação se é 0 para encerramento do programa
    print(dict_choice[choice])
    break
  
  while True:   # loop do menu de operações
    choice_op = menu_operations(dict_choice, choice)  # escolha da operação

    while choice_op not in dict_choice_op:  # verificação se é um valor aceito
        choice_op = menu_operations(dict_choice, choice)

    if choice_op == 0:  # verificação se é 0 para encerramento do programa
      break
    
    continuar = 1
    while continuar == 1: # loop que contem cada operação
      match(choice_op):
        case 1: # incluir
          operation(dict_choice_op, choice_op)
          create(choice, dict_choice)
          print()

        case 2: # listar
          operation(dict_choice_op, choice_op)
          read(choice, dict_choice)
          print()

        case 3: # atualizar
          operation(dict_choice_op, choice_op)
          try:
            choice_update = int(input('O que deseja alterar:\n' 
                            '[0] Nome do Estudante\n'
                            '[1] CPF do Estudante\nR:  ').strip())
          except:
            print('Valor inválido!')
            break
          print()
          read(choice, dict_choice)
          print()
          update(choice_update, choice, dict_choice)
          print()

        case 4: # excluir
          operation(dict_choice_op, choice_op)
          read(choice, dict_choice)
          try:
            choice_code = int(input('Digite o código do aluno que deseja excluir: '))
          except:
            print('Valor inválido!')
            break
          print()
          delete(choice_code, choice, dict_choice)    
          print()  

        case 5: # voltar ao menu
          operation(dict_choice_op, choice_op)
          break       
      continuar = input('Digite 1 para continuar no menu de operações ' 
                          f'[{dict_choice_op[choice_op]}] e 0 para voltar ao menu [{dict_choice[choice]}]\nR: ').strip()
      if continuar == '1' or continuar == '0': # vereficação da variavel 'continuar'
        continuar = int(continuar)
      else:
        print('Valor inválido!')
        continue
      
    if choice_op == 5: # verificar se é para voltar ao menu principal
      break

  if choice_op == 0: # verificação se deve encerrar o programa
    print(dict_choice[choice_op])
    break
  else:
    continue
