__author__ = 'Andreas'
import unittest, os, sys, pickle
from pickler import list_pickler, unpickler

class PicklerTests(unittest.TestCase):
    def setUp(self):
        global tester = os.open("pickle_test.p", os.O_RDWR|os.O_CREAT)
    def pickled_list_no_change(self):
        my_list = ["cheese","ham"]
        pickle.dump(my_list,tester)
        another_list = pickle.load(tester)
        self.assertEqual(my_list,another_list)

    def tearDown(self):
        tester.close()
        os.remove("pickle_test.p")
