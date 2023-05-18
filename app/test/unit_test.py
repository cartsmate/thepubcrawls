import unittest
from ..views import pub_test as pt


class TestPub(unittest.TestCase):

    def test_add(self):
        result = pt.pub_test(2, 3)
        self.assertEqual(result, 6)
