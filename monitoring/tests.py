import unittest
import pymon


class TestPymonConfig(unittest.TestCase):

    def setUp(self):
        self.pc = pymon.Config()

    def test_get_config_file(self):
        self.assertTrue(self.pc.get_config_file())

    def test_get_config_sections(self):
        self.assertIsInstance(self.pc.get_config_sections(), list)
        sections = self.pc.get_config_sections()
        section = sections[0]
        self.assertEqual(section, 'Test Section')

    def test_get_config_options(self):
        self.assertIsInstance(self.pc.get_config_options(), list)
        options = self.pc.get_config_options()
        self.assertEqual(options[0], 'testoption')


class TestPymonMain(unittest.TestCase):

    def setUp(self):
        self.pm = pymon

    def test_main(self):
        self.assertTrue(self.pm.main())


if __name__ == '__main__':
    unittest.main()
