from getRandomNumber import get_random_number

print('JOGO DO ADIVINHA NÚMEROS \n' + '-' * 60)

while True:
    try:
        minimum_range = int(input('insira um número minimo para adivinhar:'))
        maximum_range = int(input('insira um número máximo para adivinhar'))
        
        number_to_be_guessed = get_random_number(minimum_range, maximum_range)

        while True:
            while True:
                try:
                    chosen_number_by_user = int(input('insira o número que voce ache ser o certo:'))



                    if chosen_number_by_user > maximum_range or chosen_number_by_user < minimum_range:
                        raise

                    print(chosen_number_by_user, number_to_be_guessed)

                    if number_to_be_guessed == chosen_number_by_user:
                        print('Parabens! Voce ganhou')
                        isExit = input('Voce quer continuar: s/n')

                        if 'n' in isExit:
                            break

                    elif number_to_be_guessed > chosen_number_by_user:
                        print('Tente um número mais alto!')
                    else:
                        print('Tenter um número mais baixo!')
                except:
                    print('insira um numero entre os numeros dados')
            break
        break
    except:
        print('insira um número válido!!!!')
