import unittest
from game.scorer import Scorer
from game.player import Player

class TestScorer(unittest.TestCase):
    def setUp(self):
        self.players = [Player(), Player()]
        self.scorer = Scorer(self.players)

    def test_update_scores(self):
        player = self.players[0]
        initial_score = self.scorer.scores[player]
        self.scorer.update_scores(player, 10)
        updated_score = self.scorer.scores[player]
        self.assertEqual(updated_score, initial_score + 10)

if __name__ == '__main__':
    unittest.main()
