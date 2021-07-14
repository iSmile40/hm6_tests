import unittest
from main import people_document, list_database, add_command, delete_command, move_command, add_shelf
from data import documents


class TestSomething(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("setUpClass")

    def setUp(self):
        print("setUp")

    def test_people_document(self):
        self.assertEqual(people_document("11-2"), "Геннадий Покемонов")

    def test_list_database(self):
        self.assertNotEqual(list_database(), documents)

    def test_add_command(self):
        self.assertEqual(add_command("Пасспорт", "123", "Дмитрий", "4"), "Документ успешно создан и добавлен на полку")

    def test_delete_doc_1(self):
        self.assertEqual(delete_command("2207 876234"), "Документ успешно удален")

    def test_delete_doc_2(self):
        self.assertEqual(delete_command("11-3"), "Такого номера не существует")

    def test_move_command_1(self):
        self.assertEqual(move_command("11-2", "3"), "Документ успешно перемещен")

    def test_move_command_2(self):
        self.assertEqual(move_command("11-3", "3"), "Такого документа не существует")

    def test_add_shelf(self):
        self.assertEqual(add_shelf("3"), "Такая полка уже существует")

    def tearDown(self):
        print("tearDown")

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass")


if __name__ == "__main__":
    unittest.main()
