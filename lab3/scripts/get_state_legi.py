
import requests
from bs4 import BeautifulSoup

#data is pulled from ballotpedia.org
senates_html = requests.get("https://ballotpedia.org/Partisan_composition_of_state_senates")
#legis_html = requests.get("https://ballotpedia.org/Partisan_composition_of_state_legislatures")
#houses_html = requests.get("https://ballotpedia.org/Partisan_composition_of_state_houses")

#State list
state_str = """
Alabama - AL
Alaska - AK
Arizona - AZ
Arkansas - AR
California - CA
Colorado - CO
Connecticut - CT
Delaware - DE
Florida - FL
Georgia - GA
Hawaii - HI
Idaho - ID
Illinois - IL
Indiana - IN
Iowa - IA
Kansas - KS
Kentucky - KY
Louisiana - LA
Maine - ME
Maryland - MD
Massachusetts - MA
Michigan - MI
Minnesota - MN
Mississippi - MS
Missouri - MO
Montana - MT
Nebraska - NE
Nevada - NV
New Hampshire - NH
New Jersey - NJ
New Mexico - NM
New York - NY
North Carolina - NC
North Dakota - ND
Ohio - OH
Oklahoma - OK
Oregon - OR
Pennsylvania - PA
Rhode Island - RI
South Carolina - SC
South Dakota - SD
Tennessee - TN
Texas - TX
Utah - UT
Vermont - VT
Virginia - VA
Washington - WA
West Virginia - WV
Wisconsin - WI
Wyoming - WY
"""
states = []
s1 = state_str.split("\n")
for s in s1:
    if s:
        state_name = s.split("-")[0]
        states.append(state_name)

soup = BeautifulSoup(senates_html.content, 'html.parser')

headlines = soup.find_all("span", {"class":"mw-headline"})
t = soup.find_all("table")

print(len(states))

for i,item in enumerate(t):
    cls = item.get("class")
    if cls and cls[0] == "wikitable":
        tr = item.find_all("tr")
        for row in tr:
            th = row.find_all("th")
            #print(th)
            print(th)
