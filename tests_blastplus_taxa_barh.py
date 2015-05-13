#!/usr/bin/env python

import pandas
import unittest
from blastplus_taxa_barh import *

__author__ = "Paul Johnston"
__contact__ = "paul.johnston[at]fu-berlin.de"

class test_blast_parse(unittest.TestCase):
    
    def test_blast_in(self):
        known_frame = pandas.io.pickle.read_pickle("test_data/test_frame.pkl")
        test_frame = blast_in("test_data/outfmt6.all.uniq")
        try:
            pandas.util.testing.assert_frame_equal(known_frame, test_frame, check_names=False)
            return True
        except (AssertionError, ValueError, TypeError):
            return False

    def test_genus(self):
        known_series = pandas.io.pickle.read_pickle("test_data/test_series.pkl")
        known_frame = pandas.io.pickle.read_pickle("test_data/test_frame.pkl")
        test_series = genus(known_frame, int(12), int(15))
        try:
            pandas.util.testing.assert_series_equal(known_series, test_series)
            return True
        except (AssertionError, ValueError, TypeError):
            return False

if __name__ == '__main__':
    unittest.main()
