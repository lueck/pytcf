from xml.etree.ElementTree import iterparse
import logging

from token import Token

def parseTokens(filename,
                tcns = "{http://www.dspin.de/data/textcorpus}",
                tagset = "stts"):

    tokens = {}
    tokenNumber = 1
    sentenceNumber = 1

    logger = logging.getLogger()

    def _getAttr(el, attr, default = None):
        """Case insensitive getter for attribute."""
        if hasattr(el, attr):
            return el.get(attr)
        else:
            attrl = str.lower(attr)
            for at in el.keys():
                if str.lower(at) == attrl:
                    return el.get(at)
            return default
    
    def getTokenIds(elem):
        """Extract the token IDs from a tokenIDs attribute."""
        ids = _getAttr(elem, 'tokenIDs', "")
        for i in ids.split(' '):
            yield i.strip()

    # parse tcf file using a fast stream parser
    for ev, elem in iterparse(filename, events=("start", "end")):

        # parse tokens
        if ev == "start" and str.lower(elem.tag) == tcns + "tokens":
            logger.debug("Parsing token layer...\n")
        if ev == "end" and str.lower(elem.tag) == tcns + "token":
            tid = _getAttr(elem, "ID")
            t = tokens.get(tid, Token())
            t.token = elem.text
            t.tokenId = tid
            t.tokenNum = tokenNumber
            t.start = _getAttr(elem, "start")
            t.end = _getAttr(elem, "end")
            t.srcStart = _getAttr(elem, "srcStart")
            t.srcEnd = _getAttr(elem, "srcEnd")
            tokens[tid] = t
            elem.clear()
            tokenNumber = tokenNumber + 1
        if ev == "end" and str.lower(elem.tag) == tcns + "tokens":
            elem.clear()

        # parse lemmas
        if ev == "start" and str.lower(elem.tag) == tcns + "lemmas":
            logger.debug("Parsing lemma layer...\n")
        if ev == "end" and str.lower(elem.tag) == tcns + "lemma":
            for tid in getTokenIds(elem):
                t = tokens.get(tid, Token())
                t.lemma = elem.text
                tokens[tid] = t
            elem.clear()
        if ev == "end" and str.lower(elem.tag) == tcns + "lemmas":
            elem.clear()
        
        # parse part-of-speach tags
        if ev == "start" and str.lower(elem.tag) == tcns + "postags":
            logger.debug("Parsing postag layer...\n")
            tagset = _getAttr(elem, "{*}tagset", tagset)
        if ev == "end" and str.lower(elem.tag) == tcns + "tag":
            for tid in getTokenIds(elem):
                t = tokens.get(tid, Token())
                t.POStag = elem.text
                t.tagset = tagset
                tokens[tid] = t
            elem.clear()
        if ev == "end" and str.lower(elem.tag) == tcns + "postags":
            elem.clear()
        
        # parse sentences
        if ev == "start" and str.lower(elem.tag) == tcns + "sentences":
            logger.debug("Parsing sentence layer...\n")
        if ev == "end" and str.lower(elem.tag) == tcns + "sentence":
            numberInSentence = 1
            sid = _getAttr(elem, "ID")
            for tid in getTokenIds(elem):
                t = tokens.get(tid, Token())
                t.sentenceId = sid
                t.sentenceNum = sentenceNumber
                t.numInSentence = numberInSentence
                tokens[tid] = t
                numberInSentence = numberInSentence + 1
            sentenceNumber = sentenceNumber + 1
            elem.clear()
        if ev == "end" and str.lower(elem.tag) == tcns + "sentences":            
            elem.clear()
        
    return tokens
