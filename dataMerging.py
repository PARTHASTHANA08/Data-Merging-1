import csv 
dataSet1 = []
dataSet2 = []
with open("bright_stars.csv","r") as f:
    csvReader = csv.reader(f)
    for row in csvReader : 
        dataSet1.append(row)
        star_mass = dataSet1[3] 
        starMassValue = float(star_mass) * 0.000954588
        dataSet1[3] = starMassValue
        star_radius = dataSet1[4]
        starRadiusValue = float(star_radius) * 0.102763
        dataSet1[4] = starRadiusValue
with open("dwarf_stars.csv","r") as f:
    csvReader = csv.reader(f)
    for row in csvReader :
        dataSet2.append(row)
        starMass1 = dataSet2[4]
        starmassvalue1 = float(starMass1) * 0.000954588
        dataSet2[4] = starmassvalue1
        starRadius1 = dataSet2[5]
        starradiusvalue1 = float(starRadius1) * 0.102763
        dataSet2[5] = starradiusvalue1
header1 = dataSet1[0]
stardata1 = dataSet1[1:]
header2 = dataSet2[0]
stardata2 = dataSet2[1:]
headers = header1 + header2
starData = []     
for index,data_row in enumerate():
    starData.append(stardata1[index] + stardata2[index])
with open("final.csv","a+") as f:
    csvWriter = csv.writer(f)
    csvWriter.writerow(headers)
    csvWriter.writerows(starData)    
