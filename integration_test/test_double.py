import unittest
from double import double


class TestDouble(unittest.TestCase):
    """
    Test double function
    """

    def test_should_return_double(self):
        # Arrange
        num = 2
        # Act
        res = double(num)
        # Assert
        self.assertEqual(res, 4)

    def test_0_should_return_0(self):
            # Arrange
        num = 0
        # Act
        res = double(num)
        # Assert
        self.assertEqual(res, 0)
