import sys
rok_narozeni = input("Zadej ve kterem roce ses narodil: ")
vek = 2023 - int(rok_narozeni)
print(vek) 
user_input = input('Je tohle tvuj vek? (ano/ne): ')

if user_input.lower() == 'ano':
    print('haha! ja to vedel')
elif user_input.lower() == 'ne':
    print('asi jsem se zardhl o rok...')

input("Stiskni jakoukoli klavesu pro ukonceni programu")
sys.exit() 