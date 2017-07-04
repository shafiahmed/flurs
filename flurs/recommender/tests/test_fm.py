from unittest import TestCase
import numpy as np

from flurs.data.entity import User, Item, Event
from flurs.recommender.fm import FMRecommender


class FMRecommenderTestCase(TestCase):

    def setUp(self):
        self.k = 40
        self.recommender = FMRecommender(p=3, k=self.k)
        self.recommender.init_recommender()

    def test_add_user(self):
        self.recommender.add_user(User(0))
        self.assertEqual(self.recommender.n_user, 1)

    def test_add_item(self):
        self.recommender.add_item(Item(0))
        self.assertEqual(self.recommender.n_item, 1)

    def test_update(self):
        self.recommender.add_user(User(0))
        self.recommender.add_item(Item(0))
        self.recommender.update(Event(User(0), Item(0), 1))
        self.assertEqual(self.recommender.n_user, 1)
        self.assertEqual(self.recommender.n_item, 1)

    def test_score(self):
        self.recommender.add_user(User(0))
        self.recommender.add_item(Item(0))
        self.recommender.update(Event(User(0), Item(0), 1))
        score = self.recommender.score(User(0), np.array([0]), np.array([0]))
        self.assertTrue(score >= 0.)
