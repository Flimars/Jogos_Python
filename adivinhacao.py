import random
print("|********************************|")
print("|Bem vindo ao jogo de Adivinhação|")
print("|********************************|")

num_secret = random.randrangem(0, 101)
tot_tentativas = 3
rodada = 1
# for (rodada in range(1, tot_tentativas)):
while(rodada <= tot_tentativas):
    print("Tentativa {} de {}".format(rodada, tot_tentativas))
    chute_str = input("Digite seu número: ")
    print("Você digitou: ", chute_str)
    chute = int(chute_str)

    acertou = chute == num_secret
    maior   = chute  > num_secret
    menor   = chute  < num_secret

    if(acertou):
        print("|***********************|")
        print("|PARABÉNS! Você acertou!|")
        print("|***********************|")
        break
    else:
        if(maior):
            print("Você errou! - O número digitado é maior.")
            print("\n")
        elif(menor):
            print("Você errou! - O número digitado é menor.")
            print("\n")
           

    rodada = rodada + 1   
print("\n")
print("Fim do Jogo")
