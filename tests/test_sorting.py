import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here

    def test_nonexistent_folder(self):
        self.assertEqual(True, False)#Hold on

    def test_existing_folder(self):
        self.assertEqual(True, False)#Hold on

if __name__ == '__main__':
    unittest.main()