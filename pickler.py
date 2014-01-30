__author__ = 'Andreas'
import pickle

def list_pickler(my_list):
    file_loc = 'pickle_test.p'
    tester = open(file_loc,'r+')
    pickle.dump(my_list,tester)
    tester.close()
    return file_loc

def unpickler(file_loc):
    tester = open(file_loc,'r+')
    another_list = pickle.load(tester)
    tester.close()
    return another_list