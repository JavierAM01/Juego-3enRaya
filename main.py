from enviroment import Enviroment
from player import Player_3moves, Player_FullBaoard


def main():
    
    print("Elige una opción:")
    print(" 1) Modo clásico")
    print(" 2) Modo de Tres Fichas")
    x = input(" > ")

    env = Enviroment()

    if x == "1":
        player1 = Player_FullBaoard(env)
        player2 = Player_FullBaoard(env)
    else:
        player1 = Player_3moves(env)
        player2 = Player_3moves(env)
    
    env.play(player1, player2)


if __name__ == '__main__':
    main()
