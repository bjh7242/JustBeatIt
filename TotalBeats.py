#!/usr/bin/env python
__author__ = "Jared E. Stroud"

'''
    Name: beatReader
    Purpose: fileToRead
    Return: list of strings.
'''
def beatReader(fileToRead):

    with open(fileToRead, "r") as fin:
        beats = fin.readlines()

    return beats

'''
    Name: beatCounter
    Purpose: listofBeats
    Return: integer value.
'''
def beatCounter(listOfBeats):

    nbeat = 1000000000000000000
    totalBeats = 0

    for beat in range(0, len(listOfBeats)):
        if beat != 0 and int(listOfBeats[beat] < listOfBeats[beat-1]):
                totalBeats += 1
    return(totalBeats)

btr = beatReader("bpq.txt")
print(beatCounter(btr))

