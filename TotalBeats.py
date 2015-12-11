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

    totalBeats = 0

    for beat in range(0, len(listOfBeats)):
        if beat != 0 and int(listOfBeats[beat] > listOfBeats[beat-1]):
                totalBeats += 1
    return(totalBeats)

'''
    Name: beatPrints
    Purpose: Print total beats in an innapropriate way.
    Return: 0, (exits)
'''
def beatPrint(intOfBeats):

    print("=" * 25 +  "D\n" \
         "Total counted beats: " + str(intOfBeats) + "\n" + \
         "=" * 25 +  "D")

    return(0)
if __name__ == "__main__":

    btr = beatReader("bpq.txt")
    countedBeats= beatCounter(btr)
    beatPrint(countedBeats)

