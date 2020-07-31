
import csv

def parse_legis():
    legis = []
    with open("data/state_legis.ssv", "r") as f:
        ssvreader = csv.reader(f, delimiter=" ")
    
        for row in ssvreader:
            legis.append(row)
    return legis
