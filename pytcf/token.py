import sys, csv

default_fields = ["tokenNum", "token", "tokenId", "start", "end", "srcStart", "srcEnd", "lemma", "POStag", "sentenceNum", "sentenceId", "numInSentence"]

class Token(object):
    """A token and further information on it like its ID assigned by the
    tokenizer, the lemma, the POS-tag etc. """

    def getAttrsInOrder(self, order):
        for attr in order:
            yield getattr(self, attr, None)
            

def writeCsv(tokens,
             filename = None,
             attrs = default_fields,
             header = True,
             sortAttr = lambda x: getattr(x, "tokenNum", None)):

    def _strAttr(at):
        if type(at) is unicode:
            return at.encode("utf-8")
        elif at is None:
            return None
        else:
            return unicode(at).encode("utf-8")

    handle = open(filename, 'w') if filename else sys.stdout
    wr = csv.writer(handle, delimiter = ",")
    if header:
        wr.writerow(attrs)
    for tok in sorted(tokens.values(), key=sortAttr):
        wr.writerow([_strAttr(at) for at in tok.getAttrsInOrder(attrs)])
    if handle is not sys.stdout:
        handle.close()
