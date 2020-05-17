import csv
import json
DATE = "2020-05-16"
final_data = []

# get location data
with open('locations.csv') as f:
    csv_data = csv.reader(f)
    for row in csv_data:
        d = {}
        if row[1] != "location" and row[1] != 'World' and row[1] != 'International':
            d["country"] = row[1]
            d["continent"] = row[2]
            try:
                d["population"] = int(row[4])
            except:
                continue
            final_data.append(d)

# get data on Covid cases
length = len(final_data)
l = 0
with open('full_data.csv') as f:
    csv_data = csv.reader(f)
    for row in csv_data:
        if row[0] == DATE:
            for i in final_data:
                if i['country'] == row[1]:
                    i['newCases'] = int(row[2])
                    i['newDeaths'] = int(row[3])
                    i['totalCases'] = int(row[4])
                    i['totalDeaths'] = int(row[5])
                    l += 1
                    break

continents = []
# remove entries with NaN values and 0s
to_del = []
for i,val in enumerate(final_data):
    mistakes = not (val['population'] > 0 and val['totalCases'] > 0 and val['population'] > val['totalCases'] and val['totalDeaths'] < val['totalCases'])
    low_pop = val['population'] < 100000;
    if mistakes or low_pop:
        print(val)
        to_del.append(i)

to_del.reverse()
for i in to_del:
    final_data.pop(i)


# save data
with open("data.json",'w+') as f:
    json.dump(final_data,f,indent=4)
    print("Data saved to : data.json")
