import unittest
from tools import mysql

class TestStringMethods(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        hostname = '127.0.0.1'
        username = 'root'
        password = 'admin'
        database = 'groundhopping_db'
        port = 3307
        self.db = mysql.create_connection(hostname, username, password, database, port)

    @classmethod
    def tearDownClass(self):
        self.db.close()

    def setUp(self):
        self.cursor = self.db.cursor()

    def tearDown(self):
        query = "DELETE FROM `User`"
        self.cursor.execute(query)
        self.db.commit()
        self.cursor.close()
        print("toto")

    def test_select(self):
        query = "SELECT * FROM User"
        res = self.cursor.execute(query)
        self.assertEqual(res, 0)

    def test_insert(self):
        query = "INSERT INTO `User`(`Username`, `Password`) VALUES(%s, %s)"
        args = ('toto', 'tata')
        res = self.cursor.execute(query, args)
        self.db.commit()
        self.assertEqual(res, 1)