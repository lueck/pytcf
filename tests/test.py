# -*- coding: utf-8 -*-

import os
from unittest import TestCase
import tempfile

from pytcf.parser import parseTokens
from pytcf.token import writeCsv

dirname = os.path.dirname(__file__)
rosenkranz = os.path.join(dirname, "rosenkranz_aesthetik_1853.tcf.xml")
kdu = os.path.join(dirname, "KdU1963.tcf.xml")
tokens_behind = os.path.join(dirname, "KdU1963.tokensbehind.tcf.xml")
no_tokens = os.path.join(dirname, "KdU1963.notokens.tcf.xml")


class TestParser(TestCase):
    def test_parseTokensRK(self):
        t = parseTokens(rosenkranz) # test with DTA data
        self.assertEqual(len(t), 140455)
        self.assertEqual(t['w100'].token, u'H\xe4\xdflichen')
        self.assertEqual(t['w100'].lemma, u'H\xe4\xdfliche')
        self.assertEqual(t['w100'].POStag, "NN")
        self.assertEqual(t['w100'].sentenceNum, 18)
        self.assertEqual(t['w100'].numInSentence, 9)

        rosenkranz_csv = tempfile.NamedTemporaryFile(mode="wb")
        writeCsv(t, rosenkranz_csv.name)
        
    def test_parseTokens(self):
        t = parseTokens(kdu)
        self.assertEqual(len(t), 352)
        self.assertEqual(t['w100'].token, u'überschwenglich')
        self.assertEqual(t['w100'].lemma, u'überschwenglich')
        self.assertEqual(t['w100'].POStag, "ADJD")
        self.assertEqual(t['w100'].sentenceNum, 3)
        self.assertEqual(t['w100'].numInSentence, 81)

    def test_parseTokensBehind(self):
        t = parseTokens(tokens_behind)
        self.assertEqual(len(t), 352)
        self.assertEqual(t['w100'].token, u'überschwenglich')
        self.assertEqual(t['w100'].lemma, u'überschwenglich')
        self.assertEqual(t['w100'].POStag, "ADJD")
        self.assertEqual(t['w100'].sentenceNum, 3)
        self.assertEqual(t['w100'].numInSentence, 81)

    def test_parseNoTokens(self):
        t = parseTokens(no_tokens)
        self.assertEqual(len(t), 352)
        #self.assertEqual(t['w100'].token, u'überschwenglich')
        self.assertEqual(t['w100'].lemma, u'überschwenglich')
        self.assertEqual(t['w100'].POStag, "ADJD")
        self.assertEqual(t['w100'].sentenceNum, 3)
        self.assertEqual(t['w100'].numInSentence, 81)

    def test_writeTokens(self):
        t = parseTokens(kdu)
        csvf = tempfile.NamedTemporaryFile(mode="wb")
        writeCsv(t, csvf.name)
        
