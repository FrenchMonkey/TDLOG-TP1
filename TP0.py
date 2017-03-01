#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 11:33:14 2017

@author: wildgrizzly
"""

#Premier tp de tdlog
#tests
#dict = { 0:"obj1" , 3:"I love", "quatre":5}
#
#for clef in dict:
#    print clef
#
#print dict["quatre"]
#
#a = "je"
#b= " taimais"
#print a + b
#print b[len(b):0:-1]

#exo
groups = {
        "1": {"Denmark", "England", "France", "Sweden"},
        "2" : {"CIS", "Germany", "Netherlands", "Scotland"}     
        }

matches = [ 
    ("Sweden",      1, 1, "France"),
    ("Denmark",     0, 0, "England"),
    ("Netherlands", 1, 0, "Scotland"),
    ("CIS", 1, 1, "Germany"),
    ("France", 0, 0, "England"),
    ("Sweden", 1, 0, "Denmark")
    ]

for pays in groups["1"]:
    print pays

def classer(group_nb):
    classement = {}
    for pays in groups[group_nb]:
        pays_stats = [0,0]
        for match in matches:
            #match à domicile
            if (pays == match[0])  == True:
                if (match[1]>match[2]):
                    pays_stats[0] += 3
                    pays_stats[1] += match[1] - match[2]
                if (match[1] == match[2]):
                    pays_stats[0] += 1
                if (match[1] < match[2]):
                    pays_stats[1] += match[1] - match[2]
            #match à l'extérieur
            if (pays == match[3])  == True:
                if (match[2]>match[1]):
                    pays_stats[0] += 3
                    pays_stats[1] += match[2] - match[1]
                if (match[1] == match[2]):
                    pays_stats[0] += 1
                if (match[2] < match[1]):
                    pays_stats[1] += match[2] - match[1]
        classement[pays]=pays_stats
        #on trie
        l = classement.items()
        l = sorted(l, key = lambda l:l[1][0], reverse = True)
    return l

def sign(n):
    if n<0:
        return "-"
    else: 
        return "+"

def print_ranking(group_nb):
    ranks = classer(group_nb)
    n = 18
    for i in ranks:
        i[1][0] = str(i[1][0])
        i[1][1] = sign(i[1][1]) + str(abs(i[1][1]))
        a = i[0] + " " + i[1][0] + "pts" + " " + i[1][1] 
        k = n - len(a)
        rank_to_print = i[0] + " " + "."*k + " "+ i[1][0] + "pts" + " " + i[1][1] 
        print rank_to_print

print_ranking("1")     
                    
def print_matches(matches_t):
    for match in matches_t:
        n = (10 - len(match[0]))
        a = match[0] + " "*n + str(match [1]) + " " + str(match[2]) + " " + match[3]
        print a 
        
print_matches(matches)

    