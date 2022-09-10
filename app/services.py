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

    def get_sales_cost(self):
        return self._sales_cost

    def rent_value(self):
        return self._rent_value

    def __str__(self):
        s = ""
        s += "Sales_cost:" + str(self._sales_cost) + "\n"
        s += "Rent_value:" + str(self._rent_value) + "\n"
        s += "Owner:" + self.owner + "\n"
        return s


class Player(object):
    def __init__(self, player_name, personality):
        """
        :param player_name: string, name_plyer
        :param personality: string, type of player
        """
        self._player_name = player_name
        self._personality = personality
        self._balance = 300.0
        self._position = 0

    def get_player_name(self):
        """
        :return: string, player_name
        """
        return self._player_name

    def get_personality(self):
        """
        :return: string, personality player type
        """
        return self._personality

    def get_balance(self):
        """
        :return: float, total balance
        """
        return self._balance

    def update_balance(self, money, tag):
        """
        :money: float, balance to update with new value
        :tag: int, 1 to plus, 0 to minus
        """
        if tag == 1:
            self._balance += money
        else:
            self._balance -= money

    def get_posision(self):
        """
        :return: int, board position
        """
        return self._position

    def update_posision(self, position):
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
        return s
