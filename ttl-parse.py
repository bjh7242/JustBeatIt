#!/usr/bin/env python

x = [] 

with open("bpq.txt","r") as f:
    for line in f:
        # read the list of lists and strip off the newline from each line
        # last field in bpq.txt is the TTL
        x.append(line.split(" ")[-1:][0].strip("\n"))

