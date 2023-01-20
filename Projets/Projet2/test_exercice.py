import unittest
import os
import sys
from unittest.mock import patch
from exercice import nettoyer, chargement, chercher


class TestExercice(unittest.TestCase):

    def test_nettoyer(self):
        ligne = "Film Test_Film 2012"
        type_d, nom_d, annee_d = "Film", "Test Film", "2012"
        type_r, nom_r, annee_r = nettoyer(ligne)
        self.assertEqual(type_d, type_r)
        self.assertEqual(nom_d.lower(), nom_r)
        self.assertEqual(annee_d, annee_r)

    def test_chargement(self):
        film_donnees_d = {"Birdman".lower(): "2014", "Whiplash".lower(): "2014",
                          "Reviens-moi".lower(): "2007", "Les Fils de l'homme".lower(): "2006",
                          "Old Boy".lower(): "2003", "Harry Potter 1".lower(): "1998",
                          "Harry Potter 2".lower(): "1999", "Harry Potter 3".lower(): "1999",
                          "Harry Potter 4".lower(): "2001", "Harry Potter 5".lower(): "2003",
                          "Harry Potter 6".lower(): "2005", "Harry Potter 7".lower(): "2007",
                          "la chasse".lower(): "2012"}

        serie_donnees_d = {"Breaking Bad".lower(): "2008", "Watchmen".lower(): "2019",
                           "Person of Interest".lower(): "2011", "Mr.Robor".lower(): "2015",
                           "Game Of Thrones".lower(): "2011", "Sherlock".lower(): "2010"}

        film_donnees_r, serie_donnees_r = chargement()

        self.assertDictEqual(film_donnees_d, film_donnees_r)
        self.assertDictEqual(serie_donnees_d, serie_donnees_r)

    @patch('builtins.input', side_effect=["film", "har"])
    def test_chercher_1(self, mock_inputs):
        film_donnees, serie_donnees = chargement()
        media_donnees_r = chercher(film_donnees, serie_donnees)
        media_donnees_d = {"Harry Potter 1".lower(): "1998", "Harry Potter 2".lower(): "1999",
                           "Harry Potter 3".lower(): "1999", "Harry Potter 4".lower(): "2001",
                           "Harry Potter 5".lower(): "2003", "Harry Potter 6".lower(): "2005",
                           "Harry Potter 7".lower(): "2007"}
        self.assertDictEqual(media_donnees_r, media_donnees_d)

    @patch('builtins.input', side_effect=["serie", "test"])
    def test_chercher_2(self, mock_inputs):
        film_donnees, serie_donnees = chargement()
        self.assertIsNone(chercher(film_donnees, serie_donnees))


if __name__ == '__main__':
    if not os.path.exists('logs'):
        os.mkdir('logs')
    with open('logs/tests_results.txt', 'w') as f:
        loader = unittest.TestLoader()
        suite = loader.loadTestsFromModule(sys.modules[__name__])
        unittest.TextTestRunner(f, verbosity=2).run(suite)