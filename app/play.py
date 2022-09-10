from services import Property, Player
import random

if __name__ == "__main__":
    board = []
    round_game = 1
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
    for i in range(50):
        for j in range(len(board)):
            for k, player in enumerate(player_order):
                # verifica o tipo do jogador e joga o dado
                personality = player.get_personality()
                dice = random.randrange(1, 7)
                old_position = player.get_posision()
                new_position = old_position + dice
                if new_position > (len(board) - 1):
                    new_position = new_position - (len(board) - 1)
                    player.update_balance(100, 1)

                elif new_position == (len(board) - 1):
                    player.update_balance(100, 1)
                    player.update_posision(0)
                    print(f"dice: {dice}")
                    print(player)
                    print()
                    continue

                # sempre compra a propriedade
                if personality == 'impulsivo':
                    # verifica se a casa já pertence ao jogador
                    if board[new_position].owner == player.get_player_name():
                        player.update_posision(new_position)

                    # se a casa já está alugada, paga o aluguel ao proprietário
                    elif board[new_position].owner != "":
                        rent_value = board[new_position].rent_value()
                        player.update_balance(board[new_position].get_sales_cost(), 0)
                        player_order[k].update_balance(rent_value, 1)
                        player.update_posision(new_position)

                    # se a casa não está alugada, compra
                    elif board[new_position].get_sales_cost() <= player.get_balance():
                        player.update_balance(board[new_position].get_sales_cost(), 0)
                        board[new_position].owner = player.get_player_name()
                        player.update_posision(new_position)

                    else:
                        player.update_posision(new_position)

                    print(f"dice: {dice}")
                    print(player)
                    print()

                elif personality == 'exigente':
                    pass
                elif personality == 'cauteloso':
                    pass
                elif personality == 'aleatorio':
                    pass

    print("Fim do programa")
