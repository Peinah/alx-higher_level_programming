#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    penny = 0
    mercy = None
    for k, v in a_dictionary.items():
        if v > penny:
            penny = v
            mercy = k
    return mercy
