import unittest
from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_search_existed(self):
        player = self.stats.search("Kurri")

        self.assertEqual(player.name, "Kurri")
        self.assertEqual(player.team, "EDM")

    def test_search_uknown(self):
        self.assertIsNone(self.stats.search("Selanne"))

    def test_team(self):
        players = self.stats.team("EDM")
        names = [player.name for player in players]

        self.assertEqual(names, ["Semenko", "Kurri", "Gretzky"])

    def test_team_uknown(self):
        self.assertEqual(self.stats.team("UKN"), [])

    def test_top(self):
        self.assertEqual(len(self.stats.top(3)), 3)

    def test_top_by_points(self):
        players = self.stats.top(3)
        names = [player.name for player in players]

        self.assertEqual(names, ["Gretzky", "Lemieux", "Yzerman"])