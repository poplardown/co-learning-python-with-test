import editdistance
import pylev
import Levenshtein
import pyxdameraulevenshtein


def compare(a, b):
    results = {
        'editdistance'          : editdistance.eval(a, b),
        'pylev'                 : pylev.levenshtein(a, b),
        'python-Levenshtein'    : Levenshtein.distance(a, b),
        'pyxdameraulevenshtein' : pyxdameraulevenshtein.damerau_levenshtein_distance(a, b),
    }
    return results

