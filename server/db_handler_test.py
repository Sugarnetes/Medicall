import unittest
from my_db_handler import DatabaseHandler

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.db_object = DatabaseHandler()
    def test_db_transaction(self):
        store = {"first": "Bach", "middle": "none"}
        test_ref = self.db_object.user_collection().document("unit_test_1")
        test_ref.set(store)

        self.assertEqual(test_ref.get().to_dict(), store)

        test_ref.delete()

if __name__ == '__main__':
    unittest.main()