import os
from unittest import TestCase

from pytcf.parser import parseTokens

dirname = os.path.dirname(__file__)
rosenkranz = os.path.join(dirname, "rosenkranz_aesthetik_1853.tcf.xml")

class TestParser(TestCase):
    def test_parseTokens(self):
        t = parseTokens(rosenkranz)
        self.assertEqual(len(t), 140455)
        self.assertEqual(t['w100'].token, u'H\xe4\xdflichen')
        self.assertEqual(t['w100'].lemma, u'H\xe4\xdfliche')
        self.assertEqual(t['w100'].POStag, "NN")
        self.assertEqual(t['w100'].sentenceNum, 18)
        self.assertEqual(t['w100'].numInSentence, 9)
