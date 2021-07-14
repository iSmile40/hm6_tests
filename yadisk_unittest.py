import unittest
from yadisk import create_folder, check_folder_exist


class TestYadisk(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("setUpClass")

    def setUp(self):
        print("setUp")

    def test_create_folder_success(self):
        self.assertEqual(create_folder("Hello").status_code, 201)

    def test_create_folder_failed(self):
        self.assertEqual(create_folder("").status_code, 409)

    def test_check_folder_exist_success(self):
        self.assertEqual(check_folder_exist("Hello").status_code, 200)

    def test_check_folder_exist_failed(self):
        self.assertEqual(check_folder_exist("Hello").status_code, 404)

    def tearDown(self):
        print("tearDown")

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass")

if __name__ == "__main__":
    unittest.main()
