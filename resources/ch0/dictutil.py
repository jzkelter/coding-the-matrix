# Copyright 2013 Philip N. Klein
def dict2list(dct, keylist): return [dct[k] for k in keylist]

def list2dict(L, keylist): return {k: l for k,l in zip(keylist, L)}

def listrange2dictL(L): return list2dict(L, range(L))
