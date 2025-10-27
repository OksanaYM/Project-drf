from unittest import TestCase
from unittest.mock import MagicMock, patch

from ..service import calc, math


class CalcTestCase(TestCase):
    @patch.object(math, 'cos')
    def test_plus(self, mock_cos: MagicMock):
        mock_cos.return_value=55
        res = calc(1, 2, '+')
        self.assertEqual(res, 57)
    # @patch('apps.pizza.service.cos')
    # def test_plus(self, mock_cos: MagicMock):
    #     mock_cos.return_value=55
    #     res = calc(1, 2, '+')
    #     self.assertEqual(res, 57)

    # def test_plus(self):
    #     res = calc(1, 2, '+')
    #     self.assertEqual(res, 3)

    def test_minus(self):
        res = calc(1, 2, '-')
        self.assertEqual(res, -1)

    def test_multiply(self):
        res = calc(1, 2, '*')
        self.assertEqual(res, 2)