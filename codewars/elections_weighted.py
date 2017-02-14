#title              :elections_weighted.py
#description        :
#                    Many websites use weighted averages of various polls to make projections for elections. 
#                    They re weighted based on a variety of factors, such as historical accuracy of the polling firm, sample size, 
#                    as well as date(s). The weights, in this kata, are already calculated for you. All you need to do is convert
#                    a set of polls with weights, into a fixed projection for the result.
#
#                   Task:
#
#                   Your job is to convert an array of candidates (variable name candidates) and an array of polls (variable 
#                   name polls), each poll with two parts, a result and a weight, into a guess of the result, with each value
#                   rounded to one decimal place, through use of a weighted average. Weights can be zero! Don't worry about 
#                   the sum not totalling 100. The final result should be a hash in Ruby/dictionary in Python/object in JS in 
#                   the format shown below:
#                   { 
#                       "<candidate name 1>": "<candidate's projected percent, rounded to nearest tenth>",
#                       "<candidate name 2>": "<candidate's projected percent, rounded to nearest tenth>",
#                         ...
#                   }

#                   For your convenience, a function named round1 has been defined for you. You can
#                   use it to round to the nearest tenth correctly (due to the inaccuracy of round
#                   and floats in general).

#author             : Jose Fernando Gonzalez
#date               : 20170213
#version            : 0.1
#usage              : python high_profit.py
#notes              : Kata from codewars
#python_version     : 3.4.3


candidates = ["A", "B", "C"]

poll1res = [20, 30, 50]
poll1wt = 1
poll1 = [poll1res, poll1wt]

poll2res = [40, 40, 20]
poll2wt = 0.5
poll2 = [poll2res, poll2wt]

poll3res = [50, 40, 10]
poll3wt = 2
poll3 = [poll3res, poll3wt]

polls = [poll1, poll2, poll3]


def predict(candidates, polls):
    sum_w = 0
    wr = [0] * len(candidates)
    for candidate in candidates:
        sum_w = 0
        for poll in polls:
            wr[candidates.index(candidate)]+=poll[0][candidates.index(candidate)]*poll[1]
            sum_w += poll[1]
    list_res = [round((x / sum_w) + 1e-4, 1) for x in wr]
    D = { candidates[i]: list_res[i] for i in range(0,len(candidates)) }
    return D


predict(candidates, polls)