import numpy


def union(p,q):
    for e in q:
        if e not in p:
            p.append(e)

