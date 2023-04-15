import random #bibilioteca

while True:
    numberRandom = random.randint(0, 10) #gera numero aleatorio
    pontos = 100 #pontos do usuario

    for i in range(5): #laço de repetição para as tentativas
        try:
            numberUser = int(input('Digite um número de 0-10: \n')) #pede ao usuario um numero
            if (numberUser > 10 or numberUser < 0): #verifica se esse valor esta correto
                print('Digite um valor válido')
            else:
                if numberUser == numberRandom: #verifica se o valor é igual ao numero gerado
                    print(f'Parabens, voce acertou na {i+1} tentativa')
                    pontosUser = max(0, pontos - i * 20) #calcula a pontuação do usuario
                    print(f'Sua pontuação final é: {pontosUser} pontos')
                    break #para o laço
                else:
                    if i == 4:
                        print('Suas tentativas acabaram! O número era', numberRandom) #se as tentativas acabarem, retorna o valor gerado
                        pontosUser = max(0, pontos - i * 20)
                        print(f'Sua pontuação final é: {pontosUser} pontos')
                    else:
                        print(f'Tente novamente. Você tem {4-i} tentativas restantes.') #Retorna as tentativas que o usuario possui
                        pontos -= 20
        except ValueError:
            print("Digite um valor válido") #Mensagem de erro para valores não numéricos

    newGame = input('Deseja iniciar uma nova partida? (s/n) \n')
    if newGame.lower() == 's':
        continue #reinicia o laço para uma nova partida
    else:
        print('Fim do jogo!')
        break #encerra o laço e finaliza a aplicação.
