# breadth-first search with heuristics culling
#https://stackoverflow.com/questions/890171/algorithm-to-divide-a-list-of-numbers-into-2-equal-sum-lists
import random
import csv
import json

count = 0
with open('data.csv') as f:
   count = sum(1 for _ in f)
print(count)
with open("data.csv") as f:
    lines = f.readlines()
random.shuffle(lines)
with open("mixedData.csv", "w") as f:
    f.writelines(lines)
f.close()

csvfile = open('mixedData.csv', 'r')
jsonfile = open('data.json', 'w')
fieldnames = ("Name","KD","Score")
reader = csv.DictReader( csvfile, fieldnames)
jsonfile.write('{\"team_players\" : [')

m = 0
for row in reader:
    json.dump(row, jsonfile)
    m = m +1
    if m != count: jsonfile.write(',\n')
jsonfile.write(']}')
jsonfile.close()

with open('data.json') as json_file:
    data = json.load(json_file)

    my_list_first = []
    my_list_second = []
    my_list_final = []
    my_list_names = []
    for i in data['team_players']:
        my_list_second.append(float(i['KD']))
        my_list_first.append(float(i['Score']))
        my_list_names.append(i['Name'].encode('utf-8'))
    sum1 = sum(my_list_first)
    sum2 = sum(my_list_second)
    z = 0
    for i in my_list_first :
        avg_p = ((i /sum1 * 100) + (my_list_second[z] / sum2 * 100)) / 2
        my_list_final.append(avg_p)
        z = z + 1

def team(t):
    iterations = range(2, int(len(t) / 2 + 1))
    totalscore = sum(t)
    halftotalscore = totalscore/2.0
    oldmoves = {}

    for p in t:
        people_left = t[:]
        people_left.remove(p)
        oldmoves[p] = people_left

    if iterations == []:
        solution = min(map(lambda i: (abs(float(i)-halftotalscore), i), oldmoves.keys()))
        return (solution[1], sum(oldmoves[solution[1]]), oldmoves[solution[1]])

    for n in iterations:
        newmoves = {}
        for total, roster in oldmoves.items():
            for p in roster:
                people_left = roster[:]
                people_left.remove(p)
                newtotal = total+p
                if newtotal > halftotalscore: continue
                newmoves[newtotal] = people_left
        oldmoves = newmoves

    solution = min(map(lambda i: (abs(float(i)-halftotalscore), i), oldmoves.keys()))
    return (oldmoves[solution[1]])


a = 0
total = sum(my_list_final)
half = total / 2.0
team1 = []
team1Total = sum(team(my_list_final))
team2Total = total - team1Total
print("<b>Diff : </b>",half-team1Total)

if (half-team1Total > 0 ) : team1CT = 1
if (half-team1Total == 0) : team1CT = random.randint(0,1)
if (half-team1Total < 0 ) : team1CT = 0
print ("<font face=Verdana size=5>")
print ("<br><br><b>Team 1 </b>")

if team1CT : print("(CT) :")
else : print ("(T) :")
print("<ul>")
for i in team(my_list_final) :
    team1.append(my_list_names[my_list_final.index(team(my_list_final)[a])])
    a = a + 1
for b in my_list_names :
     if b in team1 :
        print("<li>")
        print(b)
print("</ul>")
team2 = total - sum(team(my_list_final))
print ("<br><br><b>Team 2 </b>")
if ( team1CT == 1) : print("(T) :")
else : print ("(CT) :")
print("<ul>")
for b in my_list_names :
     if b not in team1 :
        print("<li>")
        print(b)
print("</ul>")
print("</font>")