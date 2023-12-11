#!/usr/bin/python3
"""_summary_"""


import sys
import os

sys.path.append(os.getcwd())

from unittest import TestCase
from models.base import Base


class Test_Base(TestCase):
    """_summary_

    Args:
        TestCase (_type_): _description_
    """

    def test_base(self):
        """_summary_"""
        b1 = Base()
        self.assertEqual(b1.id, 1)

        b2 = Base()
        self.assertEqual(b2.id, 2)

        b3 = Base()
        self.assertEqual(b3.id, 3)

        b4 = Base(12)
        self.assertEqual(b4.id, 12)

        b5 = Base()
        self.assertEqual(b5.id, 4)
