import csv

from scripts.make_pres import parse_pres

def main():
    
    #get current data
    #get enriched data from mike's work in excel
    rows = []
    with open("data/covid-19_dist0720_enriched.csv","r") as csvfile:

        spamreader = csv.reader(csvfile, delimiter=",")
        for row in spamreader:
            rows.append(row)
    
    
    #get augmented data
    lgs = parse_legis()

    with open("data/legis.csv","w") as out:
        for r in lgs:
            out.write(",".join(r)+"\n")


def parse_legis():
    legis = []
    with open("data/state_legis.ssv", "r") as f:
        ssvreader = csv.reader(f, delimiter=" ", quotechar='"')
        for row in ssvreader:
            legis.append(row)
    return legis


if __name__ == "__main__":
    main()
