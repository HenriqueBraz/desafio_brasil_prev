import unittest
from app import engine, play


class TestEngine(unittest.TestCase):
    def test_board(self):
        """
        Test if board was initialized with 21 positions
        """
        engine.run()
        result = len(engine.test_board)
        self.assertEqual(result, 21)

    def test_players(self):
        """
        Test if players was initialized with 4 positions
        """
        engine.run()
        result = len(engine.test_players_list)
        self.assertEqual(result, 4)

    def test_game_finish(self):
        """
        Test game finish if players_list == 1
        """
        engine.run()
        result = len(engine.test_players_finish)
        self.assertEqual(result, 1)

    def test_time_out(self):
        """
        Test if time out ends, engine get correct player parameters
        """
        test_time_out_players_list = []
        while not test_time_out_players_list:
            engine.run()
            test_time_out_players_list = engine.test_time_out_players_list

        temp = max([player.balance for player in test_time_out_players_list])
        champion_list = [player for player in test_time_out_players_list if player.balance == temp]
        champion = champion_list[0]
        test_champion = engine.test_champion
        self.assertEqual(champion, test_champion)


class TestPlay(unittest.TestCase):
    def test_play(self):
        """
        Test it finish in 300 games
        """
        play.play(True)
        test_game = play.test_game
        self.assertEqual(test_game, 300)


if __name__ == '__main__':
    unittest.main()
