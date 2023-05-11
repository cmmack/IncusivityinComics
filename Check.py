import csv

with open ('dc-wikia-data.csv', 'r') as wdcomicsdata:
    wdcharacters = csv.reader(wdcomicsdata)
    with open ('Finaldata.csv', 'w') as writewdcomicsdata:
        wdcharactersdata = csv.writer(writewdcomicsdata)
        for row in wdcharacters:

            sex = row[7]

        if sex == "Female Characters":

                wdcharactersdata.writerow(row)


with open ('marvel-wikia-data.csv', 'r') as wmcomicsdata:
    wmcharacters = csv.reader(wmcomicsdata)
    with open ('Finaldata.csv', 'w') as writewmcomicsdata:
        wmcharactersdata = csv.writer(writewmcomicsdata)
        for row in wmcharacters:

            sex = row[7]

        if sex == "Female Characters":

                wmcharactersdata.writerow(row)



    

       


        