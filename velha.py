def tabuleiro_vazio():
    return [" "] * 9


def desenhar(tabuleiro):
    linhas = [tabuleiro[i:i + 3] for i in range(0, 9, 3)]
    print()
    for i, linha in enumerate(linhas):
        print(" " + " | ".join(linha))
        if i < 2:
            print("---+---+---")
    print()


LINHAS_VITORIA = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),
    (0, 3, 6), (1, 4, 7), (2, 5, 8),
    (0, 4, 8), (2, 4, 6),
]


def verificar_vencedor(tabuleiro):
    for a, b, c in LINHAS_VITORIA:
        if tabuleiro[a] != " " and tabuleiro[a] == tabuleiro[b] == tabuleiro[c]:
            return tabuleiro[a]
    return None


def tabuleiro_cheio(tabuleiro):
    return " " not in tabuleiro


def jogar():
    tabuleiro = tabuleiro_vazio()
    jogador = "X"

    print("=== JOGO DA VELHA ===")
    print("Posicoes de 1 a 9, da esquerda pra direita, de cima pra baixo.")

    while True:
        desenhar(tabuleiro)
        print(f"Vez do jogador {jogador}")

        posicao = input("Escolha uma posicao (1-9): ").strip()

        if not posicao.isdigit() or not (1 <= int(posicao) <= 9):
            print("Digite um numero de 1 a 9.")
            continue

        indice = int(posicao) - 1

        if tabuleiro[indice] != " ":
            print("Essa posicao ja foi jogada.")
            continue

        tabuleiro[indice] = jogador

        vencedor = verificar_vencedor(tabuleiro)
        if vencedor:
            desenhar(tabuleiro)
            print(f"Jogador {vencedor} venceu!")
            return vencedor

        if tabuleiro_cheio(tabuleiro):
            desenhar(tabuleiro)
            print("Empate!")
            return None

        jogador = "O" if jogador == "X" else "X"


if __name__ == "__main__":
    testes = [
        (["X", "X", "X", " ", " ", " ", " ", " ", " "], "X"),
        (["O", " ", " ", "O", " ", " ", "O", " ", " "], "O"),
        (["X", "O", "X", "O", "X", "O", "O", "X", "O"], None),
    ]
    for tab, esperado in testes:
        assert verificar_vencedor(tab) == esperado, f"falhou para {tab}"
    print("Testes de verificar_vencedor passaram.")
