__author__ = 'Andreas'
import unittest, os, sys, pickle
from pickler import list_pickler, unpickler

class PicklerTests(unittest.TestCase):
    def setUp(self):
        os.open("pickle_test.p", os.O_RDWR|os.O_CREAT)
    def pickled_list_no_change_test(self):

        #old code - ignore me
        #tester = open('pickle_test.p','r+')
        #my_list = ["cheese","ham"]
        #pickle.dump(my_list,tester)
        #another_list = pickle.load(tester)
        #tester.close()
        my_list = ["cheese","ham"]
        file_loc = list_pickler(my_list)
        another_list = unpickler(file_loc)

        self.assertEqual(my_list,another_list)

    def tearDown(self):
        os.remove("pickle_test.p")
