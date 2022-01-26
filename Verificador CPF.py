"""
CPF = 168.995.350-09
______________________
1 * 10 = 10              #       1 * 11 = 11
6 * 9 = 54               #       6 * 10  = 60
8 * 8 = 64               #       8 * 9 = 72
9 * 7 = 63               #       9 * 8 = 72
9 * 6 = 54               #       9 * 7 = 63
5 * 5 = 25               #       5 * 6 = 30
3 * 4  = 12              #       3 * 5 = 15
5 * 3 = 15               #       5 * 4 = 20
0 * 2 = 0                #       0 * 3 = 0
                         #       0 * 2 = 0
11 - (297 % 11) = 11     #    11 - (343 % 11) = 9
11 > 9 = 0               #      Digito 2 = 9
Digito 1 = 0             #

"""

cpf = input("Digite seu cpf: ").replace(".", "").replace("-", "")
cpf_verif = cpf[:9]

if cpf_verif.isnumeric():

    contador = 0
    soma = 0

    for numero in cpf_verif:
        if contador < 9:
            multi = int(numero) * (10 - contador)
            soma = soma + multi
            contador += 1

    conta_dig_1 = 11 - (soma % 11)

    if conta_dig_1 > 9:
        dig_1 = "0"
    else:
        dig_1 = str(conta_dig_1)

    cpf_verif = cpf_verif + dig_1

    contador = 0
    soma = 0
    for numero_2 in cpf_verif:
        if contador <= 9:
            multi = int(numero_2) * (11 - contador)
            soma = soma+ multi
            contador += 1

    conta_dig_2 = 11 - (soma % 11)
    if conta_dig_2 > 9:
        dig_2 = "0"
    else:
        dig_2 = str(conta_dig_2)

    cpf_verif = cpf_verif + dig_2

    print("O CPF ESTA CORRETO" if cpf_verif == cpf else "CPF INCORRETO")

else:
    print("O FORMATO QUE VOCÊ DIGITOU ESTÁ INCORETTO!!!!")






