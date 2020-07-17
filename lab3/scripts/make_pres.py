import csv

states = {}
rows = []
with open("pres.csv","r") as csvfile:
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
        percent_vote = round(float(row[10])/float(row[11])*100,2)
        #election lean is a continous variable that changes our poltical voting to a single interval 0-50 for R 50-100 for D, 
        election_lean = percent_vote
        if party == "D" and percent_vote < 50.0:
            election_lean = round(100.0 - percent_vote,2)
        elif party == "R" and percent_vote > 50.0:
            election_lean = round(100.0 - percent_vote,2)
        if row[1] not in states:
            states[row[1]] = True
            rows.append([row[0],row[1],party, str(percent_vote), str(election_lean)])
    
with open("pres_2016.csv","w") as csvfile:
    csvfile.write(",".join(["year","state","party","percent_vote","election_lean", "\n"]))
    for row in rows:
        csvfile.write(",".join(row)+"\n")


