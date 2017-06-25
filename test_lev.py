#import sys
#sys.argv.append('.')
import lev


def test_lev():
    assert lev.compare("abc", "axyz") == {
        'pyxdameraulevenshtein': 3,
        'pylev': 3,
        'python-Levenshtein': 3,
        'editdistance': 3
    }
