from xml.etree.ElementTree import iterparse
import logging

from pytcf.token import Token

def parseTokens(filename):

    tokens = {}
    tagset = "stts"

    tcns = "{http://www.dspin.de/data/textcorpus}"

    logger = logging.getLogger()

    def getElementId(el):
        return el.get("ID", "nichtgefunden") #, elem.get('id', elem.get('{*}Id', "NONE")))
    
    def getTokenIds(elem):
        ids = elem.get('tokenIDs', "nix") # elem.get('{*}tokenids', elem.get('{*}tokenIds', "")))
        for i in ids.split(' '):
            yield i.strip()
            
    for ev, elem in iterparse(filename, events=("start", "end")):

        # if ev == "start":
        #     logger.debug("Found %s element", elem.tag)
        #     print(elem.tag + "\n")
        
        # parse tokens
        if ev == "start" and str.lower(elem.tag) == tcns + "tokens":
            logger.debug("Parsing token layer...\n")
        if ev == "end" and str.lower(elem.tag) == tcns + "token":
            tid = getElementId(elem)
            t = tokens.get(tid, Token())
            t.token = elem.text
            tokens[tid] = t
            elem.clear()
        if ev == "end" and str.lower(elem.tag) == tcns + "tokens":
            elem.clear()

        # parse lemmas
        if ev == "start" and str.lower(elem.tag) == tcns + "lemmas":
            logger.debug("Parsing lemma layer...\n")
        if ev == "end" and str.lower(elem.tag) == tcns + "lemma":
            for tid in getTokenIds(elem):
                t = tokens.get(tid, Token())
                t.lemma = elem.text
            elem.clear()
        if ev == "end" and str.lower(elem.tag) == tcns + "lemmas":
            elem.clear()

        # parse part-of-speach tags
        if ev == "start" and str.lower(elem.tag) == tcns + "postags":
            logger.debug("Parsing postag layer...\n")
            tagset = elem.get("{*}tagset", tagset)
        if ev == "end" and str.lower(elem.tag) == tcns + "tag":
            for tid in getTokenIds(elem):
                t = tokens.get(tid, Token())
                t.POStag = elem.text
                t.tagset = tagset
            elem.clear()
        if ev == "end" and str.lower(elem.tag) == tcns + "postags":
            elem.clear()
            
        # parse sentences
        if ev == "start" and str.lower(elem.tag) == tcns + "sentences":
            logger.debug("Parsing sentence layer...\n")
        if ev == "end" and str.lower(elem.tag) == tcns + "sentence":
            sid = elem.get("ID", "nichtgefunden") #getElementId(elem)
            for tid in getTokenIds(elem):
                t = tokens.get(tid, Token())
                t.sentence = sid
            elem.clear()
        if ev == "end" and str.lower(elem.tag) == tcns + "sentences":            
            elem.clear()

            
    return tokens
