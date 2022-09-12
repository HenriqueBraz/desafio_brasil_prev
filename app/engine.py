from services import Property, Player, game_round, remove_player
import random


def run():
    board = []
    round_control = 1
    champion_list = []
    rounds = None

    # inicializando o tabuleiro
    for i in range(20):
        sales_cost = random.randrange(100, 1000)
        rent_value = round(sales_cost * (20 / 100))
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
    while 0 < round_control <= 1000:
        control = 0
        for k, player in enumerate(player_order):
            # verifica o tipo do jogador e joga o dado
            personality = player.personality()
            dice = random.randrange(1, 7)
            old_position = player.position
            new_position = old_position + dice

            # verifica se o jogador passou a casa Start
            if new_position > (len(board) - 1):
                new_position = new_position - (len(board) - 1)
                player.balance = 100, 1
                player.game_round = True

            # verifica se o jogador está em cima da casa Start
            elif new_position == (len(board) - 1):
                player.balance = 100, 1
                player.position = 0
                player.game_round = True
                continue

            # verifica se a casa já pertence ao jogador
            if board[new_position].owner == player.player_name():
                player.position = new_position
                player, control, round_control = game_round(player, control, round_control)
                continue

            # se a casa já está alugada, paga o aluguel ao proprietário
            elif board[new_position].owner != "":
                player_owner = board[new_position].owner
                rent_value = board[new_position].rent_value()

                # retira o valor do jogador atual
                player.balance = rent_value, 0

                # se o saldo do jogador atual ficar negativo, é retirado do jogo, com o proprietario
                # recebendo o saldo restante do jogador atual:
                if player.balance <= 0:
                    player.balance = rent_value, 1
                    champion_list.append(player)
                    remove_player(player, rent_value, player_owner, player_order, board)
                    continue

            if personality == 'impulsivo':  # --> sempre compra a propriedade
                if board[new_position].sales_cost() <= player.balance:
                    player.balance = board[new_position].sales_cost(), 0
                    board[new_position].owner = player.player_name()

            elif personality == 'exigente':  # --> compra se o valor do aluguel > 50
                if board[new_position].rent_value() > 50:
                    if board[new_position].sales_cost() <= player.balance:
                        player.balance = board[new_position].sales_cost(), 0
                        board[new_position].owner = player.player_name()

            elif personality == 'cauteloso':  # --> compra se saldo > 80 depois da compra.
                if player.balance - board[new_position].sales_cost() > 80:
                    player.balance = board[new_position].sales_cost(), 0
                    board[new_position].owner = player.player_name()

            elif personality == 'aleatorio':  # --> compra com probabilidade de 50%.
                if random.choice([0, 1]) == 1:
                    if board[new_position].sales_cost() <= player.balance:
                        player.balance = board[new_position].sales_cost(), 0
                        board[new_position].owner = player.player_name()

            player.position = new_position

            # verifica o jogador que completou a rodada e incrementa o contador de rodadas
            player, control, round_control = game_round(player, control, round_control)

            if len(player_order) == 1:
                rounds = round_control
                round_control = 0
                champion_list.append(player)

    if round_control != 0:
        temp = []
        for player in player_order:
            temp.append(player.balance)
        temp = max(temp)
    else:
        dict_return = {'rounds': rounds, 'champion': champion_list[-1]}
        return dict_return
