from exercice1 import calculer_portee
from exercice2 import resoudre_equation
from exercice3 import calculer_unites_dizaines_centaine
from exercice4 import trouver_jour_semaine
from exercice5 import points_perdu
import numpy as np
from random import randint
import unittest
import os
import sys
import math


class TestExercice1(unittest.TestCase):
    CONST_SIZE = 10

    def test_calculer_portee(self):
        array = np.random.randint(0, (360, 1000), size=(self.CONST_SIZE, 2))
        for angle, vitesse in array:
            self.assertAlmostEqual(calculer_portee(angle, vitesse),
                                   ((vitesse / 3.6) ** 2 * math.sin(2 * math.pi * angle / 180)) / 9.8)


class TestExercice2(unittest.TestCase):
    def test_no_solution(self):
        self.assertEqual(resoudre_equation(1, 1, 1), None)

    def test_one_solution(self):
        a, b, c = 1, -2, 1
        expectedSolution = 1
        self.assertEqual(resoudre_equation(a, b, c), expectedSolution)

    def test_two_solutions(self):
        a, b, c = 1, -4, 3
        x1, x2 = 1, 3
        b1 = resoudre_equation(a, b, c)[0] == x1 and resoudre_equation(a, b, c)[1] == x2
        b2 = resoudre_equation(a, b, c)[0] == x2 and resoudre_equation(a, b, c)[1] == x1
        self.assertTrue(b1 or b2)


class TestExercise3(unittest.TestCase):
    CONST_SIZE = 10

    def test_chiffres(self):
        array = np.random.randint(0, 999, size=(self.CONST_SIZE, 1))
        for nombre in array:
            b1 = calculer_unites_dizaines_centaine(nombre)[0] == nombre % 10
            b2 = calculer_unites_dizaines_centaine(nombre)[1] == (nombre // 10) % 10
            b3 = calculer_unites_dizaines_centaine(nombre)[2] == (nombre // 100) % 10
            self.assertTrue(b1 and b2 and b3)


class TestExercise4(unittest.TestCase):
    def test_30_jour(self):
        annee, mois, jour = 2011, 6, 30
        self.assertEqual(trouver_jour_semaine(annee, mois, jour), "Jeudi")

    def test_31_jour(self):
        annee, mois, jour = 2020, 7, 31
        self.assertEqual(trouver_jour_semaine(annee, mois, jour), "Vendredi")

    def test_jour_fevrier(self):
        annee, mois, jour = 2008, 2, 29
        self.assertEqual(trouver_jour_semaine(annee, mois, jour), "Vendredi")

    def test_dimanche(self):
        annee, mois, jour = 2021, 1, 24
        self.assertEqual(trouver_jour_semaine(annee, mois, jour), "Dimanche")

    def test_annee_bissextile(self):
        annee, mois, jour = 2020, 6, 1
        self.assertEqual(trouver_jour_semaine(annee, mois, jour), "Lundi")


class TestExercice5(unittest.TestCase):
    CONST_SIZE = 10

    def test_calculer_points(self):
        array = np.random.randint(0, 5, size=(self.CONST_SIZE, 4))
        for dindon, lievre, cerf, ours_noir in array:
            self.assertAlmostEqual(points_perdu(dindon, lievre, cerf, ours_noir),
                                   (100 - (dindon + 3 * lievre + 5 * cerf + 10 * ours_noir)))


if __name__ == '__main__':
    if not os.path.exists('logs'):
        os.mkdir('logs')
    with open('logs/tests_results.txt', 'w') as f:
        loader = unittest.TestLoader()
        suite = loader.loadTestsFromModule(sys.modules[__name__])
        unittest.TextTestRunner(f, verbosity=2).run(suite)
