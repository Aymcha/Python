from exercice1 import trouver_index_somme
from exercice2 import fibonacci
from exercice3 import combinne_dic
from exercice4 import calculer_pgcd
from exercice5 import multiplication_matrice
from exercice6 import premier
import numpy as np
from random import randint
import unittest
import os
import sys

class TestExercice1(unittest.TestCase):
    liste= [[3, 2, 4],[0, 5, 6]]
    targer = [6, 5, 10]
    result = [[1, 2], [0, 2], [0, 1], [0, 1]]
    def test_trouver_index_somme(self):
        for i in range(2):
            for j in range(2):
                indx_1, indx_2 = trouver_index_somme(self.liste[j],self.targer[i])
                self.assertTrue((indx_1 == self.result[2*i+j][0]) and (indx_2 == self.result[2*i+j][1]))
        self.assertIsNone(trouver_index_somme(self.liste[1],self.targer[2]))

class TestExercice2(unittest.TestCase):
    liste = [1, 2, 3, 5, 8, 13, 21, 34]
    def test_fibonnacci(self):
        for i in range (2,10):
            self.assertTrue(fibonacci(i) == self.liste[i - 2])

class TestExercice3(unittest.TestCase):
    dict_1 = {'a': 100, 'b': 200, 'c':300}
    dict_2 = {'a': 300, 'b': 200, 'd':400}
    dict_3 = {'a': 400, 'b': 400, 'd': 400, 'c': 300}
    def test_combinne_dic(self):
        self.assertDictEqual(combinne_dic(self.dict_1,self.dict_2), self.dict_3)
            
class TestExercice4(unittest.TestCase):
    liste = [[12, 20, 5, 30, 100],[6, 12, 90, 120, 40]]
    target = [6, 4, 5, 30, 20]
    def test_calculer_pgcd(self):
        for i in range(5):
            self.assertTrue(calculer_pgcd(self.liste[0][i],self.liste[1][i]) == self.target[i])

class TestExercice5(unittest.TestCase):
    A = [[2, 3, 6], [5, -1, 12]]
    B = [[1, 0, 4, 7], [2, -3, 6, 2], [5, 8, 9, 6]]
    C = [[38, 39, 80, 56], [63, 99, 122, 105]]
    def test_multiplication_matrice(self):
        self.assertTrue(multiplication_matrice(self.A,self.B) == self.C)
        self.assertIsNone(multiplication_matrice(self.C,self.A))
        self.assertIsNone(multiplication_matrice(self.B,self.C))

class TestExercice6(unittest.TestCase):
    M = [[1, 0, 4, 7], [2, 3, 6, 21], [5, 8, 9, 12]]
    T = [7, 2, 3, 5,]
    def test_premier(self):
        self.assertTrue(premier(self.M) == self.T)
        
    
if __name__ == '__main__':
    if not os.path.exists('logs'):
        os.mkdir('logs')
    with open('logs/tests_results.txt', 'w') as f:
        loader = unittest.TestLoader()
        suite = loader.loadTestsFromModule(sys.modules[__name__])
        unittest.TextTestRunner(f, verbosity=2).run(suite)
