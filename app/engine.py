from services import Property, Player, game_round, remove_player
import random

test_board = []
test_players_list = []
test_players_finish = []
test_time_out_players_list = []
test_champion = None


def run():
    global test_board
    global test_champion
    global test_players_list
    global test_players_finish
    global test_time_out_players_list
    board = []
    round_control = 1
    champion_list = []
    rounds = None

    # inicializando o tabuleiro
    for i in range(20):
        sales_cost = random.randrange(300, 10000)
        rent_value = round(sales_cost * (10 / 100))
        board.append(Property(sales_cost, rent_value))

    board.append('start')
    test_board = board.copy()

    # inicializando os jogadores
    player_1 = Player('player_1', 'impulsivo')
    player_2 = Player('player_2', 'exigente')
    player_3 = Player('player_3', 'cauteloso')
    player_4 = Player('player_4', 'aleatorio')

    # define a ordem dos jogadores
    players_list = [player_1, player_2, player_3, player_4]
    test_players_list = players_list.copy()
    random.shuffle(players_list)

    # começando o jogo
    while 0 < round_control <= 1000:
        control = 0
        for player in players_list:
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

            # pega a propriedade que está na casa do tabuleiro aonde está o jogador:
            property_game = board[new_position]

            # verifica se a propriedade já pertence ao jogador
            if property_game.owner == player.player_name():
                player.position = new_position
                player, control, round_control = game_round(player, control, round_control)
                continue

            # se a propriedade já está comprada, paga o aluguel ao proprietário
            elif property_game.owner != "":
                player_owner = property_game.owner
                rent_value = property_game.rent_value()

                # retira o valor do jogador atual
                player.balance = rent_value, 0

                # se o saldo do jogador atual ficar negativo, é retirado do jogo, com o proprietario
                # recebendo o saldo restante do jogador atual:
                if player.balance <= 0:
                    player.balance = rent_value, 1
                    champion_list.append(player)
                    remove_player(player, player_owner, players_list, board)
                    continue

            if personality == 'impulsivo':  # --> sempre compra a propriedade
                if property_game.sales_cost() <= player.balance:
                    player.balance = property_game.sales_cost(), 0
                    property_game.owner = player.player_name()

            elif personality == 'exigente':  # --> compra se o valor do aluguel > 50
                if property_game.rent_value() > 50:
                    if property_game.sales_cost() <= player.balance:
                        player.balance = property_game.sales_cost(), 0
                        property_game.owner = player.player_name()

            elif personality == 'cauteloso':  # --> compra se saldo > 80 depois da compra.
                if player.balance - property_game.sales_cost() > 80:
                    player.balance = property_game.sales_cost(), 0
                    property_game.owner = player.player_name()

            elif personality == 'aleatorio':  # --> compra com probabilidade de 50%.
                if random.choice([0, 1]) == 1:
                    if property_game.sales_cost() <= player.balance:
                        player.balance = property_game.sales_cost(), 0
                        property_game.owner = player.player_name()

            player.position = new_position

            # verifica o jogador que completou a rodada e incrementa o contador de rodadas
            player, control, round_control = game_round(player, control, round_control)

            # se resta somente 1 jogador, encerra a partida
            if len(players_list) == 1:
                rounds = round_control
                round_control = 0
                champion_list.append(player)
                test_players_finish = players_list.copy()

    if round_control != 0:
        # se a partida acaba por time_out, retorna o player com maior saldo e por ordem de jogada
        temp = max([player.balance for player in players_list])
        champion_list = [player for player in players_list if player.balance == temp]
        test_time_out_players_list = players_list.copy()
        test_champion = champion_list[0]
        return {'rounds': round_control, 'champion': champion_list[0], 'time_out': True}
    else:
        return {'rounds': rounds, 'champion': champion_list[-1], 'time_out': False}
