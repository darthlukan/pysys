# Adapt the code to your code kata tutorial.

import unittest

class Tutorial(unittest.TestCase):
	
	def test_foo(self):
		object_under_test = self
		self.assertEqual('foo', self.foo())
	
	def foo(self):
	    return "foo"
	
	def test_maths(self):
		object_under_test = self
		self.assertEqual(4, object_under_test.maths())
	
	def maths(self):
	    return 2+2

#class TestTutorial(unittest.TestCase):

    #def test_foo(self):
    #    object_under_test = Tutorial()
    #    self.assertEqual("foo", object_under_test.foo())

	#def test_maths(self):
	#	object_under_test = Tutorial()
	#	self.assertEqual(4, object_under_test.maths())

if __name__ == '__main__':
    unittest.main()