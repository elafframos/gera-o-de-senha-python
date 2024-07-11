import random  #Importação de random para

print('\nGerador de Senhas!\n')

caracteres = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%¨&*().,1234567890'

numero = int(input('Digite o número de senhas que você deseja: '))

quantidade = int(input('Digite a quantidade de caracteres que você deseja em sua senha: '))

print('\nEssa é a sua senha: ')

#Gerador de senhas aleátorios!
for senha in range(numero):
    senhas = ''
    for s in range(quantidade):
        senhas += random.choice(caracteres)
        print(senhas)
