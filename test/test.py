import unittest
from src.main.classes import abilities
from src.main.classes import player

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)

class AbilitiesTests(unittest.TestCase):
    def test_heal(self):
        pl = player.Player(3,4,"", 5)
        ab = abilities.Ability("Heal", "stats_based")
        ab.heal_amount = 20
        ab.hp_change(pl, pl.hp+ab.heal_amount)
        self.assertEqual(pl.hp, 120)

if __name__ == '__main__':
    unittest.main()