import rock_paper_scissors
import unittest
import random

class TestRockPaperScissors(unittest.TestCase):

    # rock = 1, paper = 2, scissors = 3

    def test_decider(self):
        comp = 2  # computer picked paper
        num = 1  # user picked rock
        expected = print('The computer wins, rock loses to paper')
        self.assertEqual(expected, rock_paper_scissors.decider(num, comp))

        comp = 3
        num = 1
        expected =  print('The computer loses, scissors loses to rock')
        self.assertEqual(expected, rock_paper_scissors.decider(num, comp))

        comp = 3
        num = 2
        expected = print('The computer wins, paper loses to scissors')
        self.assertEqual(expected, rock_paper_scissors.decider(num, comp))

        comp = 1
        num = 2
        expected = print('The computer loses, rock loses to paper')
        self.assertEqual(expected, rock_paper_scissors.decider(num, comp))

        comp = 1
        num = 1
        expected = print("It's a draw ")
        self.assertEqual(expected, rock_paper_scissors.decider(num, comp))
