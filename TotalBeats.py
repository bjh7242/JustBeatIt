#!/usr/bin/env python


def beatReader(fileToRead):

    with open(fileToRead, "r") as fin:
        beats = fin.readlines()

    return beats

def beatCounter(listOfBeats):

    nbeat = 1000000000000000000
    totalBeats = 0

    for beat in listOfBeats:
        beat = beat.strip("\n")
        beat = int(beat)

        if beat < nbeat:
            nbeat = beat
            totalBeats += 1

    return(totalBeats)


btr = beatReader("bpq.txt")
print(beatCounter(btr))

