import random as r
import math


def rand(i):
    return i * r.random()/2


def dist(source, target):
    if source is None or target is None:
        return 2000
    return math.sqrt((source.left - target.left)**2 + (source.top - target.top)**2)
