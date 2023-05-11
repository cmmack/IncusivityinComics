import csv

with open ('dc-wikia-data.csv', 'r') as dcomicsdata:
    dcharacters = csv.reader(dcomicsdata)
    with open ('FinalStartdata.csv', 'w') as writedcomicsdata:
        dcharactersdata = csv.writer(writedcomicsdata)    
        for row in dcharacters:
            
            date = row[12]
            if date >= "2000": 
               
                sexuality = row[8]
                if sexuality != '':            
            

                    dcharactersdata.writerow(row)


with open ('marvel-wikia-data.csv', 'r') as mcomicsdata:
    mcharacters = csv.reader(mcomicsdata)
    with open ('FinalStartdata.csv', 'w') as writemcomicsdata:
        mcharactersdata = csv.writer(writemcomicsdata)    
        for row in mcharacters:
            
            date = row[12]
            if date >= "2000": 
               
                sexuality = row[8]
                if sexuality != '':            
        
                    mcharactersdata.writerow(row)





