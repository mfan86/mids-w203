import csv

def parse_pres():
    states = {}
    rows = []
    with open("data/pres.csv","r") as csvfile:
        spam = csv.reader(csvfile, delimiter=",")
        for i,row in enumerate(spam):
            if i == 0:
                continue
            if row[0] != "2016":
                continue

            party = row[8]
            if party == "democrat":
                party = "D"
            elif party == "republican":
                party = "R"
            else:
                party = "I"
            percent_vote = str(round(float(row[10])/float(row[11])*100,2))
            if row[1] not in states:
                states[row[1]] = True
                rows.append([row[0],row[1],party, percent_vote])
   
    rows.insert(0,["year","state","party","percent_vote","\n"]) 

    return rows

    #with open("data/pres_2016.csv","w") as csvfile:
    #    csvfile.write(",".join(["year","state","party","percent_vote","\n"]))
    #    for row in rows:
    #        csvfile.write(",".join(row)+"\n")


