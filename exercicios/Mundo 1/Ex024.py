#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "santo"
city = str(input('Insira o nome de uma cidade:  '))
city = city.title().split()
print('O nome da cidade começa com "Santo?', 'Santo' in city[0])


'''if resp == True:
    print('A cidade inserida possui a palavra "Santo".')
else :
    print('A cidade inserida NÃO possui a palavra "Santo".')'''