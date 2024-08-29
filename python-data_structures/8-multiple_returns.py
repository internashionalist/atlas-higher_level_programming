#!/usr/bin/python3

def multiple_returns(sentence):
    if len(sentence) == 0:  # if sentence is empty
        return (0, None) # return 0 and None
    else:  # return length of sentence and first character
        return (len(sentence), sentence[0])
