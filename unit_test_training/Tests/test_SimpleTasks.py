import unittest
import getpass
from MyApp.SimpleTasks import SimpleTasks
tasks = SimpleTasks()

class tes_MyApp(unittest.TestCase):

    def test_returns_my_user_name(self):
        self.assertEqual("Hello, {}!".format(getpass.getuser()), tasks.get_greeting("Hello")) #Note: first arg is the expect value

    def test_add_two_number(self):
        self.assertEqual(5 , tasks.get_sum(2,3))