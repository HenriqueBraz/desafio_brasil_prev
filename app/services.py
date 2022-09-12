def game_round(player, control, round_control):
    """
    if player finsh game round, increment count_round and update player.game_round
    :param player: object, current player
    :param control: int, aux control variable
    :param round_control: int, round control variable
    :return: player, control, round_control
    """
    if player.game_round and control == 0:
        player.game_round = False
        round_control += 1
        control = 1

    elif player.game_round:
        player.game_round = False

    return player, control, round_control


def remove_player(player, rent_value, player_owner, player_order, board):
    # paga o saldo restante para o proprietario:
    for player2 in player_order:
        if player2.player_name() == player_owner:
            player2.balance = player.balance, 1
            break
    # perde todas as propriedades:
    for p in board:
        if p != 'start':
            if p.owner == player.player_name():
                p.owner = ""
    # é retirado do jogo:
    player_order.remove(player)


class Property(object):
    def __init__(self, sales_cost, rent_value, owner=""):
        """
        :param sales_cost: int, 0 to 100
        :param rent_value: int, 0 to 100
        :param owner: string, player name
        """
        self._sales_cost = sales_cost
        self._rent_value = rent_value
        self.owner = owner

    def sales_cost(self):
        return self._sales_cost

    def rent_value(self):
        return self._rent_value

    def __str__(self):
        s = ""
        s += "Sales_cost:" + str(self._sales_cost) + "\n"
        s += "Rent_value:" + str(self._rent_value) + "\n"
        s += "Owner:" + self.owner + "\n"
        return s


#########################################################################################################
class Player(object):
    def __init__(self, player_name, personality):
        """
        :param player_name: string, name_player
        :param personality: string, type of player
        """
        self._player_name = player_name
        self._personality = personality
        self._balance = 300.0
        self._position = 0
        self._game_round = False

    def player_name(self):
        """
        :return: string, player_name
        """
        return self._player_name

    def personality(self):
        """
        :return: string, personality player type
        """
        return self._personality

    @property
    def game_round(self):
        """
        :return: boolean, True if player finish one board round
        """
        return self._game_round

    @game_round.setter
    def game_round(self, flag):
        """
        :param flag: boolean
        """
        self._game_round = flag

    @property
    def balance(self):
        """
        :return: float, total balance
        """
        return self._balance

    @balance.setter
    def balance(self, args):
        """
        :param args: args[0] -> float, value to update, args[1] -> int, 1 to plus, 0 to minus
        :return:
        """
        if args[1]:
            self._balance += args[0]
        else:
            self._balance -= args[0]

    @property
    def position(self):
        """
        :return: int, board position
        """
        return self._position

    @position.setter
    def position(self, position):
        """
        :param position: int, new board position to update
        """
        self._position = position

    def __str__(self):
        s = ""
        s += "Player:" + self._player_name + "\n"
        s += "Type:" + self._personality + "\n"
        s += "Balance:" + str(self._balance) + "\n"
        s += "Board Position:" + str(self._position) + "\n"
        s += "Game Round:" + str(self._game_round) + "\n"
        return s
