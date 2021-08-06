import unittest
from database_connection import Database


class TestStringMethods(unittest.TestCase):
    def test_create_user_table(self):
        database = Database("test.db")
        self.assertEqual(database.create_user_table(), "user table created successfully")

    def test_create_product_table(self):
        database = Database("test.db")
        self.assertEqual(database.create_product_table(), "product table created successfully")

    def test_register_user(self):
        database = Database("test.db")
        self.assertEqual(database.register_user("first_name", "last_name", "username", "email_address", "address", "password"), "user successfully registered")

    def test_save_product(self):
        database = Database("test.db")
        self.assertEqual(database.save_product("name", "description", "price", "category", "review"), "product successfully added")


