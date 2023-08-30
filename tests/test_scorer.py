import unittest
from scorer import Scorer
from player import Player
from board import Board  # Si es necesario

class TestScorer(unittest.TestCase):
    def test_update_scores(self):
        players_count = 2
        players = [Player() for _ in range(players_count)]
        scorer = Scorer(players)
        
        scorer.update_scores(players[0], 10)
        self.assertEqual(scorer.scores[players[0]], 10)

    

if __name__ == '__main__':
    unittest.main()
