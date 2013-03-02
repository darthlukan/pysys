# Adapt the code to your code kata test.

import os
import sys
import unittest

from basic.basic import numbers, strings

class TestBasic(unittest.TestCase):
	
	def test_numbers(self):
		self.assertEqual(numbers(1), 1)
		
	def test_strings(self):
		self.assertEqual(strings('foo'), 'foo')

if __name__ == '__main__':
    unittest.main()