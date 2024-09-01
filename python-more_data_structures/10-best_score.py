#!/usr/bin/python3

def best_score(a_dictionary):
    if not a_dictionary:  # if dictionary is empty or None
        return None  # return None
    
    winner = None  # gamer with the highest score
    high_score = 0  # highest score
    
    for key, value in a_dictionary.items(): # go through scores
        if value > high_score:  # if higher score found
            high_score = value  # update high_score
            winner = key  # that gamer is the winner
    
    return winner  # return gamer with highest score
