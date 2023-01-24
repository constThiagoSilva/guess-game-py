from getRandomNumber import get_random_number

print('JOGO DO ADIVINHA NÚMEROS \n' + '-' * 50)

while True:
    try:
        minimum_range = int(input('Insira um número minimo para adivinhar: \n'))
        print('-' * 50)
        maximum_range = int(input('Insira um número máximo para adivinhar: \n'))
        print('-' * 50)
        
        number_to_be_guessed = get_random_number(minimum_range, maximum_range)
        while True:
            while True:
                try:
                    chosen_number_by_user = int(input('Insira o número que voce ache ser o certo: \n'))
                    print('-' * 50)

                    if chosen_number_by_user > maximum_range or chosen_number_by_user < minimum_range:
                        raise

                    if number_to_be_guessed == chosen_number_by_user:
                        print('Parabens! Voce ganhou.')
                        isExit = input('Voce quer continuar: s/n \n')

                        if 'n' in isExit:
                            break

                        minimum_range = int(input('Insira um número minimo para adivinhar: \n'))
                        print('-' * 50)
                        
                        maximum_range = int(input('Insira um número máximo para adivinhar: \n'))
                        print('-' * 50)
        
                        number_to_be_guessed = get_random_number(minimum_range, maximum_range)
                    elif number_to_be_guessed > chosen_number_by_user:
                        print('Tente um número mais alto. \n')
                    else:
                        print('Tente um número mais baixo. \n')
                except:
                    print('Insira um número entre os números dados')
            break
        break
    except:
        print('Insira um número válido!!!!')
