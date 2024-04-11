from functions import menu, menu_operations, operation, include


v_choice = {
  0: 'Finalizando Aplicação...',
  1: 'ESTUDANTES',
  2: 'PROFESSORES',
  3: 'DISCIPLINAS',
  4: 'TURMAS',
  5: 'MATRÍCULAS'
}

v_choice_op = {
   0: 'Operação não adicionada...',
   1: 'INCLUIR',
   2: 'LISTAR',
   3: 'ATUALIZAR',
   4: 'EXCLUIR',
   5: 'VOLTAR AO MENU'
}

lista_op ={
1: [],
2: [],
3: [],
4: [],
5: []
}


while True: # loop do menu
  choice = menu()  # escolha principal
  
  while choice not in v_choice:  # verificação se é um valor aceito
    choice = menu()
    
  if choice == 0:     # verificação se é 0 para encerramento do programa
    print(v_choice[choice])
    break
  
  while True:   # loop do menu de operações
    choice_op = menu_operations(v_choice, choice)  # escolha da operação

    while choice_op not in v_choice_op:  # verificação se é um valor aceito
        choice_op = menu_operations(v_choice, choice)

    if choice_op == 0:  # verificação se é 0 para encerramento do programa
      break
    
    continuar = 1
    while continuar == 1: # loop que contem cada operação
      match(choice_op):
        case 1: # incluir
          operation(v_choice_op, choice_op)
          include(choice, v_choice, lista_op)
        case 2: # listar
          operation(v_choice_op, choice_op)
          lista_op[choice].sort()
          count = 1
          print(f'/////////// [{v_choice[choice]}] ///////////')
          for i in lista_op[choice]:
            print(f'N°{count}: {i}')
            count += 1
        case 3: # atualizar
          operation(v_choice_op, choice_op)
          print('EM DESENVOLVIMENTO...')
          break
        case 4: # excluir
          operation(v_choice_op, choice_op)
          print('EM DESENVOLVIMENTO...')
          break
        case 5: # voltar ao menu
          operation(v_choice_op, choice_op)
          break       
      continuar = input('Digite 1 para continuar no menu de operações ' 
                          f'[{v_choice_op[choice_op]}] e 0 para voltar ao menu [{v_choice[choice]}]\nR: ').strip()
      if continuar == '1' or continuar == '0': # vereficação da variavel 'continuar'
        continuar = int(continuar)
      else:
        print('Valor inválido!')
        continue
      
    if choice_op == 5: # verificar se é para voltar ao menu principal
      break

  if choice_op == 0: # verificação se deve encerrar o programa
    print(v_choice[choice_op])
    break
  else:
    continue
