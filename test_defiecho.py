# test_defiecho.py
"""
Tests for DefiEcho module.
"""

import unittest
from defiecho import DefiEcho

class TestDefiEcho(unittest.TestCase):
    """Test cases for DefiEcho class."""

    def test_initialization(self):
        """Test class initialization."""
        instance = DefiEcho()
        self.assertIsInstance(instance, DefiEcho)

    def test_run_method(self):
        """Test the run method."""
        instance = DefiEcho()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
