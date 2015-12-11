#!/bin/bash

if [ "$#" -ne 1 ]; then 
    echo "Please specify the domain to query as the first argument. Ctrl+C to quit"
    exit
fi

while true; do 
    echo -n `date`" " >> bpq.txt
    dig @208.67.222.222 $1 A +norecurse | head -n 15 | egrep $1 | tail -n 1 | awk "{print \$1, \$2}" >> bpq.txt;
done

