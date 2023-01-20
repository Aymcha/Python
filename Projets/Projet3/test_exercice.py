import os
import sys
import unittest
from Exercice import read_file, word_count
def tester_les_2_fichiers():
    ressemblance=True
    with open("database/Result.txt", encoding="utf-8") as f1, open("database/Result_solution.txt") as f2:
        i=1
        for line1 in f1:
            line2 = f2.readline()
            if line1 != line2:
                ressemblance=False
                print(f"la ligne {i} n'est pas identique dans les deux fichiers")
            i+=1
    return ressemblance
class TestExercice(unittest.TestCase):
    def test_readfile(self):
        liste1 = ['lorem', 'ipsum', 'dolor', 'sit', 'amet', 'consectetur', 'adipiscing', 'elit', 'integer', 'nec', 'odio', 'praesent', 'libero', 'sed', 'cursus', 'ante', 'dapibus', 'diam', 'sed', 'nisi', 'nulla', 'quis', 'sem', 'at', 'nibh', 'elementum', 'imperdiet', 'duis', 'sagittis', 'ipsum', 'praesent', 'mauris', 'fusce', 'nec', 'tellus', 'sed', 'augue', 'semper', 'porta', 'mauris', 'massa', 'vestibulum', 'lacinia', 'arcu', 'eget', 'nulla', 'class', 'aptent', 'taciti', 'sociosqu', 'ad', 'litora', 'torquent', 'per', 'conubia', 'nostra', 'per', 'inceptos', 'himenaeos', 'curabitur', 'sodales', 'ligula', 'in', 'libero', 'sed', 'dignissim', 'lacinia', 'nunc', 'curabitur', 'tortor', 'pellentesque', 'nibh', 'aenean', 'quam', 'in', 'scelerisque', 'sem', 'at', 'dolor', 'maecenas', 'mattis', 'sed', 'convallis', 'tristique', 'sem', 'proin', 'ut', 'ligula', 'vel', 'nunc', 'egestas', 'porttitor', 'morbi', 'lectus', 'risus', 'iaculis', 'vel', 'suscipit', 'quis', 'luctus', 'non', 'massa', 'fusce', 'ac', 'turpis', 'quis', 'ligula', 'lacinia', 'aliquet', 'mauris', 'ipsum', 'nulla', 'metus', 'metus', 'ullamcorper', 'vel', 'tincidunt', 'sed', 'euismod', 'in', 'nibh', 'quisque', 'volutpat', 'condimentum', 'velit', 'class', 'aptent', 'taciti', 'sociosqu', 'ad', 'litora', 'torquent', 'per', 'conubia', 'nostra', 'per', 'inceptos', 'himenaeos', 'nam', 'nec', 'ante', 'sed', 'lacinia', 'urna', 'non', 'tincidunt', 'mattis', 'tortor', 'neque', 'adipiscing', 'diam', 'a', 'cursus', 'ipsum', 'ante', 'quis', 'turpis', 'nulla', 'facilisi', 'ut', 'fringilla', 'suspendisse', 'potenti', 'nunc', 'feugiat', 'mi', 'a', 'tellus', 'consequat', 'imperdiet', 'vestibulum', 'sapien', 'proin', 'quam', 'etiam', 'ultrices', 'suspendisse', 'in', 'justo', 'eu', 'magna', 'luctus', 'suscipit', 'sed', 'lectus', 'integer', 'euismod', 'lacus', 'luctus', 'magna', 'quisque', 'cursus', 'metus', 'vitae', 'pharetra', 'auctor', 'sem', 'massa', 'mattis', 'sem', 'at', 'interdum', 'magna', 'augue', 'eget', 'diam', 'vestibulum', 'ante', 'ipsum', 'primis', 'in', 'faucibus', 'orci', 'luctus', 'et', 'ultrices', 'posuere', 'cubilia', 'curae;', 'morbi', 'lacinia', 'molestie', 'dui', 'praesent', 'blandit', 'dolor', 'sed', 'non', 'quam', 'in', 'vel', 'mi', 'sit', 'amet', 'augue', 'congue', 'elementum', 'morbi', 'in', 'ipsum', 'sit', 'amet', 'pede', 'facilisis', 'laoreet', 'donec', 'lacus', 'nunc', 'viverra', 'nec', 'blandit', 'vel', 'egestas', 'et', 'augue', 'vestibulum', 'tincidunt', 'malesuada', 'tellus', 'ut', 'ultrices', 'ultrices', 'enim', 'curabitur', 'sit', 'amet', 'mauris', 'morbi', 'in', 'dui', 'quis', 'est', 'pulvinar', 'ullamcorper', 'nulla', 'facilisi', 'integer', 'lacinia', 'sollicitudin', 'massa', 'cras', 'metus', 'sed', 'aliquet', 'risus', 'a', 'tortor', 'integer', 'id', 'quam', 'morbi', 'mi', 'quisque', 'nisl', 'felis', 'venenatis', 'tristique', 'dignissim', 'in', 'ultrices', 'sit', 'amet', 'augue', 'proin', 'sodales', 'libero', 'eget', 'ante', 'nulla', 'quam', 'aenean', 'laoreet', 'vestibulum', 'nisi', 'lectus', 'commodo', 'ac', 'facilisis', 'ac', 'ultricies', 'eu', 'pede']
        liste2= read_file("database/text.txt")
        self.assertListEqual(liste1,liste2)
    def test_dictionnaire(self):
        dictionnaire, motpluslong, motpluscourt, longueur= word_count(read_file("database/text.txt"))
        motpluslongtest='sollicitudin'
        motpluscourttest="a"
        avg=5.51
        media_donnees_d = {'lorem': 1, 'ipsum': 6, 'dolor': 3, 'sit': 5, 'amet': 5, 'consectetur': 1, 'adipiscing': 2, 'elit': 1, 'integer': 4, 'nec': 4, 'odio': 1, 'praesent': 3, 'libero': 3, 'sed': 10, 'cursus': 3, 'ante': 5, 'dapibus': 1, 'diam': 3, 'nisi': 2, 'nulla': 6, 'quis': 5, 'sem': 5, 'at': 3, 'nibh': 3, 'elementum': 2, 'imperdiet': 2, 'duis': 1, 'sagittis': 1, 'mauris': 4, 'fusce': 2, 'tellus': 3, 'augue': 5, 'semper': 1, 'porta': 1, 'massa': 4, 'vestibulum': 5, 'lacinia': 6, 'arcu': 1, 'eget': 3, 'class': 2, 'aptent': 2, 'taciti': 2, 'sociosqu': 2, 'ad': 2, 'litora': 2, 'torquent': 2, 'per': 4, 'conubia': 2, 'nostra': 2, 'inceptos': 2, 'himenaeos': 2, 'curabitur': 3, 'sodales': 2, 'ligula': 3, 'in': 9, 'dignissim': 2, 'nunc': 4, 'tortor': 3, 'pellentesque': 1, 'aenean': 2, 'quam': 5, 'scelerisque': 1, 'maecenas': 1, 'mattis': 3, 'convallis': 1, 'tristique': 2, 'proin': 3, 'ut': 3, 'vel': 5, 'egestas': 2, 'porttitor': 1, 'morbi': 5, 'lectus': 3, 'risus': 2, 'iaculis': 1, 'suscipit': 2, 'luctus': 4, 'non': 3, 'ac': 3, 'turpis': 2, 'aliquet': 2, 'metus': 4, 'ullamcorper': 2, 'tincidunt': 3, 'euismod': 2, 'quisque': 3, 'volutpat': 1, 'condimentum': 1, 'velit': 1, 'nam': 1, 'urna': 1, 'neque': 1, 'a': 3, 'facilisi': 2, 'fringilla': 1, 'suspendisse': 2, 'potenti': 1, 'feugiat': 1, 'mi': 3, 'consequat': 1, 'sapien': 1, 'etiam': 1, 'ultrices': 5, 'justo': 1, 'eu': 2, 'magna': 3, 'lacus': 2, 'vitae': 1, 'pharetra': 1, 'auctor': 1, 'interdum': 1, 'primis': 1, 'faucibus': 1, 'orci': 1, 'et': 2, 'posuere': 1, 'cubilia': 1, 'curae;': 1, 'molestie': 1, 'dui': 2, 'blandit': 2, 'congue': 1, 'pede': 2, 'facilisis': 2, 'laoreet': 2, 'donec': 1, 'viverra': 1, 'malesuada': 1, 'enim': 1, 'est': 1, 'pulvinar': 1, 'sollicitudin': 1, 'cras': 1, 'id': 1, 'nisl': 1, 'felis': 1, 'venenatis': 1, 'commodo': 1, 'ultricies': 1}
        self.assertDictEqual(dictionnaire, media_donnees_d)
        self.assertEqual(motpluslongtest,motpluslong)
        self.assertEqual(motpluscourttest,motpluscourt)
        self.assertEqual(avg,longueur)
    def test_2fichiers(self):
        ressemblance=tester_les_2_fichiers()
        self.assertIs(ressemblance, True)

if __name__ == '__main__':
    if not os.path.exists('logs'):
        os.mkdir('logs')
    with open('logs/tests_results.txt', 'w') as f:
        loader = unittest.TestLoader()
        suite = loader.loadTestsFromModule(sys.modules[__name__])
        unittest.TextTestRunner(f, verbosity=2).run(suite)