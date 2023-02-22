import unittest
from circle import circle_length as cl
from math import pi

class TestCircleLength(unittest.TestCase):

  def test_number(self):
    self.assertEqual(cl(0), 0)
    self.assertEqual(cl(1), 2*pi*1)
    self.assertEqual(cl(5), 2*pi*5)
    self.assertEqual(cl(1.2), 2*pi*1.2)

  def test_values(self):
    self.assertRaises(ValueError, cl, -6.8)
    self.assertRaises(ValueError, cl, -1)

  def test_types(self):
    self.assertRaises(TypeError, cl, 5+2j)
    self.assertRaises(TypeError, cl, 'text')
    self.assertRaises(TypeError, cl, [12, 3])
    self.assertRaises(TypeError, cl, [12])
    self.assertRaises(TypeError, cl, [4.23])
    self.assertRaises(TypeError, cl, True)
    self.assertRaises(TypeError, cl, False)

  if __name__ == '__main__':
    unittest.main()