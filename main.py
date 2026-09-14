from velha import jogar


def main():
    while True:
        jogar()
        resposta = input("\nJogar de novo? (s/n): ").strip().lower()
        if resposta != "s":
            print("Ate a proxima!")
            break


if __name__ == "__main__":
    main()
