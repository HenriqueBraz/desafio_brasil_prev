from services import Property, Player
import random

if __name__ == "__main__":
    board = []
    round_control = 1
    sales_cost = random.randrange(50, 101)
    rent_value = round(sales_cost * (10 / 100))

    # inicializando o tabuleiro
    for i in range(20):
        sales_cost = random.randrange(50, 101)
        rent_value = round(sales_cost * (10 / 100))
        board.append(Property(sales_cost, rent_value))

    board.append('start')

    # inicializando os jogadores
    player_1 = Player('player_1', 'impulsivo')
    player_2 = Player('player_2', 'exigente')
    player_3 = Player('player_3', 'cauteloso')
    player_4 = Player('player_4', 'aleatorio')

    # define a ordem dos jogadores
    player_order = [player_1, player_2, player_3, player_4]
    random.shuffle(player_order)

    # começando o jogo
    while round_control <= 1000:
        control = 0
        for k, player in enumerate(player_order):
            # verifica o tipo do jogador e joga o dado
            personality = player.personality()
            dice = random.randrange(1, 7)
            old_position = player.position
            new_position = old_position + dice

            # verifica se o jogador completou a rodada
            if new_position > (len(board) - 1):
                new_position = new_position - (len(board) - 1)
                player.balance = 100, 1
                player.game_round = True

            elif new_position == (len(board) - 1):
                player.balance = 100, 1
                player.position = 0
                player.game_round = True
                print(f"dice: {dice}")
                print(player)
                print()
                continue

            # verifica se a casa já pertence ao jogador
            if board[new_position].owner == player.player_name():
                player.position = new_position

            # se a casa já está alugada, paga o aluguel ao proprietário
            elif board[new_position].owner != "":
                rent_value = board[new_position].rent_value()
                player.balance = board[new_position].get_sales_cost(), 0
                player_order[k].balance = rent_value, 1
                player.position = new_position

            if personality == 'impulsivo':  # --> sempre compra a propriedade
                # se a casa não está alugada, compra se tiver saldo suficiente
                if board[new_position].get_sales_cost() <= player.balance:
                    player.balance = board[new_position].get_sales_cost(), 0
                    board[new_position].owner = player.player_name()
                    player.position = new_position

                else:
                    player.position = new_position

            elif personality == 'exigente':  # --> exigente compra, desde que o valor do aluguel > 50
                player.position = new_position

            elif personality == 'cauteloso':
                player.position = new_position

            elif personality == 'aleatorio':
                player.position = new_position

            print(f"dice: {dice}")
            print(player)
            print()

            # verifica o primeiro jogador que completou a rodada e incrementa o contador de rodadas
            if player.game_round and control == 0:
                player.game_round = False
                round_control += 1
                control = 1

            elif player.game_round:
                player.game_round = False

    print("Fim do programa")
