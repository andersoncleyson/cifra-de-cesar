print(10 * '=', 'CIFRA DE CEZAR', 10 * '=')


ed = input('Você deseja encriptar ou desencriptar? E/D: ')

if ed == 'E' or ed == 'e':
    palavra = str(input("Digite qualquer texto para criptografar: "))
    palavra = list(palavra)

    alfa = list(' ABCDEFGHIJKLMNOPQRSTUVWXYZ')

    indice = -1
    cont = -1
    for p in palavra:
    
        for letra in alfa:
            cont += 1
            if letra == p:
                indice += 1
                if letra == 'X':
                    cont = -2
                if letra == 'Y':
                    cont = -1
                if letra == 'Z':
                    cont = 0
                if letra == ' ':
                    palavra[indice] = alfa[0]
                    cont = - 1
                else:
                    palavra[indice] = alfa[cont + 3]
                    cont = -1
                break
    palavra = ''.join(palavra)
    print('')
    print('-' * 10, 'TEXTO CRIPTOGRAFADO', '-' * 10)
    print(palavra)

if ed == 'D' or ed == 'd':
    crip = str(input("INSIRA O TEXTO CRIPTADO: "))
    crip = list(crip)

    alfa_crip = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ ')

    indice = -1
    cont = -1
    for p in crip:
    
        for letra in alfa_crip:
            cont += 1
            if letra == p:
                indice += 1
                if letra == 'A':
                    cont = 26
                if letra == 'B':
                    cont = 27
                if letra == 'C':
                    cont = 28
                if letra == ' ':
                    crip[indice] = alfa_crip[26]
                    cont = -1
                else:
                    crip[indice] = alfa_crip[cont - 3]
                    cont = -1
                break
    crip = ''.join(crip)
    print('')
    print('-' * 10, 'TEXTO DESINCRIPTOGRAFADO', '-' * 10)
    print(crip)
