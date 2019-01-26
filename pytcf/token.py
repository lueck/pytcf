import csv

class Token(object):
    """A token and further information on it like its ID assigned by the
    tokenizer, the lemma, the POS-tag etc. """

    def getAttrsInOrder(self, order):
        for attr in order:
            yield getattr(self, attr, None)
            

def writeCsv(tokens,
             filename,
             attrs = ["tokenNum", "token", "tokenId", "start", "end", "srcStart", "srcEnd", "lemma", "POStag", "sentenceNum", "sentenceId", "numInSentence"],
             sortAttr = lambda x: getattr(x, "tokenNum", None)):

    def _strAttr(at):
        if type(at) is unicode:
            return at.encode("utf-8")
        else:
            return unicode(at).encode("utf-8")
    
    with open(filename, "wb") as csv_file:
        wr = csv.writer(csv_file, delimiter = ",")
        for tok in sorted(tokens.values(), key=sortAttr):
            wr.writerow([_strAttr(at) for at in tok.getAttrsInOrder(attrs)])
