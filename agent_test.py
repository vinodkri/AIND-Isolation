"""This file is provided as a starting template for writing your own unit
tests to run and debug your minimax and alphabeta agents locally.  The test
cases used by the project assistant are not public.
"""
import random as ran
import unittest
import isolation
import game_agent
import sample_players

from importlib import reload


class CenterHeuristicTestOne(unittest.TestCase):
    def setUp(self):
        #depth = 3
        print("Test Case Details:")
        print("------------------")
        print("Heuristic: improved_score")
        reload(game_agent)
        #self.player1 = game_agent.MinimaxPlayer()
        self.player2 = game_agent.AlphaBetaPlayer()
        self.player1 = sample_players.CenterPlayer()
        self.game = isolation.Board(self.player1, self.player2)
        self.game.apply_move((ran.randint(0, 6), ran.randint(0, 6)))
        #self.game.apply_move((ran.randint(0, 6), ran.randint(0, 6)))
        print("Initial Board State:")
        print(self.game.to_string())

    @unittest.skip("reason for skipping")
    def test_game_play(self):
        winner, history, outcome = self.game.play()
        print("\nWinner: {}\nOutcome: {}".format(winner, outcome))
        if winner == self.player1:
            print("Player 1 Wins")
        else:
            print("Player 2 Wins")
            print("Final Board State")
        print("----------------------------------------")
        print(self.game.to_string())
        print("Move history:\n{!s}".format(history))
        print("Compare Board State")
        unittest.assertEqual(self.game._board_state, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 15, 60],
                             "Reached state same as the udacity testcase")

    @unittest.skip("reason for skipping")
    def test_aplha_beta_game_play(self):
        winner, history, outcome = self.game.play()
        print("\nWinner: {}\nOutcome: {}".format(winner, outcome))
        if winner == self.player1:
            print("Player 1 Wins")
        else:
            print("Player 2 Wins")
        print("Final Board State")
        print("----------------------------------------")
        print(self.game.to_string())
        print("Move history:\n{!s}".format(history))


class ImprovedHeuristicTestOne(unittest.TestCase):
    def setUp(self):
        depth = 3
        print("Test Case Details:")
        print("------------------")
        print("Heuristic: improved_score")
        print("Depth: ", depth)
        reload(game_agent)
        self.player2 = game_agent.MinimaxPlayer()
        self.player1 = sample_players.ImprovedPlayer()
        self.game = isolation.Board(self.player1, self.player2)
        self.player1.depth = depth
        self.player2.depth = depth
        self.game.apply_move((ran.randint(1, 7), ran.randint(1, 7)))
        self.game.apply_move((ran.randint(1, 7), ran.randint(1, 7)))
        print("Initial Board State:")
        print(self.game.to_string())
    @unittest.skip("reason for skipping")
    def test_game_play(self):
        winner, history, outcome = self.game.play()
        print("\nWinner: {}\nOutcome: {}".format(winner, outcome))
        if winner == self.player1:
            print("Player 1 Wins")
        else:
            print("Player 2 Wins")
        print("Final Board State")
        print("----------------------------------------")
        print(self.game.to_string())
        print("Move history:\n{!s}".format(history))
        print("Compare Board State")
        # self.assertEqual(self.game._board_state, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 46, 12],
        #    "Reached state same as the udacity testcase")

class OpenMovesHeuristicTestOne(unittest.TestCase):
    def setUp(self):
        print("Test Case Details:")
        print("------------------")
        print("Heuristic: open_move_score")
        reload(game_agent)
        self.player2 = game_agent.AlphaBetaPlayer()
        self.player1 = sample_players.OpenMovesPlayer()
        self.game = isolation.Board(self.player1, self.player2, 9 , 9)
        #self.game.apply_move((ran.randint(1, 7), ran.randint(1, 7)))
        #self.game.apply_move((ran.randint(1, 7), ran.randint(1, 7)))
        print("Initial Board State:")
        print(self.game.to_string())

    @unittest.skip("reason for skipping")
    def test_board_state_one(self):
        self.game._board_state = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 51, 49]
        winner, history, outcome = self.game.play()
        print("\nWinner: {}\nOutcome: {}".format(winner, outcome))
        if winner == self.player1:
            print("Player 1 Wins")
        else:
            print("Player 2 Wins")
        print("Final Board State")
        print("----------------------------------------")
        print(self.game.to_string())
        print("Move history:\n{!s}".format(history))
        #print("Compare Board State")

    #@unittest.skip("reason for skipping")
    def test_board_state_two(self):
        self.game._board_state = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 39, 32]
        winner, history, outcome = self.game.play()
        print("\nWinner: {}\nOutcome: {}".format(winner, outcome))
        if winner == self.player1:
            print("Player 1 Wins")
        else:
            print("Player 2 Wins")
        print("Final Board State")
        print("----------------------------------------")
        print(self.game.to_string())
        print("Move history:\n{!s}".format(history))

if __name__ == '__main__':
    print("Testing Main")
    unittest.main()
