# ======================== Functions definition ==========================
def input_to_digit(string):
    number = input(string)
    while not number.isnumeric():
        print("Insira apenas dígitos.\n")
        number = input(string)
    number = int(number)
    return number


def get_digit():
    numeric_string = input()
    while not numeric_string.isnumeric():
        print("Insira apenas dígitos.\n")
        input()
    number = int(numeric_string)
    return number


def computador_escolhe_jogada(n, m):
    removed_pieces = 0
    while removed_pieces == 0 or (n - removed_pieces) % (m + 1) != 0:
        removed_pieces += 1
    if removed_pieces <= m and removed_pieces <= n:
        if removed_pieces > 1:
            print(f"O computador tirou {removed_pieces} peças.")
        else:
            print(f"O computador tirou {removed_pieces} peça.")
        return removed_pieces


def usuario_escolhe_jogada(n, m):
    s = "Quantas peças você vai tirar? "
    removed_pieces = input_to_digit(s)
    while removed_pieces == 0 or removed_pieces > m or removed_pieces > n:
        print("Oops! Jogada inválida! Tente de novo.\n")
        removed_pieces = input_to_digit(s)
    removed_pieces = int(removed_pieces)
    if removed_pieces > 1:
        print(f"Você tirou {removed_pieces} peças.")
    else:
        print(f"Você tirou {removed_pieces} peça.")
    return removed_pieces


def remaining_pieces(n):
    if n >= 2:
        return print(f"Agora restam {n} peças no tabuleiro.\n")
    elif n == 1:
        return print("Agora resta apenas uma peça no tabuleiro.\n")

# ========================================================================

def partida():
    m = 0
    n = 0
    while m >= n or n < 2:
        n = "Quantas peças? "
        m = "Limite de peças por jogada? "
        n = input_to_digit(n)
        m = input_to_digit(m)
        if m >= n and n < 2:
            print("O limite de peças por jogada não pode ser maior ou igual à quantidade de peças do tabuleiro, e o número de peças não pode ser menor do que 2.")
        elif m >= n:
            print(
                "O limite de peças por jogada não pode ser maior ou igual à quantidade de peças do tabuleiro.")
        elif n < 2:
            print("O número de peças no tabuleiro não pode ser menor do que 2.")

    if n % (m + 1) == 0:
        print("\nVocê começa!\n")
        start = "user"
    else:
        print("\nComputador começa!\n")
        start = "computer"

#! A parte abaixo poderia ficar mais limpa, mas, dado que um dos requisitos do exercício é que user_pieces() retorne o número de peças que o jogador retirou, não dá pra colocar a outra parte dentro da função.

    while n > 0:
        if start == "user":
            user_pieces = usuario_escolhe_jogada(n, m)
            n -= user_pieces
            remaining_pieces(n)
            if n == 0:
                print("\nFim do jogo! Você ganhou!\n")
                return "user wins"

            computer_pieces = computador_escolhe_jogada(n, m)
            n -= computer_pieces
            remaining_pieces(n)
            if n == 0:
                print("\nFim do jogo! O computador ganhou!\n")
                return "computer wins"

        elif start == "computer":
            computer_pieces = computador_escolhe_jogada(n, m)
            n -= computer_pieces
            remaining_pieces(n)
            if n == 0:
                print("\nFim do jogo! O computador ganhou!\n")
                return "computer wins"

            user_pieces = usuario_escolhe_jogada(n, m)
            n -= user_pieces
            remaining_pieces(n)
            if n == 0:
                print("\nFim do jogo! Você ganhou!\n")
                return "user wins"


# ========================================================================


def main():
    print("Bem-vindo ao jogo do NIM! Escolha:")
    print("1 - para jogar uma partida isolada")
    print("2 - para jogar um campeonato")
    option = get_digit()

    while option != 1 and option != 2:
        print("Você deve selecionar a opção 1 ou 2.\nSelecionar: ")
        option = get_digit()

    if option == 1:
        print("\nVocê escolheu jogar uma partida isolada!\n")
        partida()
    else:
        print("\nVocê escolheu jogar um campeonato!\n")
        user_score = 0
        computer_score = 0
        rodada = 1
        while rodada <= 3:
            print(f"**** Rodada {rodada} ****")
            score = partida()

            if score == "user wins":
                user_score += 1
            elif score == "computer wins":
                computer_score += 1

            rodada += 1
        print("**** Final do campeonato! ****\n")
        print(f"Placar: Você {user_score} X {computer_score} Computador")

    return 0


main()
