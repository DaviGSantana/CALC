from os import system

while True:
    system('clear')

    print('Escolha uma opção: ')
    print('1 - Soma')
    print('2 - Subtração')
    print('3 - Multiplicação')
    print('4 - Divisão')
    print('5 - Raiz')
    print('6 - Sair')

    try: 
        cmd = int(input('Escolha a opção: '))
    except:
        print('Apenas numeros')
        exit()

    if cmd == 1:
        n1 = int(input(f'Numero_1: '))
        n2 = int(input(f'Numero_2: '))
        print(f"Resultado da soma é: {n1+n2}")
        input(f"[*] - Pressione enter para voltar ao menu.")
  
    elif cmd == 2:
        n1 = int(input('Numero_1: '))
        n2 = int(input('Numero_2: '))
        print(f"Resultado da subtração é: ", n1-n2)
        input(f"[*] - Pressione enter para voltar ao menu.")

    elif cmd == 3:
        n1 = int(input('Numero_1: '))
        n2 = int(input('Numero_2: '))
        print(f"Resultado da multiplicação: ", n1*n2)
        input(f"[*] - {Y}Pressione enter para voltar ao menu.")

    elif cmd == 4:
        n1 = int(input('Numero_1: '))
        n2 = int(input('Numero_2: '))
        print(f"Resultado da divisão: ", n1/n2)
        input(f"[*] - Pressione enter para voltar ao menu.")

    elif cmd == 5:
        n1 = float(input('Numero_1: '))
        print("Resultado da raiz: ", math.sqrt(n1))
        input(f"[*] - Pressione enter para voltar ao menu.")
    elif cmd == 6:
        print(f"[!] - SAINDO....")
        sleep(2)
        exit()

    else:
        print(f"[!] - Opção Invalida! :(")
        exit()  