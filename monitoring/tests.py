import unittest
import pymon


class TestPymonConfig(unittest.TestCase):

    #def setUp(self):
    #    self.pc = pymon.Config()

    def test_get_config_file(self):
        self.pc = pymon.Config()
        #self.assertIsInstance(self.pc.config, object)
        self.assertTrue(self.pc.config)

    def test_get_config_sections(self):
        self.pc = pymon.Config()
        self.assertIsInstance(self.pc.get_config_sections(), list)

    def test_get_config_options(self):
        self.pc = pymon.Config()
        self.assertIsInstance(self.pc.get_config_options(), list)


class TestPymonMain(unittest.TestCase):

    def setUp(self):
        self.pm = pymon

    def test_main(self):
        self.assertTrue(self.pm.main())


if __name__ == '__main__':
    unittest.main()
